# Generated by Django 4.0.2 on 2022-08-16 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Films', '0004_alter_film_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='created_at',
            field=models.IntegerField(verbose_name='Год выпуска'),
        ),
    ]