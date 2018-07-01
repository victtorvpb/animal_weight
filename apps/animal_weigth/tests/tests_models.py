from django.test import TestCase
from django.contrib.auth.models import User

from apps.animal_weigth.models import FarmModel, AnimalWeigthModel
from apps.animal_weigth.choices import AnimalChoice


class TestModelFarm(TestCase):
    '''
        Test model Farm
    '''

    def setUp(self):
        self.user = User.objects.create_user(
            username='teste', email='teste@test.com', password='test'
        )

    def test_insert_farm(self):
        farm = FarmModel.objects.create(owner=self.user, name='Farm', cnpj='93.822.024/0001-07')

        self.assertEqual(farm.owner, self.user)


class TestModelAnimalWeigth(TestCase):
    '''
        Test model Farm
    '''

    def setUp(self):
        self.user = User.objects.create_user(
            username='teste', email='teste@test.com', password='test'
        )
        self.farm = FarmModel.objects.create(
            owner=self.user, name='Farm', cnpj='93.822.024/0001-07'
        )

    def test_insert_animal(self):
        animal = AnimalWeigthModel.objects.create(
            farm=self.farm, type_animal=AnimalChoice.bovino, weigth=1290.32, earring_number=3621
        )

        self.assertEqual(animal.farm, self.farm)
