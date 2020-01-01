#Import statements
import csv
import sys
import datetime
import os.path

import numpy as np
from numpy import mean
from numpy import std

import matplotlib.pyplot as plt
from matplotlib import pyplot

from textblob import TextBlob

from pandas import Series
import pandas as pd
import pandas_datareader as pdr



#Loads up csv file extracted from nlpExtractor, edit the name inside the apostraphe to match your chosen file.
infile = 'data/facebook.csv'

#Arrays for data to go in for graph
dateArray = []
opinionArray = []
biasArray = []
sentenceArray = []

#Responsible for taking csv data, appending to an array and performing NLP tasks.
#Prints out information regarding sentiment and subjectivity.
def tweetAnalyser():
    with open(infile, 'r') as csvfile: 
        rows = csv.reader(csvfile)
        for row in rows:
            date = row[0]
            sentence = row[2]
                       
            #Assigns variable to pass to TextBlob library
            blob = TextBlob(sentence)
            polarity = blob.sentiment.polarity            
            subjectivity = blob.sentiment.subjectivity

            #Adds sentiment(opinion) and subjectivity(bias) to a list
            #As well as performing the NLP tasks
            opinionArray.append(polarity)
            biasArray.append(subjectivity)
            sentenceArray.append(sentence)
            #Adds date and time to a list
            dateArray.append(row[0])

            

            #Print statement
            print('The Tweet was posted at : ' + (date) + '\n\n:' + (sentence) +
                    '\n \nSentiment value = ' + (str(polarity)) +
                    '\nSubjectivity value = ' + (str(subjectivity)) + '\n\n')

#Adds Polarity value           
def appendPolarityToArray():
        a = opinionArray
        if not os.path.isfile("data/graphs/facebook_graphing.csv"):   
            np.savetxt("data/graphs/facebook_graphing.csv", a)
        else:
            print('The file already exists \n')

def plotPolarity():    
        polls = pd.read_csv("data/graphs/facebook_graphing.csv", index_col=0)
        ax = polls.plot()
        plt.gcf().autofmt_xdate()
        plt.xticks(rotation = 90)
        plt.xlabel('Time')
        plt.ylabel('Polarity (Opinion)')
        plt.title('Facebook')
        plt.show()
        
def plotRealData():
    #Gets data from Yahoo Finance and places data into CSV file
    start = datetime.datetime(2019, 8, 16)
    end = datetime.datetime(2019, 8, 23)
    df = pdr.DataReader("fb", 'yahoo', start, end)
    df.to_csv('data/correlation/facebook_stock_prices.csv')                    

    #Plots the real data
    polls = pd.read_csv("data/correlation/facebook_stock_prices.csv", index_col=0)
    ax = polls['Close']
    ax.plot()
    plt.title('Facebook')
    plt.xlabel('Time')
    plt.ylabel('Price')
    plt.show()

def correlate():
    df = pd.read_csv("data/correlation/facebook_stock_prices_with_avg_pol.csv", usecols = [4,7])
    corvar = df.corr()
    print(corvar)

def plotAvgCorrelation():
    df = pd.read_csv("data/correlation/facebook_stock_prices_with_avg_pol.csv", index_col=0)

    plt.scatter(df['Close'], df['Avg Polarity'])
    plt.title('Closing Price vs Average Polarity')
    plt.xlabel('Price')
    plt.ylabel('Polarity')
    plt.show()

def plotFullCorrelation():
    df = pd.read_csv("data/graphs/facebook_graphing.csv")
    
    plt.scatter(df['Date'], df['Polarity'])
    plt.title('Price vs Polarity')
    plt.gcf().autofmt_xdate()
    plt.xticks(rotation = 90)
    plt.xlabel('Time')
    plt.ylabel('Polarity')
    plt.show()
                

"""
def averagePolarity():
    averagePolarity = opinionArray.count(UNSURE OF VARIABLE TO COUNT) / len(sentenceArray)
    print('The average number of Polarity is : ' + (str(averagePolarity)))
        
    averageSubjectivity = biasArray.count(blob) / sentenceArray.count(sentence)
    print('The average number of Subjectivity is : ' + (str(averageSubjectivity)))
"""    
#Main class responsible for running function
if __name__ == '__main__':
    tweetAnalyser()
    appendPolarityToArray()
    plotPolarity()
    plotRealData()
    correlate()
    plotAvgCorrelation()
    plotFullCorrelation()
    #averagePolarity()
    
        






        
