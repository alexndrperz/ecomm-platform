# Generated by Django 4.2.3 on 2023-08-15 14:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Sellers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('comissionPercent', models.IntegerField(choices=[(5, 'Tercera Clase'), (15, 'Segunda Clase'), (25, 'Primera Clase')])),
            ],
        ),
        migrations.CreateModel(
            name='Transacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('quantity', models.IntegerField(default=1)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API.products')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API.sellers')),
            ],
        ),
        migrations.AddField(
            model_name='products',
            name='transact',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API.transacts'),
        ),
    ]
