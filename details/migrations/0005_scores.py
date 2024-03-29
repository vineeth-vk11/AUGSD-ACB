# Generated by Django 2.2.4 on 2019-10-19 11:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('details', '0004_auto_20191015_1024'),
    ]

    operations = [
        migrations.CreateModel(
            name='scores',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(default='NIL', max_length=30)),
                ('midsem_grade', models.CharField(default='NIL', max_length=15)),
                ('midsem_score', models.CharField(default='NIL', max_length=20)),
                ('attendance', models.CharField(default='NIL', max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
