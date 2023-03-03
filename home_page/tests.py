from django.test import TestCase
from django.urls import reverse


class HomePageTest(TestCase):

    def test_index_home(self):
        response = self.client.get(reverse('home_page:index'))
        assert b"<h1>Welcome to Holiday Homes</h1>" in response.content
        assert response.status_code == 200
