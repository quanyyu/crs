from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("hellow world")

def gg(request):
    return render(request, "index.html", {"gg": 'hello world'})