# Generated by Django 4.2.6 on 2023-11-22 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dobrinapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='date',
            field=models.DateField(help_text='дата новости'),
        ),
    ]
