from random_user_agent.user_agent import UserAgent
import requests
import json
from django.shortcuts import render
from django.http import HttpResponse
from .models import JaySong
from .tasks import test_task


# Create your views here.

JAY_SONG_JSON_URL = "https://gist.githubusercontent.com/lvyueyang/cb11eaafbe69fc7ba63c38f9ff40e0d9/raw/a33540e7bb5e75557d9079a47e52b67c40cbad52/jay-music.json"
UA_GENER = UserAgent()

def parse_file(request):

    dic = requests.get(JAY_SONG_JSON_URL, headers={"User-Agent": UA_GENER.get_random_user_agent()}).json()

    song_list = dic["list"]    
    for song in song_list:
        song_do = JaySong()
        song_do.id = int(song["id"])
        song_do.cid = song["cid"]
        song_do.name = song["name"]
        song_do.song_info = json.dumps(song["songInfo"])
        song_do.flac_url = song["songInfo"].get("flac", song["songInfo"].get("320"))
        song_do.save()

    return HttpResponse(content=b"ok")

def ce_test(request):
    r = test_task.delay()
    a = r.get()
    res = {
        "result": a,
        "id": r.id
    }
    return HttpResponse(content=json.dumps(res))

