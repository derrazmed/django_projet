# Generated by Django 5.0.4 on 2024-05-31 10:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_profile_email'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]