from rest_framework.views import APIView
from rest_framework.response import Response

from .models import AnimalWeigthModel
from .serializers import GetAnimalWeigthCnpjSerializer


class GetAnimalWeigthCNPJ(APIView):
    def get(self, request, cnpj=None, format=None):

        register = AnimalWeigthModel.objects.filter(farm__cnpj=cnpj)

        serializer = GetAnimalWeigthCnpjSerializer(register, many=True)
        return Response(serializer.data)


class GetAnimalWeigthToken(APIView):
    def get(self, request, token=None, earring_number=None, format=None):

        register = AnimalWeigthModel.objects.filter(
            farm__token=token, earring_number=earring_number
        )

        serializer = GetAnimalWeigthCnpjSerializer(register, many=True)
        return Response(serializer.data)
