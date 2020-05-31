# Generated by Django 3.0.6 on 2020-05-31 09:08

from django.db import migrations, models
import django.db.models.deletion
import main.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('slug', models.SlugField()),
            ],
            options={
                'verbose_name': 'city',
                'verbose_name_plural': 'cities',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='FoodType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('slug', models.SlugField()),
            ],
            options={
                'verbose_name': 'food_type',
                'verbose_name_plural': 'food_types',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='RestaurantType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('slug', models.SlugField()),
                ('city', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.City')),
            ],
            options={
                'verbose_name': 'rest_type',
                'verbose_name_plural': 'rest_types',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255)),
                ('slug', models.SlugField()),
                ('image', models.ImageField(blank=True, upload_to=main.models.rest_image_folder)),
                ('mini_description', models.CharField(default='', max_length=255)),
                ('address', models.CharField(default='', max_length=255)),
                ('open', models.BooleanField(default=True)),
                ('postal_code', models.CharField(default='', max_length=16)),
                ('open_time', models.TimeField()),
                ('close_time', models.TimeField()),
                ('city', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.City')),
                ('rest_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='restaurants', to='main.RestaurantType')),
            ],
            options={
                'verbose_name': 'restaurant',
                'verbose_name_plural': 'restaurants',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255)),
                ('slug', models.SlugField(unique=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('ingredients', models.TextField()),
                ('image', models.ImageField(blank=True, upload_to=main.models.food_image_folder)),
                ('food_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='foods', to='main.FoodType')),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='foods', to='main.Restaurant')),
            ],
            options={
                'verbose_name': 'food',
                'verbose_name_plural': 'foods',
                'ordering': ('name',),
            },
        ),
    ]
