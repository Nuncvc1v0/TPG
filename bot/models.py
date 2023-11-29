# bot/models.py
from django.db import models

class BotSettings(models.Model):
    token = models.CharField(max_length=255)
    chat_id = models.CharField(max_length=255)

    def __str__(self):
        return f'Bot Settings'

class UserProfile(models.Model):
    user_id = models.IntegerField(unique=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    language = models.CharField(max_length=255)
    UTC = models.CharField(max_length=255)
    notification = models.IntegerField(max_length=255)


    def __str__(self):
        return f'{self.first_name} {self.last_name}'