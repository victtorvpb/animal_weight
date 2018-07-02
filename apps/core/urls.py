
from django.urls import path, re_path


from .views import its_alive_view, login

app_name = 'core'

urlpatterns = [path('its_alive', its_alive_view, name="itsalive"),
re_path(r'^login/$', login, name="login")]
