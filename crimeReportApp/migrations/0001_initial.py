# Generated by Django 5.1.2 on 2024-10-24 17:22

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CrimeReports',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(blank=True, max_length=30)),
                ('email_address', models.CharField(blank=True, max_length=60)),
                ('crime_type', models.CharField(blank=True, max_length=60)),
                ('location', models.CharField(blank=True, max_length=60)),
                ('description', models.TextField(blank=True, max_length=225)),
                ('evidence', models.FileField(upload_to='evidence/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
