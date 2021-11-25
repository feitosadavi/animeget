from rest_framework import generics
from .models import Album, Band, Member, Music
from .serializers import AlbumSerializer, BandSerializer, MemberSerializer, MusicSerializer
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated

class MusicList(generics.ListCreateAPIView):
	queryset = Music.objects.all()
	serializer_class = MusicSerializer
	authentication_classes = [SessionAuthentication]
	permission_classes = (IsAuthenticated,)

class MusicDetail(generics.RetrieveUpdateAPIView):
	queryset = Music.objects.all()
	serializer_class = MusicSerializer
	authentication_classes = [SessionAuthentication]
	permission_classes = (IsAuthenticated,)

class AlbumList(generics.ListCreateAPIView):
	queryset = Album.objects.all()
	serializer_class = AlbumSerializer
	authentication_classes = [SessionAuthentication]
	permission_classes = (IsAuthenticated,)

class AlbumDetail(generics.RetrieveUpdateAPIView):
	queryset = Album.objects.all()
	serializer_class = AlbumSerializer
	authentication_classes = [SessionAuthentication]
	permission_classes = (IsAuthenticated,)

class BandList(generics.ListCreateAPIView):
	queryset = Band.objects.all()
	serializer_class = BandSerializer
	authentication_classes = [SessionAuthentication]
	permission_classes = (IsAuthenticated,)

class BandDetail(generics.RetrieveUpdateAPIView):
	queryset = Band.objects.all()
	serializer_class = BandSerializer
	authentication_classes = [SessionAuthentication]
	permission_classes = (IsAuthenticated,)

class MemberList(generics.ListCreateAPIView):
	queryset = Member.objects.all()
	serializer_class = MemberSerializer
	authentication_classes = [SessionAuthentication]
	permission_classes = (IsAuthenticated,)

class MemberDetail(generics.RetrieveUpdateAPIView):
	queryset = Member.objects.all()
	serializer_class = MemberSerializer
	authentication_classes = [SessionAuthentication]
	permission_classes = (IsAuthenticated,)
