# Generated by Django 4.0.2 on 2022-08-16 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Films', '0002_film_file_film_rating'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='film',
            options={'verbose_name': 'Фильм', 'verbose_name_plural': 'Фильмы'},
        ),
        migrations.AlterField(
            model_name='film',
            name='duration',
            field=models.DurationField(verbose_name='Продолжительность фильма'),
        ),
    ]