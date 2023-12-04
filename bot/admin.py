# bot/admin.py
from django.contrib import admin
from .models import *

admin.site.register(BotSettings)
admin.site.register(UserProfile)
admin.site.register(language)
admin.site.register(Giveaways)
admin.site.register(folders)