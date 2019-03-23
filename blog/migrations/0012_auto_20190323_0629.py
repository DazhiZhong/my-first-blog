# Generated by Django 2.1 on 2019-03-23 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_payment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='body',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='assets/'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='payment',
            field=models.ImageField(blank=True, null=True, upload_to='assets/'),
        ),
    ]
