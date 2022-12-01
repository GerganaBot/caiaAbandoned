# Generated by Django 4.1.3 on 2022-12-01 19:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Locations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(choices=[('Center', 'Sofia Center'), ('Neighbourhood', 'Sofia Neighbourhood'), ('Municipality', 'Sofia Municipality')], max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Houses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('house_photo', models.URLField()),
                ('street', models.CharField(max_length=50)),
                ('street_number', models.PositiveIntegerField()),
                ('description', models.TextField(blank=True, max_length=300, null=True)),
                ('slug', models.SlugField(unique=True)),
                ('house_location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='houses.locations')),
            ],
        ),
    ]
