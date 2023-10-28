# Generated by Django 4.2.6 on 2023-10-28 09:14

from django.db import migrations, models
import events.models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='code',
            field=models.CharField(default=events.models.generate_pin, max_length=6, unique=True),
        ),
    ]