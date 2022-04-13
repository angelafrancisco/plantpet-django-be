# Generated by Django 4.0.3 on 2022-04-12 21:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('plant_api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateField(auto_now_add=True)),
                ('health', models.CharField(choices=[('Poor', 'Poor'), ('Good', 'Good'), ('Excellent', 'Excellent')], max_length=9)),
                ('notes', models.CharField(max_length=30)),
                ('plant', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='plant_api.plant')),
            ],
        ),
    ]
