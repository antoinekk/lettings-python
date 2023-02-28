from django.test import TestCase
from django.urls import reverse
from .models import Profile

class ProfilesTest(TestCase):
    
    def test_index_profiles(self):
        response = self.client.get(reverse('profiles:index'))
        assert b"<title>Profiles</title>" in response.content
        assert response.status_code == 200
    
    def test_profile(self):
        profiles = Profile.objects.all()
        for profile in profiles:
            response = self.client.get(reverse('profiles:profile', args=[profile.id]))
            assert profile.title in response.content
            assert response.status_code == 200
