# Generated by Django 4.2.1 on 2023-05-13 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='product_price',
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='', upload_to='home/images'),
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.CharField(default=0, max_length=50),
        ),
    ]
