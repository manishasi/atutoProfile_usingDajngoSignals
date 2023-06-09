# Generated by Django 4.1.6 on 2023-03-23 13:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='profile_pics')),
                ('father_name', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('mother_name', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('dob', models.DateField()),
                ('city', models.CharField(max_length=100)),
                ('place', models.CharField(max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
