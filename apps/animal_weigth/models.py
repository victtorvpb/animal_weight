import secrets

from django_extensions.db.models import TimeStampedModel
from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from dj.choices.fields import ChoiceField

from .choices import AnimalChoice


class FarmModel(TimeStampedModel):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    name = models.CharField(max_length=100, verbose_name=_('Name'), null=False, blank=False)

    cnpj = models.CharField(
        verbose_name=_('CNPJ'), null=False, blank=False, max_length=18, unique=True
    )

    token = models.CharField(
        verbose_name=_('token'), max_length=30, unique=True, default=secrets.token_hex(30)
    )

    def __str__(self):
        return 'Fazenda {} de CNPJ {}'.format(self.name, self.cnpj)


class AnimalWeigthModel(TimeStampedModel):
    farm = models.ForeignKey(
        FarmModel, on_delete=models.CASCADE, related_name=_('animal_witgth_farm')
    )
    type_animal = ChoiceField(
        choices=AnimalChoice, default=AnimalChoice.bovino, verbose_name=_('Tipo do Animal')
    )
    weigth = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, blank=False, verbose_name=_('Peso do animal')
    )

    earring_number = models.CharField(
        max_length=15, verbose_name=_('Número do brinco'), null=False, blank=False
    )
