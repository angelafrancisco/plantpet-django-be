# Generated by Django 4.0.3 on 2022-04-14 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plant_api', '0005_rename_room_name_plant_room_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plant',
            name='direction',
            field=models.CharField(choices=[('North', 'North'), ('South', 'South'), ('East', 'East'), ('West', 'West')], max_length=5),
        ),
    ]
