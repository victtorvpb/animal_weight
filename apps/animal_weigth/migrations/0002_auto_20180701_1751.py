# Generated by Django 2.0.6 on 2018-07-01 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animal_weigth', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farmmodel',
            name='cnpj',
            field=models.CharField(max_length=18, unique=True, verbose_name='CNPJ'),
        ),
    ]