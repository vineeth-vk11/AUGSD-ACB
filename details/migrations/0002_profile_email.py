# Generated by Django 2.2.4 on 2019-10-15 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.EmailField(default='NIL', max_length=255, unique=True, verbose_name='email address'),
        ),
    ]