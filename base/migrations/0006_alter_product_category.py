# Generated by Django 4.0.1 on 2022-03-18 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_alter_order_payment_method_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Seeds', 'Seeds'), ('Fertilizers', 'Fertilizers'), ('Groceries', 'Groceries'), ('Traditional Tools', 'Traditional Tools'), ('Modern Tools', 'Modern Tools')], max_length=100),
        ),
    ]
