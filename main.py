import os

import telebot
import pandas as pd
import random

excels = pd.ExcelFile('sample.xlsx')

df1 = pd.read_excel(excels, 'Sheet1')
df2 = pd.read_excel(excels, 'Sheet2')
df3 = pd.read_excel(excels, 'Sheet3')


bot = telebot.TeleBot('telegram bot token')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Available Commands \n/1 - get random numbers \n /2 - get random fruit \n /3 - get random greeting")
@bot.message_handler(commands=['1','2','3'])
def excel1(message):
    if message.text == '/1':
        bot.reply_to(message, df1['text'][random.choice(list(df1.index))])
    elif message.text == '/2':
        bot.reply_to(message, df2['text'][random.choice(list(df2.index))])
    elif message.text == '/3':
        bot.reply_to(message, df3['text'][random.choice(list(df3.index))])

print('polling...')

bot.infinity_polling()