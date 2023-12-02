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
    print("The bot's running")
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
    # log_file_path = 'log.txt'
    # with open(log_file_path, 'a') as log_file:
    #     if username is not None:
    #         log_message = '-- id' + str(user_id) + '   @' + username + '   ' + 'wrote the start command\n'
    #     else:
    #         log_message = '-- id' + str(user_id) + '   ' + 'Unknown Username   ' + 'wrote the start command\n'

    #     log_file.write(log_message)
    keylan = types.InlineKeyboardMarkup()
    
    it1 = types.InlineKeyboardButton(text="ru", callback_data="ru")
    it2 = types.InlineKeyboardButton(text="en", callback_data="en")
    it3 = types.InlineKeyboardButton(text="ua", callback_data="ua")

    keylan.add(it1, it2, it3)

    bot.send_message(message.chat.id, "Выберите язык!", reply_markup=keylan)

# Command to handle '/test' command
@bot.message_handler(commands=['test'])
def handle_test(message):
    user_id = message.from_user.id

    # Retrieve user language from the database
    user_profile = UserProfile.objects.get(user_id=user_id)
    language = user_profile.language

    # Prepare a dictionary with test messages for each language
    test_messages = {
        'ru': 'Тест на русском',
        'en': 'Test in English',
        'ua': 'Тест на українській'
    }

    # Send the appropriate test message based on the user's language
    bot.send_message(message.chat.id, test_messages.get(language, 'Unsupported language'))

# Command to handle '/testL' command
@bot.message_handler(commands=['testL'])
def handle_testL(message):
    user_id = message.from_user.id

    # Retrieve user language from the database
    user_profile = UserProfile.objects.get(user_id=user_id)
    language_code = user_profile.language

    # Retrieve language entry from the 'languages' table
    language_entry = language.objects.filter(language_code=language_code).first()

    if language_entry:
        # Replace {day}, {all_day_subscribe}, and {Giceaway_list} with specific values
        text_today = language_entry.text_today.format(
            day="4.12.2023",
            all_day_subscribe=15000,
            Giceaway_list="https://t.me/wewantyoutodothejob/36"
        )

        # Replace \n with actual line breaks
        text_today = text_today.replace('\\n', '\n')

        # Send the language names as a message
        bot.send_message(message.chat.id, text_today)

    else:
        bot.send_message(message.chat.id, 'Unsupported language')


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
