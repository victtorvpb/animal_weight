
from django.urls import path


from .views import HomeView

app_name = 'animal_weigth'

urlpatterns = [path('', HomeView.as_view(), name="home")]
