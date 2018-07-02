
from django.urls import path, re_path


from .views import HomeView, ListAnimalWeigth, CreateAnimalWeigth, UpdateAnimalWeigth

from .apiviews import GetAnimalWeigthCNPJ, GetAnimalWeigthToken

app_name = 'animal_weigth'

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    re_path(
        r'animal-weigth/(?P<farm>[a-zA-Z0-9._]+)/$',
        ListAnimalWeigth.as_view(),
        name="list_animal_weigth",
    ),
    re_path(
        r'animal-weigth/create/(?P<farm>[a-zA-Z0-9._]+)/$',
        CreateAnimalWeigth.as_view(),
        name="create_animal_weigth",
    ),
    re_path(
        r'animal-weigth/edit/(?P<pk>[0-9]+)/$',
        UpdateAnimalWeigth.as_view(),
        name="edit_animal_weigth",
    ),
    re_path(
        r'api/v1/animal-weigth-cnpj/(?P<cnpj>[a-zA-Z0-9._]+)/$',
        GetAnimalWeigthCNPJ.as_view(),
        name="get_animals_cnpj",
    ),
    re_path(
        r'api/v1/animal-weigth-cnpj/(?P<token>[a-zA-Z0-9._]+)/(?P<earring_number>[a-zA-Z0-9._]+)/$',
        GetAnimalWeigthToken.as_view(),
        name="get_animals_token",
    ),
]
