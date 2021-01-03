#!/usr/local/bin/python3
# client id  : wwD854PF4mORCA
# secret     : pHNgc1vA2U6HzavgyLsGDcoHkUw
# twilio pw  : mypass
import praw
import os
from twilio.rest import Client

def reddit_setup():

    # Define reddit stuff
    reddit = praw.Reddit('switch_deals')
    subreddit = reddit.subreddit("nintendoswitchdeals")

    # Write String to be sent in loop

    text_string = "-------------------------------------\n"

    for new_post in subreddit.new(limit=4):

        text_string += "Title: " + str(new_post.title) + "\n"
        text_string += "Score: " + str(new_post.score)+ "\n"
        text_string += "URL: "   + str(new_post.url)+ "\n"
        text_string += "-------------------------------------\n"

    return text_string


def send_text(text_string):

    # Connect to Twilio rest client to send text
    accountSID ='ACec8067c1d7b13920c4271c410d882a00'
    authToken  ='5cb29f69bdadcc6007221dd9a250825f'
    twilioConn = Client(accountSID, authToken)

    # Define twilio cell number and my own number
    twilioCell = '+13342928393'
    myCell     = '+16172911113'
    twilioConn.messages.create(body=text_string, to=myCell, from_=twilioCell)

def main():

    text_string = reddit_setup()

    if len(text_string) == 0:
        print("No results returned")
    else:
        send_text(text_string)

main()
