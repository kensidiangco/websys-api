# Generated by Django 4.1.2 on 2022-10-12 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='message',
            field=models.CharField(max_length=500, verbose_name='message'),
        ),
    ]
