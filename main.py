# Slash-Friends Assistant bot
# Coded by / Zanyar (slashzanyar)
# Licensed on ELUA

# Importing General Modules 
from telebot import *

# Add extensions
import messages
from randomizer import MR_start, MR_restart, MR_damage, MR_add_damage, MR_no_fosh

# Genral Variabels
API_TOKEN = 'Doooooooooooooooooooooooooooooooooot :)'
bot = telebot.TeleBot(API_TOKEN)

# Other Variables
hm = messages.help_message
dlhm = messages.dlh_message
sm = messages.start_messages
rsm = messages.restart_messages
adm = messages.add_damage_messages
dm = messages.damage_messages

cm = messages.codekesh_message
cnm = messages.code_nagoo_message
fm = messages.fosh_massages
nfm = messages.no_fosh_messages

# Bot Commands  
@bot.message_handler(commands=['start'])
def start_bot(message):
    bot.reply_to(message, MR_start(sm), parse_mode='HTML')

@bot.message_handler(commands=['restart'])
def restart_bot(message):
    bot.reply_to(message, MR_restart(rsm), parse_mode='HTML')

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, hm, parse_mode='HTML')

@bot.message_handler(commands=['damage'])
def add_damage(message):
    bot.reply_to(message, MR_add_damage(adm), parse_mode='HTML')

@bot.message_handler(commands=['dlh'])
def send_damage_league_help(message):
    bot.reply_to(message, dlhm, parse_mode='HTML')

# Bot Other Works
@bot.message_handler(func=lambda message: True)
def scan_messages(message):
    users_message = message.text
    fm = messages.fosh_massages
    if "#دمیج" in users_message:
        bot.reply_to(message, MR_damage(dm), parse_mode='HTML')
    elif "کصکش" in users_message:
        bot.delete_message(users_message)
        bot.reply_to(message, cm, parse_mode='HTML')
    elif "کص نگو" in users_message:
        bot.delete_message
        bot.reply_to(message, cnm, parse_mode='HTML')
    elif users_message in fm:
        bot.delete_message(users_message)
        bot.reply_to(message, MR_no_fosh(nfm), parse_mode='HTML')

# Start Bot Work
bot.infinity_polling()
