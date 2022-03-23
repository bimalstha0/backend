# Generated by Django 4.0.1 on 2022-03-18 10:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_remove_product_unit'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('scName', models.CharField(max_length=100)),
                ('temp', models.CharField(max_length=100)),
                ('water', models.CharField(max_length=100)),
                ('soilType', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='')),
                ('category', models.CharField(choices=[('Fruits', 'Fruits'), ('Vegetables', 'Vegetables'), ('Food Crops', 'Food Crops'), ('Cash Crops', 'Cash Crops')], max_length=100)),
                ('fert', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.product')),
            ],
        ),
    ]
