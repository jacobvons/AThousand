from django.shortcuts import render
from datetime import date

from rest_framework import status
from rest_framework.response import Response

from .models import *
from .serializers import *
import random
import os


def days_together():
    day_one = date(2019, 8, 25)
    today = date.today()
    return abs((day_one - today).days)


def get_random_pk(obj_class):
    all_pks = list(obj_class.objects.filter().values_list("pk", flat=True))
    random_pk = all_pks[random.randint(0, len(all_pks)-1)]
    return random_pk


def homepage(request):
    context = {"days_together": days_together()}
    return render(request, "homepage/home.html", context)


def foods_home(request):
    food = Food.objects.get(pk=get_random_pk(Food))
    all_pks = list(Food.objects.values_list("pk", flat=True))
    context = {"food": food, "all_pks": all_pks}
    return render(request, "homepage/foodsHome.html", context)


class FoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all().order_by('pk')
    serializer_class = FoodSerializer


def movies_home(request):
    movie = Movie.objects.get(pk=get_random_pk(Movie))
    all_pks = list(Movie.objects.values_list("pk", flat=True))
    context = {"movie": movie, "all_pks": all_pks}
    return render(request, "homepage/moviesHome.html", context)


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all().order_by('pk')
    serializer_class = MovieSerializer


def musics_home(request):
    music = Music.objects.get(pk=get_random_pk(Music))
    all_pks = list(Music.objects.values_list("pk", flat=True))
    context = {"music": music, "all_pks": all_pks}
    return render(request, "homepage/musicsHome.html", context)


class MusicViewSet(viewsets.ModelViewSet):
    queryset = Music.objects.all().order_by('pk')
    serializer_class = MusicSerializer


def photos_home(request):
    photo = Photo.objects.get(pk=get_random_pk(Photo))
    all_pks = list(Photo.objects.values_list("pk", flat=True))
    context = {"photo": photo, "all_pks": all_pks}
    return render(request, "homepage/photosHome.html", context)


class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all().order_by('pk')
    serializer_class = PhotoSerializer


def places_home(request):
    place = Place.objects.get(pk=get_random_pk(Place))
    all_pks = list(Place.objects.values_list("pk", flat=True))
    context = {"place": place, "all_pks": all_pks}
    return render(request, "homepage/placesHome.html", context)


class PlaceViewSet(viewsets.ModelViewSet):
    queryset = Place.objects.all().order_by('pk')
    serializer_class = PlaceSerializer


def words_home(request):
    word = Word.objects.get(pk=get_random_pk(Word))
    all_pks = list(Word.objects.values_list("pk", flat=True))
    context = {"word": word, "all_pks": all_pks}
    return render(request, "homepage/wordsHome.html", context)


class WordViewSet(viewsets.ModelViewSet):
    queryset = Word.objects.all().order_by('pk')
    serializer_class = WordSerializer
