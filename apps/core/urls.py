
from django.urls import path


from .views import its_alive_view

app_name = 'core'

urlpatterns = [path('its_alive', its_alive_view, name="itsalive")]
