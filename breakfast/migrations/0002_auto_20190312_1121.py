# Generated by Django 2.0.7 on 2019-03-12 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('breakfast', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='breakfastho',
            name='Price',
            field=models.DecimalField(decimal_places=2, max_digits=4),
        ),
    ]
