#Import Statement
import tweepy
import csv
import sys

#Twitter API keys and tokens
consumer_key = 'ZpfdUtDdExcfvRWddLF9nUIr4'
consumer_secret = 'kN0S8kOrHnuTJPpiOGMyr3a3hHSHidua5M2HHB1AtLKN1zaL5Y'

access_token = '1154446515278155781-cTrRsc5yamKIjz3FmDWvefhaWp3bjp'
access_token_secret = 'nS3ZeWyX8Q5AATEY1bFbf624XlOKN3koAwp9gqldOqPiz'

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
