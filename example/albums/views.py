from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.response import Response

from .models import Album, Artist, Genre
from .serializers import AlbumSerializer, ArtistSerializer


def index(request):
    return render(request, 'albums/albums.html')


def get_album_options():
    return "options", {
        "artist": [{'label': obj.name, 'value': obj.pk} for obj in Artist.objects.all()],
        "genre": [{'label': obj.name, 'value': obj.pk} for obj in Genre.objects.all()]
    }


class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all().order_by('rank')
    serializer_class = AlbumSerializer


class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all().order_by('name')
    serializer_class = ArtistSerializer

