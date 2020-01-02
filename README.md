# FinTwit

A Python application which extracts tweets and correlates their sentiment with closing day stock prices. A user enters parameters that define which tweets are extracted into a CSV file. From which the program performs sentiment analysis and visualises the data.

Please note that due to a limitation caused by Twitter's API tweets that are older than 2 weeks cannot be obtained. There is also a rate limit which caps the amount of tweets which can be searched. "15 requests per rate limit". For more information seek - https://developer.twitter.com/en/docs/basics/rate-limiting

For full Twitter API documentation make use of

https://developer.twitter.com/en/docs

# Dependencies

To run the program the following packages/tools are required.

Tweepy 3.5.0

TextBlob 0.15.2

Numpy

Pandas

# Pre-Requisite

Before loading the program it is neccessary to enter your Twitter API into the "tweetExtraction.py" file.

Also edit code to take chosen parameters, such as :
                            Date,
                            Time,
                            Search term, and
                            Stopwords.

# Further Work

In order to improve the functionality of the program further advancements are planned. Due to this being a project produced under time constraints many improvements are set to be made.

### First Stage

#### Currently pursuing
- Complete program to run seamlessly without need for human program editing.
     
     - Migrate pathing libraries from os to pathlib
      
- Implement a GUI to take values for search time, dates, number of tweets.

### Second Stage

- Host the program server side to avoid the limitations Twitter's API places on free accounts. For instance by invoking the program at a regular set interval regular data can be obtained.

- Set up a database to deal with continuous data.

- Improve data visualisation.

### Third Stage

- Incorporate Emojis as a form of sentiment.
