# Generated by Django 2.0.1 on 2018-01-16 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('businesses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]