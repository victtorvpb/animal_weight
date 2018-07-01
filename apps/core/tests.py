from django.test import TestCase
from django.urls import reverse


class TestsItsAliveView(TestCase):

    def test_page_its_alive_200(self):
        url = reverse('core:itsalive')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)