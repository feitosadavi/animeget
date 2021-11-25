from django.test import TestCase
from rest_framework.test import APIClient, APIRequestFactory
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User

from .models import Music
from .views import MusicList

class TestMusicListView(TestCase):
	def setUp(self):
		self.factory = APIRequestFactory()
		self.view = MusicList.as_view()
		self.client = APIClient()
		self.music = Music.objects.create(title='Panda', seconds='220')
		self.user = User.objects.create_user('davif', 'davif@email.com', '123')
		self.data = {
			'title': 'Back In Black',
			'seconds': '193'
		}
	
	# Should MusicList view return 200 on GET if user is authenticated
	def test_music_list_view_success_status_code(self):
		url = reverse('api:music-list')
		request = self.factory.get(url)
		request.user = self.user
		response = self.view(request)
		self.assertEquals(response.status_code, status.HTTP_200_OK)
