# Generated by Django 3.1.4 on 2020-12-30 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artikulli', '0002_artikulli_kategoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artikulli',
            name='kategoria',
            field=models.CharField(blank=True, choices=[('Politike', 'Politike'), ('Ekonomi', 'Ekonomi'), ('Opinion', 'Opinion'), ('Sporti', 'Sporti'), ('Kulture', 'Kulture')], max_length=10),
        ),
    ]