# Generated by Django 4.2.7 on 2023-12-03 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0011_alter_language_language_code_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='language',
            name='text_language',
            field=models.CharField(max_length=1500, null=True),
        ),
        migrations.AddField(
            model_name='language',
            name='text_language_changed',
            field=models.CharField(max_length=1500, null=True),
        ),
    ]
