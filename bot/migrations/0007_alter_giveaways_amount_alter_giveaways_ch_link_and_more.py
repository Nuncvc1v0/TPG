# Generated by Django 4.2.7 on 2023-12-03 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0006_merge_20231203_1200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='giveaways',
            name='amount',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='giveaways',
            name='ch_link',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='giveaways',
            name='duration',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='language',
            name='text_settings',
            field=models.TextField(max_length=1500),
        ),
        migrations.AlterField(
            model_name='language',
            name='text_subscribe',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='language',
            name='text_timezone',
            field=models.TextField(max_length=1500),
        ),
        migrations.AlterField(
            model_name='language',
            name='text_timezone_changed',
            field=models.TextField(max_length=1500),
        ),
        migrations.AlterField(
            model_name='language',
            name='text_today',
            field=models.TextField(max_length=1500),
        ),
        migrations.AlterField(
            model_name='language',
            name='text_tomorrow',
            field=models.TextField(max_length=1500),
        ),
        migrations.AlterField(
            model_name='language',
            name='text_welcome',
            field=models.TextField(max_length=1500),
        ),
    ]
