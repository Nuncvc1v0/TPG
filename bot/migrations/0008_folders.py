# Generated by Django 4.2.7 on 2023-12-03 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0007_alter_giveaways_amount_alter_giveaways_ch_link_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='folders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_f', models.CharField(max_length=255)),
                ('link_f', models.CharField(max_length=255)),
            ],
        ),
    ]
