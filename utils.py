administrator_restrictions_message = "Sorry, this user is too cool to ban " \
                                     "and you just simple-dimple"

smths_wrong = "Smth has gone wrong, please make sure Baby Bot has admins rights and try again"

HELP_STRING = "Hi there! Baby Bot mother on the phone!\n\n" \
              "Baby Bot will be a fair member of your chat and can help you manage the group.\n\n" \
              "When adding the bot to your group give it admins rights so that it worked as it is supposed to.\n" \
              "Make sure that all of the chat members started interacting with baby bot: " \
              "everyone should make the bot flirt (see the instruction below).\n\n" \
              "What can you do using Baby Bot?\n\n" \
              "If you want your baby bot to flirt, send the following message\n" \
              "\t- baby flirt\n\n" \
              "If you want your baby bot to get angry, send the following message\n" \
              "\t- baby get angry\n\n" \
              "If you want your baby bot to motivate you, send the following message\n" \
              "\t- baby motivate\n\n" \
              "To ban or unban the users send the following messages\n" \
              "\t- baby ban @user1 @user2 ...\n" \
              "\t- baby unban @user1 @user2 ...\n\n" \
              "To give someone admins rights send the following message\n" \
              "\t- baby make admin @user1 @user2 ...\n\n" \
              "To get chat statistics send the following message\n" \
              "\t- baby give chat statistics\n\n" \
              "If you want baby bot to self-liquidate, send the following message\n" \
              "\t- baby leave\n"

flirting = ['Hey, babe, you look so sexy', 'Hey, babe, you are damn gorgeous', 'Hey, babe, you are my queen',
            'Hey, babe, you wanna have some fun?', 'Hey, babe, you make me smile',
            'Hey, babe, you are my type', 'Hey, babe, you make this world special', 'Hey, babe, you wanna hang out?']
angry = ['You are a piece of shit!', 'You are damned', 'You piss me of!', 'You annoy me', 'You may go to hell!',
         'You are utterly not my type!', 'You make me desperate!', 'You wanna hang out? Find another baby, BEBEBEBE']
motivational = ['Old ways don\'t open new doors', 'Work bitch', 'Be a warrior, not a worrier',
                'One day or day one. You decide.', 'Life is a journey, not a race',
                'Go wild for a while', 'Mindset is everything',
                'Just because it is taking time doesn\'t mean it is not happening']


def import_user_ids(filename):
    username_user_id = {}
    with open(filename) as file:
        lines = file.readlines()
    for s in lines:
        s = s.strip()
        username, user_id = s.split(", ")
        username_user_id[username] = user_id
    return username_user_id


def import_flirt_patterns(filename):
    with open(filename) as file:
        flirt_patterns = [s.strip() for s in file.readlines()]
    return flirt_patterns


def check_bot_knows_username(bot, id, username, username_to_user_id):
    if username[1:] not in username_to_user_id:
        bot.send_message(id, "Sorry, I don't know this user " + username)
        return False
    return True
