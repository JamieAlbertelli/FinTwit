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

Before running it is neccesary to modify the code in order for it to run.

- Enter your Twitter API into the "tweetExtraction.py" file.
- Edit the code to take chosen parameters, such as :
                            Date,
                            Time,
                            Search term, and
                            Stopwords.

# Further Work

For further work head over to the development branch