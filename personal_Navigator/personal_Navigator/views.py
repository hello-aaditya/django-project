#manually i'm written this file views.py

from django.http import HttpResponse

def index(request):
    content = '''
    <a href="https://chat.openai.com/">ChatGPT-3.5</a><br>
    <a href="https://www.notion.so/">Notion</a><br>
    <a href="https://www.w3schools.com/">W3 School</a><br>
    <a href="https://www.canva.com/">Canva</a><br>
    <a href="https://www.coursera.org/">COURSERA</a>
    '''
    return HttpResponse(content)

