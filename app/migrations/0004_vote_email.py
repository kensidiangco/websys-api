# Generated by Django 4.1.2 on 2022-10-12 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_review_down_votes_remove_review_up_votes_vote'),
    ]

    operations = [
        migrations.AddField(
            model_name='vote',
            name='email',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='email'),
        ),
    ]