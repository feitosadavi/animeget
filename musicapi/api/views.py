from rest_framework import generics
from .models import Album, Band, Music
from .serializers import AlbumSerializer, BandSerializer, MusicSerializer

class MusicList(generics.ListCreateAPIView):
	queryset = Music.objects.all()
	serializer_class = MusicSerializer

class AlbumList(generics.ListCreateAPIView):
	queryset = Album.objects.all()
	serializer_class = AlbumSerializer

class BandList(generics.ListCreateAPIView):
	queryset = Band.objects.all()
	serializer_class = BandSerializer
