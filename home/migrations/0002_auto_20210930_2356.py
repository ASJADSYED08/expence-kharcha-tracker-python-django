# Generated by Django 3.2.4 on 2021-09-30 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='expenses',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='balance',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
