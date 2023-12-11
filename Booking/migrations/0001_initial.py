# Generated by Django 4.2.5 on 2023-09-15 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('director', models.CharField(max_length=50)),
                ('discription', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, null=True, upload_to='mymovies/cover')),
            ],
        ),
    ]
