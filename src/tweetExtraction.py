#Import Statement
import tweepy
import csv
import sys

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
#Writes data from function to chosen file
csvFile = open('data/google.csv', 'a')
csvWriter = csv.writer(csvFile)

"""
def sortDirectory():
    path = pathlib.Path("../FinTwit/data")
    path.mkdir(parents=True, exist_ok=True)

    filename = ***USER INPUT HERE***
    
    filepath = path / filename
    with filepath.open("w", encoding = "utf-8") as f:
        f.write()
"""

"""
Extracts Tweet data
def tweetExtractor(q):
    searchTerm = input("Input your desired search term: ")
    filterTerm = input("Input your filter words: ")
    sinceTerm  = input("Input your filter words: ")
    untilTerm = inpu
    for tweet in tweepy.Cursor(api.search, q = searchTerm -filter:retweets -burn -flames -rainforest -fire -https -sex -deforestation -brazil -brazillian -burning -forest -oxygen -eat -ate -fruit",
                               since = "2019-08-16",
                               until = "2019-08-23",
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
    tweetExtractor()