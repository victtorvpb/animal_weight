from django.contrib import admin
from .models import FarmModel, AnimalWeigthModel

# Register your models here.

admin.site.register(FarmModel)
admin.site.register(AnimalWeigthModel)
