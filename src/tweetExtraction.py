#Import Statements
import tweepy
import csv
import sys
import time

from pathlib import Path

### Initialisation of Keys ###
#Will move to another file for better abstraction
#Twitter API keys and tokens
consumer_key = 'ENTER_PUBLIC_CONSUMER_KEY'
consumer_secret = 'ENTER_SECRET_CONSUMER_KEY'

access_token = 'ENTER_PUBLIC_ACCESS_KEY'
access_token_secret = 'ENTER_SECRET_ACCESS_KEY'

#Authentication 
auth = tweepy.auth.OAuthHandler(consumer_key ,consumer_secret)
auth.set_access_token(access_token, access_token_secret)

#Stores Authentication and waits on Twitter's rate limit
api = tweepy.API(auth, wait_on_rate_limit = True)

#Writes data from function to chosen file                
stock = input("What stock do you want to search today? ")

#Writes data from function to chosen file
p = Path("../FinTwit/data")
p.mkdir(parents = True, exist_ok = True)
filename = (stock + '.csv')
filepath = p / filename

#Prints file and location
fileNamePrint = 'File is named 'f'{filename}'
filePathPrint = 'File is located in 'f'{filepath}'
print(fileNamePrint + "\n" + filePathPrint)

#Initialises q (query) in for loop param
myStockFilter = " -filter:retweets "
userStockFilter = input("Input your filter words, begin terms with a '-' and seperate with a space, i.e ""-spam -pie"" NB ommits retweets by default: " )
sinceDate  = input("Input your start date, e.g 2019-08-10: " )
untilDate = input("Input your end date, e.g 2019-08-17: " )

with open(filepath, 'w') as csv_file:
    csvWriter = csv.writer(csv_file)

    #q = query
    for tweet in tweepy.Cursor(api.search, q = stock + myStockFilter + userStockFilter, since = sinceDate, until = untilDate, lang = "en").items():
        csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])

        #Removes emojis due to error. Can be solved by obtaining paid API.
        non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
        print(tweet.created_at and tweet.text.translate(non_bmp_map))
        
    csv_file.close()
    sys.exit()
"""
if __name__ == '__main__':
    tweetExtractor()
"""