#Import Statement
import tweepy
import csv
import sys

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
csvFile = open('data\google.csv', 'a')

csvWriter = csv.writer(csvFile)

"""
Extracts Tweet data
q = query
-words mean stopwords (words to not search for)
since and until are the dates Tweepy gathers tweets between
"""
def tweetExtractor():
    for tweet in tweepy.Cursor(api.search, q = "google -filter:retweets -burn -flames -rainforest -fire -https -sex -deforestation -brazil -brazillian -burning -forest -oxygen -eat -ate -fruit",
                               since = "2020-01-23",
                               until = "2020-01-23",
                               lang = "en").items():
        
        csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])

        #Removes emojis as they cause an error
        non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
        print(tweet.created_at and tweet.text.translate(non_bmp_map))

    csvFile.close()
    sys.exit()

if __name__ == '__main__':
    tweetExtractor()
