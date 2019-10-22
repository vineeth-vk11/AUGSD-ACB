# Generated by Django 2.2.4 on 2019-10-21 09:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('details', '0009_auto_20191019_1708'),
    ]

    operations = [
        migrations.CreateModel(
            name='attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(default='NIL', max_length=20)),
                ('classes', models.CharField(default='NIL', max_length=20)),
                ('attended', models.CharField(default='NIL', max_length=20)),
                ('percentage', models.CharField(default='NIL', max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attendance', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
