# Generated by Django 4.2.3 on 2023-08-15 15:25

import API.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0003_transact_comisionchecker_transact_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='url',
            field=models.CharField(default=API.models.Product.generate_token_internal, max_length=50),
        ),
        migrations.AddField(
            model_name='seller',
            name='token',
            field=models.CharField(default=API.models.Seller.generate_token_internal, max_length=50),
        ),
    ]
