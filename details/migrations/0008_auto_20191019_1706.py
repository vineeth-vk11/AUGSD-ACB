# Generated by Django 2.2.4 on 2019-10-19 11:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0007_auto_20191019_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='score',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
