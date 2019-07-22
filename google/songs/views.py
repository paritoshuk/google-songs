from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from songs.models import Songs, SongsFixed
from songs.serializers import SongSerializer, FixedSongsSerializer
from random import randint
from django.template import loader
from django.http import HttpResponse


# Create your views here.


def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render({}, request))


def results(request):
    link = request.GET['q']
    array = []
    template = loader.get_template('search_results.html')
    randomnumber = getRandomNumber()
    for x in randomnumber:
        obj = SongsFixed.objects.get(pk=x)
        array.append(obj.songs_path)
    context = {
        'link': link,
        'songs': array
    }
    return HttpResponse(template.render(context, request))


@api_view(['POST'])
def songs(request):
    if request.method == 'POST':
        serializer = SongSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            res = [True]
            return Response(res, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET'])
# def results(request):
#     """
#     List all code snippets, or create a new snippet.
#     """
#     if request.method == 'GET':
#         array = []
#         q = request.GET['q']
#         arr = getRandomNumber()
#         for x in arr:
#             obj = SongsFixed.objects.get(pk=x)
#             array.append(obj.songs_path)
#         return Response(array)


def getRandomNumber():
    array = []
    for x in range(3):
        array.append(randint(1, 10))
    return array
