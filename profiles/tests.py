from django.test import TestCase
from django.urls import reverse

class ProfilesTest(TestCase):
    
    def test_index_profiles(self):
        response = self.client.get(reverse('profiles:index'))
        assert b"<title>Profiles</title>" in response.content
        assert response.status_code == 200
