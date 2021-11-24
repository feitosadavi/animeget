from rest_framework import serializers
from .models import Album, Music

class MusicSerializer(serializers.ModelSerializer):
	class Meta:
		model = Music
		fields = '__all__'

class AlbumSerializer(serializers.ModelSerializer):
	class Meta:
		model = Album
		fields = '__all__'
