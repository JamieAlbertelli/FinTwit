#Import Statements
import tweepy
import csv
import sys

from pathlib import Path

#Twitter API keys and tokens
consumer_key = ' "ENTER YOU PUBLIC CONSUMER KEY" '
consumer_secret = ' "ENTER YOU PRIVATE CONSUMER KEY" '

access_token = ' "ENTER YOUR PUBLIC ACCESS TOKEN" '
access_token_secret = ' "ENTER YOUR PRIVATE ACCESS TOKEN" '

#Authentication 
auth = tweepy.auth.OAuthHandler(consumer_key ,consumer_secret)
auth.set_access_token(access_token, access_token_secret)

#Stores Authentication and waits on Twitter's rate limit
api = tweepy.API(auth, wait_on_rate_limit = True)

"""
Above is completed.
Below is tasks to complete.
"""
def printInstruction():
    print("Steps for the program to function are as follows")
    print("Enter name of chosen stock or search term")
    print("Enter name of the chosen stock")
    print("Enter choice of filter words")
    print("Enter start and end dates of search, they must be no longer than two weeks apart.")


"""
Can probably be deleted will keep until tested without and everything is functional.

#Writes data from function to chosen file
csvFile = open('data/google.csv', 'a')
csvWriter = csv.writer(csvFile)
"""

#Writes data from function to chosen file
def sortDirectory():
    p = Path("../FinTwit/data")
    p.mkdir(parents = True, exist_ok = True)
    tempname = input("Enter your chosen file: ")
    filename = (tempname + '.csv')
    filepath = p / filename
    with filepath.open("w", encoding = "utf-8") as f:
        f.write(filename)

"""
#Extracts Tweet data
def tweetExtractor():
    searchTerm = input("Input your desired search term: ")
    filterTerm = input("Input your filter words, begin terms with a '-' and seperate with a space. NB ommits retweets by default: ")
    sinceTerm  = input("Input your start date, e.g 2019-08-10: ")
    untilTerm = input("Input your end date, e.g 2019-08-17: ")
    
    for tweet in tweepy.Cursor(api.search, q = searchTerm -filter:retweets filterTerm,
                               since = "sinceTerm",
                               until = "untilTerm",
                               lang = "en").items():
"""

def tweetExtractor(q):
    for tweet in tweepy.Cursor(api.search, q = "google -filter:retweets -burn -flames -rainforest -fire -https -sex -deforestation -brazil -brazillian -burning -forest -oxygen -eat -ate -fruit",
                               since = "2019-08-16",
                               until = "2019-08-23",
                               lang = "en").items():
        
        csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])

        #Removes emojis as they cause an error
        non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
        print(tweet.created_at and tweet.text.translate(non_bmp_map))

    csvFile.close()
    sys.exit()

if __name__ == '__main__':
    printInstruction()
    sortDirectory()
    tweetExtractor()