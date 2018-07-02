from rest_framework import serializers
from .models import AnimalWeigthModel


class GetAnimalWeigthCnpjSerializer(serializers.ModelSerializer):
    type_animal = serializers.SerializerMethodField()

    class Meta:
        model = AnimalWeigthModel
        exclude = ['modified', 'created']

    def get_type_animal(self, obj):
        return obj.get_type_animal_display()
