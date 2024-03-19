#manually i'm created this file

from django.http import HttpResponse

def index(request):
    file = open("myFile.txt",'r+')
    return HttpResponse(file.read())