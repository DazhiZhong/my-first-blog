# Generated by Django 2.0.7 on 2019-03-12 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='breakfastho',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Picture', models.ImageField(upload_to='')),
                ('Description', models.TextField()),
                ('Price', models.DecimalField(decimal_places=4, max_digits=4)),
            ],
        ),
    ]
