from rest_framework import serializers

from .models import *


class FoodSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Food
        fields = ("pk", "title", "date", "description", "img", "by")


class MovieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Movie
        fields = ("pk", "title", "date", "description", "img")


class MusicSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Music
        fields = ("pk", "title", "date", "description", "img", "by")


class PhotoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Photo
        fields = ("pk", "title", "description", "img", "by", "date")


class PlaceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Place
        fields = ("pk", "title", "description", "img", "date_start", "date_end", "address")


class WordSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Word
        fields = ("pk", "title", "description", "img", "date", "by", "content")
