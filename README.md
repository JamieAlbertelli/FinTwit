# FinTwit

A Python application which extracts tweets and correlates their sentiment with closing day stock prices. A user enters parameters defining which tweets are extracted into a CSV file. From which the program performs sentiment analysis and visualises the data.

Please note that due to a limitation caused by Twitter's API tweets that are older than 2 weeks cannot be obtained. There is also a rate limit which caps the amount of tweets which can be searched. "15 requests per rate limit". For more information seek;

https://developer.twitter.com/en/docs/basics/rate-limiting

For full Twitter API documentation make use of;

https://developer.twitter.com/en/docs


![alt text](https://raw.githubusercontent.com/JamieAlbertelli/FinTwit/master/data/figures/facebook/facebook_closing_price_vs_avg_polarity_with_dates.png)


# Dependencies

To run the program the following packages/tools are required.

Tweepy

TextBlob

Numpy

Pandas

pandas_datareader

matplotlib

# Pre-Requisite

Before running 'tweetExtraction.py' it is neccesary to modify the code for it to run.

- Enter your Twitter API keys into the respective variables.
- Edit the code to take chosen parameters, such as :
                            Date,
                            Time,
                            Search term, and
                            Stopwords.

# Further Work

Due to this being a project produced under time constraints many improvements are set to be made.

### First Stage

#### Currently pursuing
- Complete program to run seamlessly without need for human input. 
     - Migrate pathing libraries from os to pathlib 
          -  file 'tweetExtraction.py' is complete ✓ 
          - file 'nlpAnalysis.py' is not. ✘
     - Automate path, directory and file creation
     - Produce a package to auto-install dependencies.

- Implement a GUI to take values for search time, dates, number of tweets.

### Second Stage

- Host the program server side to try and circumnavigate the limitations Twitter's API places on free accounts. 
    - E.g - by invoking the program at a regular set interval regular data can be obtained.

- Set up a database to deal with continuous data.

- Improve data visualisation.

### Third Stage

- Incorporate Emojis as a form of sentiment.


### Distant Future

- Develop NLP or go further and get some ML involved.