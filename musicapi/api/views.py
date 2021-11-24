from rest_framework import generics
from .models import Album, Music
from .serializers import AlbumSerializer, MusicSerializer

class MusicList(generics.ListCreateAPIView):
	queryset = Music.objects.all()
	serializer_class = MusicSerializer

class AlbumList(generics.ListCreateAPIView):
	queryset = Album.objects.all()
	serializer_class = AlbumSerializer
