# Generated by Django 4.2.7 on 2023-12-03 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0009_giveaways_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='language',
            name='text_folder',
            field=models.CharField(default='', max_length=1500),
        ),
        migrations.AlterField(
            model_name='giveaways',
            name='time',
            field=models.CharField(max_length=6, null=True),
        ),
    ]