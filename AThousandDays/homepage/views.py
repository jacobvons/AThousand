from django.shortcuts import render


def homepage(request):
    return render(request, "homepage/home.html")


def foods_home(request):
    return render(request, "homepage/foodsHome.html")


def movies_home(request):
    return render(request, "homepage/moviesHome.html")


def musics_home(request):
    return render(request, "homepage/musicsHome.html")


def photos_home(request):
    return render(request, "homepage/photosHome.html")


def places_home(request):
    return render(request, "homepage/placesHome.html")


def words_home(request):
    return render(request, "homepage/wordsHome.html")