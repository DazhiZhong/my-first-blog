# Generated by Django 2.0.7 on 2019-03-11 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='dosomething',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('shit', models.TextField()),
                ('ass', models.TextField()),
            ],
        ),
    ]
