from django.test import TestCase
from django.urls import reverse

class LettingsTest(TestCase):
    
    def test_index_lettings(self):
        response = self.client.get(reverse('lettings:index'))
        assert b"<title>Lettings</title>" in response.content
        assert response.status_code == 200

