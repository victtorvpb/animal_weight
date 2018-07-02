
from django.urls import path, re_path


from .views import HomeView, ListAnimalWeigth

app_name = 'animal_weigth'

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    re_path(
        r'animal-weigth/(?P<farm>[a-zA-Z0-9._]+)/$',
        ListAnimalWeigth.as_view(),
        name="list_animal_weigth",
    ),
]
