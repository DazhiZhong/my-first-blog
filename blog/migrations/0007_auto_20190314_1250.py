# Generated by Django 2.0.7 on 2019-03-14 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20190314_0657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(null=True, upload_to='assets/'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='payment',
            field=models.ImageField(upload_to='assets/'),
        ),
    ]
