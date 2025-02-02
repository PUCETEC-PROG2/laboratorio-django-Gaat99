# Generated by Django 4.2.16 on 2025-01-22 03:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('weight', models.FloatField(blank=True, null=True)),
                ('level', models.IntegerField(default=1)),
                ('birth', models.DateField(blank=True, null=True)),
                ('picture', models.ImageField(upload_to='trainers/')),
            ],
        ),
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('type', models.CharField(max_length=30)),
                ('weight', models.DecimalField(decimal_places=4, max_digits=6)),
                ('height', models.DecimalField(decimal_places=4, max_digits=6)),
                ('picture', models.ImageField(upload_to='pokemon_images')),
                ('trainer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pokedex.trainer')),
            ],
        ),
    ]
