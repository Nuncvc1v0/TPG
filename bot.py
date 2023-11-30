# bot/bot.py
import telebot
import sqlite3
from sqlite3 import *
from db import Database
from telebot import *
from django.conf import settings
from django.core.management.base import BaseCommand
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'telegram_bot_project.settings')
import django
django.setup()
from bot.models import *
from db import Database
# Initialize the Django settings in the bot script
if not settings.configured:
    settings.configure()

# Set up the Telegram bot
bot_settings = BotSettings.objects.first()
if not bot_settings:
    print("Bruh")
    # raise ValueError("Bot settings not found in the database. Add them via the Django admin panel.")

db = Database('db.sqlite3')

TOKEN = "6868802431:AAHXbjWXQpq76_9lQw67t-XkkxYQaNx1-qI"
bot = telebot.TeleBot(TOKEN)

# Define a command to handle '/start' command
@bot.message_handler(commands=['start'])
def handle_start(message):
    global user_id
    global username
    user_id = message.from_user.id
    username = message.from_user.username
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name

    # Save user information to the database
    UserProfile.objects.get_or_create(
        user_id=user_id,
        defaults={
            'username': username,
            'first_name': first_name,
            'last_name': last_name,
            'language': 'ru',
            'user_UTC': "1",
            "notification": True
        }
    )
    keylan = types.InlineKeyboardMarkup()
    
    it1 = types.InlineKeyboardButton(text="ru", callback_data="ru")
    it2 = types.InlineKeyboardButton(text="en", callback_data="en")
    it3 = types.InlineKeyboardButton(text="ua", callback_data="ua")

    keylan.add(it1, it2, it3)

    bot.send_message(message.chat.id, "Выберите язык!", reply_markup=keylan)

# Command to echo back the user's message
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:
        
        if call.data == "ru":
            db.lang_ru(user_id)
            bot.edit_message_text('russian', call.message.chat.id, call.message.message_id)
        
        if call.data == "en":
            db.lang_en(user_id)
            bot.edit_message_text("english", call.message.chat.id, call.message.message_id)
        
        if call.data == "ua":
            db.lang_ua(user_id)
            bot.edit_message_text("ukraine", call.message.chat.id, call.message.message_id)

# Polling loop
bot.polling(none_stop=True)
