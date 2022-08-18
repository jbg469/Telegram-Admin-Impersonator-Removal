#! /usr/bin/env python3
import telebot
import telegram
import time
import mysql.connector

bot=telebot.TeleBot("5477766789:AAG-aby_N6VU9eiPgPzoQx4AfKIkWFL_xXg")

@bot.message_handler(content_types=[
    "new_chat_members"
])

#@MWT(timeout=60*60)
def NoImpostors(message):
    fname=message.new_chat_members[0].first_name
    lname=message.new_chat_members[0].last_name
    userid=message.new_chat_members[0].id
    chatid=message.chat.id
    global full
    try:
        if fname is not None and lname is not None:
            full=fname+" "+lname
            print(full)
        elif fname is not None and lname is None:
            full=fname
            print(full)
        elif fname is None and lname is not None:
            full=lname
            print(full)
        for j in bot.get_chat_administrators(message.chat.id):
            if j.user.first_name is not None and j.user.last_name is not None:
                if (j.user.first_name + " " + j.user.last_name)==full:
                    bot.ban_chat_member(chat_id=chatid, user_id=userid)
            elif j.user.first_name is not None and j.user.last_name is None:
                if(j.user.first_name)==full:
                    bot.ban_chat_member(chat_id=chatid, user_id=userid)
            elif j.user.first_name is None and j.user.last_name is not None:
                if(j.user.last_name)==full:
                    bot.ban_chat_member(chat_id=chatid, user_id=userid)
            #if (full.find(j.user.first_name)!= -1) or (full.find(j.user.last_name)!= -1) :
                #bot.ban_chat_member(chat_id=chatid, user_id=userid)
    except:
        pass
bot.polling()
