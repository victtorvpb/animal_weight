# Generated by Django 2.0.6 on 2018-07-01 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [('animal_weigth', '0002_auto_20180701_1751')]

    operations = [
        migrations.AddField(
            model_name='farmmodel',
            name='token',
            field=models.CharField(
                default='bbc9578987a6cb041e33c4ebb6635cdb25fbef32aed76652554a3e14387e',
                max_length=30,
                unique=True,
                verbose_name='CNPJ',
            ),
        )
    ]