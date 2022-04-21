from django.urls import path, include
from rest_framework import routers
from . import views


# router = routers.DefaultRouter()
# router.register('foods', views.FoodViewSet)

food_router = routers.DefaultRouter()
food_router.register('foods', views.FoodViewSet)

movie_router = routers.DefaultRouter()
movie_router.register('movies', views.MovieViewSet)

music_router = routers.DefaultRouter()
music_router.register('musics', views.MusicViewSet)

photo_router = routers.DefaultRouter()
photo_router.register('photos', views.PhotoViewSet)

place_router = routers.DefaultRouter()
place_router.register('places', views.PlaceViewSet)

word_router = routers.DefaultRouter()
word_router.register('words', views.WordViewSet)


urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('foods/', views.foods_home, name="foods"),
    path('movies/', views.movies_home, name="movies"),
    path('musics/', views.musics_home, name="musics"),
    path('places/', views.places_home, name="places"),
    path('words/', views.words_home, name="words"),
    path('photos/', views.photos_home, name="photos"),

    path('food_router/', include(food_router.urls)),
    path('movie_router/', include(movie_router.urls)),
    path('music_router/', include(music_router.urls)),
    path('photo_router/', include(photo_router.urls)),
    path('place_router/', include(place_router.urls)),
    path('word_router/', include(word_router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
