# bot/bot.py
import telebot
from django.conf import settings
from django.core.management.base import BaseCommand
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'telegram_bot_project.settings')
import django
django.setup()
from bot.models import *

# Initialize the Django settings in the bot script
if not settings.configured:
    settings.configure()

# Set up the Telegram bot
bot_settings = BotSettings.objects.first()
if not bot_settings:
    print("Bruh")
    # raise ValueError("Bot settings not found in the database. Add them via the Django admin panel.")

TOKEN = "6868802431:AAHXbjWXQpq76_9lQw67t-XkkxYQaNx1-qI"
bot = telebot.TeleBot(TOKEN)

# Define a command to handle '/start' command
@bot.message_handler(commands=['start'])
def handle_start(message):
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
        }
    )

    bot.send_message(message.chat.id, f"Hello! I am your echo bot. Type /echo to test.")

# Command to echo back the user's message
@bot.message_handler(commands=['echo'])
def handle_echo(message):
    bot.send_message(message.chat.id, message.text)

# Polling loop
bot.polling(none_stop=True)
