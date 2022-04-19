from django.urls import path

from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('foods/', views.foods_home, name="foods"),
    path('movies/', views.movies_home, name="movies"),
    path('musics/', views.musics_home, name="musics"),
    path('places/', views.places_home, name="places"),
    path('words/', views.words_home, name="words"),
    path('photos/', views.photos_home, name="photos"),
]
