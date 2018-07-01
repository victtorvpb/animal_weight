from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User


class TestsHome(TestCase):
    def setUp(self):
        self.name = 'test'
        self.password = 'teste01'
        self.user = User.objects.create_user(self.name, 'teste@test.com', self.password)

    def test_home_page_200(self):
        self.client.login(username=self.name, password=self.password)
        url = reverse('animal_weigth:home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
