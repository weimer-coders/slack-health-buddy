from slackclient import SlackClient
from tips import TIPS
import random
import os

#config variables from Heroku
TOKEN = os.environ.get('TOKEN')

slack = SlackClient(TOKEN)
#name of the token must be all caps for Heroku


def post_tip(tips):
    rand_item = random.choice(tips)
    #tips is a list of dictionaries, not a string. if you put a string in parenthesis the random number generator will pick a random letter. random takes anything that is iterable
    log = slack.api_call(
        "chat.postMessage",
        channel = "G9DDB0FNZ",
        text = rand_item["message"]
        #rand_item is the dictionary, "message" is the key
        #before posting, you must go into the slack api settings and ask for permission to post into groups
    )

    print(log)
    #note - make sure to use python 3 printing style


def run_app():
    post_tip(TIPS)

if __name__ == '__main__':
    post_tip(TIPS)
