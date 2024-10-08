# Generated by Django 4.2.16 on 2024-09-21 23:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Stadium', '0001_initial'),
        ('match', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buy_date', models.DateTimeField(auto_now_add=True)),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='match.match')),
                ('seat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Stadium.seat')),
            ],
        ),
    ]
