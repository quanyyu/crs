import gevent

from celery.utils.log import get_task_logger
logger = get_task_logger(__name__)

import requests
from celery import shared_task
from pydub import AudioSegment
from random_user_agent.user_agent import UserAgent

UA_GEN = UserAgent()

@shared_task
def test_task():
    return "test"

@shared_task(bind=True)
def convert_flac_mp3(self, path):
    song = AudioSegment.from_file(path)
    song.export(path.replace(".flac", ".mp3"), format="mp3")

@shared_task(bind=True)
def download_jay_song(self, name:str, url:str):
    gevent.spawn(_download_jay_song, self, name, url)
    logger.info("issue complete")

def _download_jay_song(self, name:str, url:str):
    rsp = requests.get(url, headers = {"User-Agent": UA_GEN.get_random_user_agent()})
    flac_path = "/mnt/d/CloudMusic/" + name + ".flac"
    with open(flac_path, "wb") as f:
        f.write(rsp.content)
    
    song = AudioSegment.from_file(flac_path)
    song.export(flac_path.replace(".flac", ".mp3"), format="mp3")