from django.test import TestCase
from django.urls import reverse
from .models import Letting

class LettingsTest(TestCase):

    def test_index_lettings(self):
        response = self.client.get(reverse('lettings:index'))
        assert b"<title>Lettings</title>" in response.content
        assert response.status_code == 200

    def test_letting(self):
        lettings = Letting.objects.all()
        for letting in lettings:
            response = self.client.get(reverse('lettings:letting', args=[letting.id]))
            assert letting.title in response.content
            assert response.status_code == 200


