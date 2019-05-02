# Discord Twitter Follows test
This python program uses the tweepy and discord.py modules

In Discord a user can enter their twitter name to test if they follow a list of twitter names determined by discord channel admin.

Features:
- A discord channel can specified in the code, and will be checked by a bot
    Once a message is entered on this channel it will be tested to see if this message follows a list of twitter names
- A list of twitter names is currently hardcoded
    TODO: Change the twitter names so that they can be read from a private channel on discord
- The resultes are output as: followOnTwitter.csv
    TODO: - Remove the header for each line
          - Write an insert function to insert into a database
