# Generated by Django 4.2.3 on 2023-08-15 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0006_rename_url_product_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(null=True, upload_to='images/products'),
        ),
    ]
