# Generated by Django 5.0.6 on 2024-07-05 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0007_alter_product_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.CharField(max_length=50),
        ),
    ]
