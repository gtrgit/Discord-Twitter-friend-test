import discord
import csv
from tweepy import OAuthHandler
from tweepy import API
import twitterCredentialsPrivate as tc

#twitter section --------------

#get twitter OAuth data
consumer_key = tc.consumer_key
consumer_secret = tc.consumer_secret
# Consumer key authentication
auth = OAuthHandler(consumer_key, consumer_secret)
access_token = tc.access_token
access_token_secret = tc.access_token_secret
# Access key authentication
auth.set_access_token(access_token, access_token_secret)

# Set up the API with the authentication handler
api = API(auth)

#twitter test friends
def are_friends(source,target):
    """
    Tests if the source follows the target on twitter
    :param source: users twitter name
    :param target: the twitter name that is tested if the user follows
    :return: followTest 'a dictionary with followTest data'
    """
    status = api.show_friendship(source_screen_name=source,target_screen_name=target)
    f1_following = status[0].following
    followTest = {'twitterName':source,'testType':'follows','targetName':target,'follows':f1_following}
    return followTest

#end twitter section


#Discord section ------------
def read_token():
    """
    read discord bot token
    :return:
    """
    with open("tokenPrivate.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()

token = read_token()
client = discord.Client()
# enter the name of the channel the bot will check below
channel = ["twitter_name"]

# enter the twitter name into the below list that are to be tested
twitterList = ['cryptoStacker', 'Apple']

# todo find out how to not include the header for each entry
def writeFollowers(followers):
    """
    Append the output of the returned data to csv file followsOnTwitter.csv
    :param followers:
    :return:
    """
    with open('followsOnTwitter.csv', mode='a') as csv_file:
        fieldnames = ['twitterName', 'testType', 'targetName', 'follows', 'discordName']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow(followers)

@client.event
async def on_message(message):
    """
    in discord check that messages are coming from channel twitter_name and tests message for follows
    :param message:
    :return:
    """
    if str(message.channel) in channel:
        for i in twitterList:
            followers = are_friends(message.content, i)
            followers['discordName'] = message.author.name
            print(followers)
            writeFollowers(followers)

client.run(token)

#end Discord section

