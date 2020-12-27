# Generated by Django 3.1.4 on 2020-12-27 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='artikulli',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=25)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('data', models.DateField(auto_now_add=True)),
                ('image', models.ImageField(blank=True, upload_to='artikulli/images/')),
            ],
        ),
    ]
