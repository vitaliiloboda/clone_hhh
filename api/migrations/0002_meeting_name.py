# Generated by Django 4.1 on 2022-09-07 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='meeting',
            name='name',
            field=models.CharField(default='random_meeting', max_length=200, verbose_name='meeting name'),
        ),
    ]