# Generated by Django 3.0.2 on 2021-02-18 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bigbox', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='box',
            name='slug',
            field=models.CharField(blank=True, max_length=20, null=True, unique=True),
        ),
    ]
