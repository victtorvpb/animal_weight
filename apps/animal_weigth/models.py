from django_extensions.db.models import TimeStampedModel
from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class FarmModel(TimeStampedModel):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.PROTECT)
    name = models.CharField(max_length=100,
                            verbose_name=_('Name'),
                            null=False,
                            blank=False)
    
    cnpj = models.CharField(verbose_name=_('CNPJ'),
                            null=False,
                            blank=False,
                            max_length=18,
                            unique=True)
