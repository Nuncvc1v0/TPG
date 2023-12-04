# bot/models.py
from django.db import models

class BotSettings(models.Model):
    token = models.CharField(max_length=255)
    chat_id = models.CharField(max_length=255)

    def __str__(self):
        return f'Bot Settings'

class UserProfile(models.Model):
    user_id = models.IntegerField(unique=True, null=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    first_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    language = models.CharField(max_length=255, null=True)
    user_UTC = models.CharField(max_length=255, null=False)
    notification = models.BooleanField()


    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class language(models.Model):
    language_code = models.CharField(max_length=127)
    text_welcome = models.TextField(max_length=1500)
    text_timezone = models.TextField(max_length=1500)
    text_timezone_changed = models.TextField(max_length=1500)
    text_language = models.CharField(max_length=1500, null=True)
    text_language_changed = models.CharField(max_length=1500, null=True)
    text_today = models.TextField(max_length=1500)
    text_tomorrow = models.TextField(max_length=1500)
    text_folder = models.CharField(max_length=1500, default ='')
    text_settings = models.TextField(max_length=1500)
    text_FAQHelp = models.TextField(max_length=1500)
    button_menu_text_today = models.CharField(max_length=1500)
    button_menu_text_tomorrow = models.CharField(max_length=1500)
    button_menu_text_settings = models.CharField(max_length=1500)
    button_menu_text_FAQHelp = models.CharField(max_length=1500)
    text_subscribe = models.BooleanField()

    def __str__(self):
        return f'Language'

class Giveaways(models.Model):
    ch_link = models.CharField(max_length=255, null=True)
    amount = models.IntegerField()
    date = models.CharField(max_length=255)
    duration = models.IntegerField()
    time = models.CharField(max_length=6, null=True, default='')
    
    def __str__(self):
        return f'{self.ch_link}'

class folders(models.Model):
    date_f = models.CharField(max_length=255)
    link_f = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.date_f}'
