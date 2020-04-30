from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hi(request):
    return HttpResponse("<h1>BEAU'S TIC TAC TOE GAME</h1>")
