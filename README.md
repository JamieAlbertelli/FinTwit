# FinTwit

Does Twitter house information which can be used to predict stock pricing? This is a Python application which gathers Tweets and correlates their sentiment with stock prices. 

By entering; a chosen stock, from a specified date, and a choice of excluding any undesired terms, Tweets can be obtained. 
The Tweets are then stored in a CSV file where Sentiment Analysis (Opinion labelling) through Text Blob is completed. 
Finally through Pandas the stock prices (At the end of n Tweet's given day) and sentiment are correlated to see if the price of a stock has moved in correlation with the overall mood of Twitter users.

Please note that due to a limitation caused by Twitter's API tweets that are older than 1 week cannot be obtained. There is also a rate limit which caps the amount of tweets which can be searched. "15 requests per rate limit". For more information seek;

https://developer.twitter.com/en/docs/basics/rate-limiting

For full Twitter API documentation make use of:

https://developer.twitter.com/en/docs

Additionally these topics are of importance:

https://developer.twitter.com/en/docs/tweets/search/api-reference/get-search-tweets

https://developer.twitter.com/en/docs/tweets/rules-and-filtering/overview/standard-operators

# Image(s) of results

An example of sentiment and price correlation.

![alt text](https://raw.githubusercontent.com/JamieAlbertelli/FinTwit/master/figures/facebook/facebook_closing_price_vs_avg_polarity.png)
(Not the best graph)

# Dependencies

To run the program the following packages/tools are required.

Tweepy

TextBlob

Numpy

Pandas

pandas_datareader

matplotlib

# Pre-Requisite

- Enter your Twitter API keys into the respective variables.

# Further Work

Due to this being a project produced under time constraints many improvements are set to be made.

### First Stage

#### Currently pursuing
- Complete program to run seamlessly without need for human input. 
     - Migrate pathing libraries from os to pathlib 
          -  file 'tweetExtraction.py' is complete ✓ 
          - file 'nlpAnalysis.py' is not. ✘
     - Automate path, directory and file creation
          -  file 'tweetExtraction.py' is complete ✓ 
          - file 'nlpAnalysis.py' is not. ✘
     - Produce a package to auto-install dependencies.
          - Currently being produced. ✘

- Implement a GUI to take values for search time, dates, number of tweets.
          
          - Still a little way off. ✘

### Second Stage

- Host the program server side to try and circumnavigate the limitations Twitter's API places on free accounts. 
    - E.g - by invoking the program at a regular set interval regular data can be obtained.

- Set up a database to deal with continuous data.

- Improve data visualisation.

### Third Stage

- Incorporate Emojis as a form of sentiment.

### Distant Future

- Develop NLP or go further and get some ML involved.
