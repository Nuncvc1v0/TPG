import telebot
import sqlite3
from sqlite3 import *
from db import Database
from telebot import *
from django.conf import settings
from django.core.management.base import BaseCommand
import os
import datetime
from datetime import date, timedelta
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'telegram_bot_project.settings')
import django
django.setup()
from bot.models import *
from db import Database


if not settings.configured:
    settings.configure()

bot_settings = BotSettings.objects.first()
if not bot_settings:
    print("The bot's running")

db = Database('db.sqlite3')
current_date = datetime.datetime.now().strftime('%d.%m.%Y')
today = datetime.datetime.today()
next = today+datetime.timedelta(days=1)
next_date = next.strftime('%d.%m.%Y')


TOKEN = "6589318330:AAFaMkqguJKcIpLGBusT5iQZygp1Q2gzAMs"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def handle_start(message):
    global user_id
    global username
    global first_name
    user_id = message.from_user.id
    username = message.from_user.username
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name

    user_profile = UserProfile.objects.filter(user_id=user_id).first()

    if user_profile is None:
        user_profile, created = UserProfile.objects.get_or_create(
            user_id=user_id,
            defaults={
                'username': username,
                'first_name': first_name,
                'last_name': last_name,
                'language': 'Русский',
                'user_UTC': "1",
                "notification": True
            }
        )

        keylan = types.InlineKeyboardMarkup()
        it1 = types.InlineKeyboardButton(text="Русский", callback_data="ru")
        it2 = types.InlineKeyboardButton(text="English", callback_data="en")
        it3 = types.InlineKeyboardButton(text="Українська", callback_data="ua")
        keylan.add(it1, it2, it3)

        bot.send_message(message.chat.id, "Выберите язык:\nSelect language:\nОберіть мову:", reply_markup=keylan)
        
    else:
        language_entry = language.objects.filter(language_code=user_profile.language).first()

        if language_entry:
            # Use only the first name in the welcome message
            welcome_message = language_entry.text_welcome.format(username=first_name)
            tod = language_entry.button_menu_text_today
            tom = language_entry.button_menu_text_tomorrow
            sett = language_entry.button_menu_text_settings
            faq = language_entry.button_menu_text_FAQHelp
            # Replace \n with actual line breaks
            welcome_message = welcome_message.replace('\\n', '\n')

            # Send the welcome message
            menu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            b_tod = types.KeyboardButton(tod)
            b_tom = types.KeyboardButton(tom)
            b_sett = types.KeyboardButton(sett)
            b_faq = types.KeyboardButton(faq)

            menu.add(b_tod, b_tom, b_sett, b_faq)
            
            bot.send_message(message.chat.id, welcome_message, reply_markup=menu)
            
        else:
            bot.send_message(message.chat.id, 'Unsupported language')

@bot.message_handler(commands=['Tomorrow'])
def handle_start(message):
    user_id = message.from_user.id
    # Retrieve user language from the database
    user_profile = UserProfile.objects.get(user_id=user_id)
    language_code = user_profile.language

    # Retrieve language entry from the 'languages' table
    giveaway = Giveaways.objects.filter(date=next_date)
    language_entry = language.objects.filter(language_code=language_code).first()
    fold = folders.objects.filter(date_f=next_date).first()
    
    if language_entry:
        if giveaway:
            text_tomorrow = language_entry.text_tomorrow.format(
                day=next_date,
                all_day_subscribe=db.g_sum_t(next_date),
                Giceaway_list=db.g_link_t(next_date),
            )
            text_folder = language_entry.text_folder

            url = fold.link_f

            folder = types.InlineKeyboardMarkup()
            f1 = types.InlineKeyboardButton(text=text_folder, url=url)
            folder.add(f1)

            text_tomorrow = text_tomorrow.replace('\\n', '\n')
            bot.send_message(message.chat.id, text_tomorrow, reply_markup=folder)
    else:
        bot.send_message(message.chat.id, 'Unsupported language')

@bot.message_handler(content_types=['text', 'photo'])
def lala(message):      
    if message.chat.type == 'private':
        user_id = message.from_user.id
        user_profile = UserProfile.objects.get(user_id=user_id)
        language_code = user_profile.language
        language_entry = language.objects.filter(language_code=language_code).first()
        if language_entry:
            if message.text == language_entry.button_menu_text_today:
                user_id = message.from_user.id

                # Retrieve language entry from the 'languages' table
                giveaway = Giveaways.objects.filter(date=current_date)
                fold = folders.objects.filter(date_f=current_date).first()

                if giveaway:
                    text_today = language_entry.text_today.format(
                        day=current_date,
                        all_day_subscribe=db.g_sum(current_date),
                        Giceaway_list=db.g_link(current_date),
                    )
                    text_folder = language_entry.text_folder
                    url = fold.link_f

                    folder = types.InlineKeyboardMarkup()
                    f1 = types.InlineKeyboardButton(text=text_folder, url=url)
                    folder.add(f1)

                    text_today = text_today.replace('\\n', '\n')
                    bot.send_message(message.chat.id, text_today, reply_markup=folder)
   
            if message.text == language_entry.button_menu_text_tomorrow:           
                # Retrieve language entry from the 'languages' table
                giveaway = Giveaways.objects.filter(date=next_date)
                fold = folders.objects.filter(date_f=next_date).first()
                if giveaway:
                    text_tomorrow = language_entry.text_tomorrow.format(
                        day=next_date,
                        all_day_subscribe=db.g_sum_t(next_date),
                        Giceaway_list=db.g_link_t(next_date),
                    )
                    text_folder = language_entry.text_folder

                    url = fold.link_f

                    folder = types.InlineKeyboardMarkup()
                    f1 = types.InlineKeyboardButton(text=text_folder, url=url)
                    folder.add(f1)

                    text_tomorrow = text_tomorrow.replace('\\n', '\n')
                    bot.send_message(message.chat.id, text_tomorrow, reply_markup=folder)
            
            elif message.text == language_entry.button_menu_text_FAQHelp:
                # получаю текст из бд
                text_faq = language_entry.text_FAQHelp
                text_faq = text_faq.replace('\\n', '\n')
                bot.send_message(message.chat.id, text_faq)
            elif message.text == language_entry.button_menu_text_settings:
                text_settings = language_entry.text_settings.format(
                    user_language=language_code)
                text_settings = text_settings.replace('\\n', '\n')
                lan=language_entry.text_language
                
                lang_ch = types.ReplyKeyboardMarkup(resize_keyboard=True)
                it1 = types.KeyboardButton(lan)
                lang_ch.add(it1)
                bot.send_message(message.chat.id, text_settings, reply_markup=lang_ch)
            elif message.text == language_entry.text_language:

                keylan = types.InlineKeyboardMarkup()
                it1 = types.InlineKeyboardButton(text="Русский", callback_data="ru")
                it2 = types.InlineKeyboardButton(text="English", callback_data="en")
                it3 = types.InlineKeyboardButton(text="Українська", callback_data="ua")
                keylan.add(it1, it2, it3)

                bot.send_message(message.chat.id, "Выберите язык:\nSelect language:\nОберіть мову:", reply_markup=keylan)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:
        # user_id = call.message.from_user.id
        def menu():
            bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
            user_profile = UserProfile.objects.filter(user_id=user_id).first()
            language_entry = language.objects.filter(language_code=user_profile.language).first()
            # Use only the first name in the welcome message
            welcome_message = language_entry.text_welcome.format(username=first_name)
            tod = language_entry.button_menu_text_today
            tom = language_entry.button_menu_text_tomorrow
            sett = language_entry.button_menu_text_settings
            faq = language_entry.button_menu_text_FAQHelp
            # Replace \n with actual line breaks
            welcome_message = welcome_message.replace('\\n', '\n')

            # Send the welcome message
            menu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            b_tod = types.KeyboardButton(tod)
            b_tom = types.KeyboardButton(tom)
            b_sett = types.KeyboardButton(sett)
            b_faq = types.KeyboardButton(faq)

            menu.add(b_tod, b_tom, b_sett, b_faq)
            bot.send_message(call.message.chat.id, welcome_message, reply_markup=menu)
        if call.data == "ru":
            db.lang_ru(user_id)
            menu()
        elif call.data == "en":
            db.lang_en(user_id)
            menu()
        elif call.data == "ua":
            db.lang_ua(user_id)
            menu()

# Polling loop
bot.polling(none_stop=True)
