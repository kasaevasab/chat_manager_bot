import telebot
from telebot import types
import keys
import random
import utils
import re

bot = telebot.TeleBot(keys.BOT_TOKEN)
username_to_user_id = utils.import_user_ids(keys.USER_IDS_FILE)


@bot.message_handler(commands=["start", "help"])
def send_info(message):
    bot.send_message(message.chat.id, utils.HELP_STRING)


@bot.message_handler(regexp="[b|B]aby flirt")
def flirt(message):
    try:
        if message.from_user.username not in username_to_user_id:
            with open(keys.USER_IDS_FILE, "a") as user_ids_file:
                username_to_user_id[message.from_user.username] = message.from_user.id
                user_ids_file.write(str(message.from_user.username) + ", " + str(message.from_user.id) + "\n")

        bot.send_message(message.chat.id, utils.flirting[random.randint(0, 2345678) % 7])
    except:
        bot.send_message(message.chat.id, utils.smths_wrong)


@bot.message_handler(regexp="[b|B]aby get angry")
def get_angry(message):
    try:
        if message.from_user.username not in username_to_user_id:
            with open(keys.USER_IDS_FILE, "a") as user_ids_file:
                username_to_user_id[message.from_user.username] = message.from_user.id
                user_ids_file.write(str(message.from_user.username) + ", " + str(message.from_user.id) + "\n")

        bot.send_message(message.chat.id, utils.angry[random.randint(0, 2345678) % 7])
    except:
        bot.send_message(message.chat.id, utils.smths_wrong)


@bot.message_handler(regexp="[b|B]aby motivate")
def motivate(message):
    try:
        if message.from_user.username not in username_to_user_id:
            with open(keys.USER_IDS_FILE, "a") as user_ids_file:
                username_to_user_id[message.from_user.username] = message.from_user.id
                user_ids_file.write(str(message.from_user.username) + ", " + str(message.from_user.id) + "\n")

        bot.send_message(message.chat.id, utils.motivational[random.randint(0, 2345678) % 7])
    except:
        bot.send_message(message.chat.id, utils.smths_wrong)


@bot.message_handler(regexp="^[b|B]aby ban @[A-Za-z0-9_]+")
def ban_chat_user(message):
    try:
        usernames_to_ban = re.findall("@[A-Za-z0-9_]+", message.text)
        for username in usernames_to_ban:
            if not utils.check_bot_knows_username(bot, message.chat.id, username, username_to_user_id):
                continue
            if bot.get_chat_member(message.chat.id, username_to_user_id[username[1:]]).status in ["administrator",
                                                                                                  "creator"]:
                bot.send_message(message.chat.id, utils.administrator_restrictions_message)
                continue
            bot.restrict_chat_member(message.chat.id, username_to_user_id[username[1:]],
                                     can_send_messages=False, can_invite_users=False)
    except:
        bot.send_message(message.chat.id, utils.smths_wrong)


@bot.message_handler(regexp="^[b|B]aby unban @[A-Za-z0-9_]+")
def unban_chat_user(message):
    try:
        usernames_to_unban = re.findall("@[A-Za-z0-9_]+", message.text)
        for username in usernames_to_unban:
            if not utils.check_bot_knows_username(bot, message.chat.id, username, username_to_user_id):
                continue
            bot.restrict_chat_member(message.chat.id, username_to_user_id[username[1:]],
                                     can_send_messages=True, can_send_media_messages=True, can_send_other_messages=True,
                                     can_invite_users=True)
    except:
        bot.send_message(message.chat.id, utils.smths_wrong)


@bot.message_handler(regexp="^[b|B]aby make admin @[A-Za-z0-9_]+")
def make_admin(message):
    try:
        usernames_to_make_admins = re.findall("@[A-Za-z0-9_]+", message.text)
        for username in usernames_to_make_admins:
            if not utils.check_bot_knows_username(bot, message.chat.id, username, username_to_user_id):
                continue
            bot.promote_chat_member(message.chat.id, username_to_user_id[username[1:]],
                                    can_manage_chat=True, can_restrict_members=True, can_promote_members=True,
                                    can_delete_messages=True, can_invite_users=True, can_change_info=True,
                                    can_pin_messages=True, can_manage_video_chats=True)
    except:
        bot.send_message(message.chat.id, utils.smths_wrong)


@bot.message_handler(regexp="[b|B]aby get chat statistics")
def get_chat_statistics(message):
    try:
        admins = bot.get_chat_administrators(message.chat.id)
        stats = "{members_num} members\n{admins_num} admins:\n".format(
            members_num=bot.get_chat_member_count(message.chat.id), admins_num=len(admins))
        for admin in admins:
            stats += "\t\t@{ad}\n".format(ad=admin.user.username)
        bot.send_message(message.chat.id, stats)
    except:
        bot.send_message(message.chat.id, utils.smths_wrong)


@bot.message_handler(regexp="[b|B]aby leave")
def self_liquidate(message):
    try:
        bot.send_message(message.chat.id, "I did get the hump with you, hypocrites"
                         )
        bot.leave_chat(message.chat.id)
    except:
        bot.send_message(message.chat.id, utils.smths_wrong)


bot.polling(none_stop=True, interval=0)
