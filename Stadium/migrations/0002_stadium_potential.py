# Generated by Django 4.2.16 on 2024-09-22 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Stadium', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='stadium',
            name='potential',
            field=models.IntegerField(default=100),
        ),
    ]
