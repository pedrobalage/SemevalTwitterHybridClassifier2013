# -*- coding: utf-8 -*-

####
#### Author: Pedro Paulo Balage Filho
#### Version: 1.0
#### Date: 12/03/13
####

#### Class to provide a data reader for Semeval Task 2 format.
#### The reader was designed for task2 (sentiment in the whole twitter message) only.
#### Information about Semeval format can be found at:
####    http://www.cs.york.ac.uk/semeval-2013/task2/index.php?id=data
####
class SemevalTwitter(object):

    # Constructor.
    def __init__(self,train_path,dev_path,test_path):
        self.train_path = train_path
        self.dev_path = dev_path
        self.test_path = test_path
        self.trainset = list()
        self.devset = list()
        self.testset = list()

        self.reader()

    def reader(self):
        # For TrainSet
        tweets = []
        pt = open(self.train_path,'r')
        for line in pt:
            tweet_line = line.split('\t')
            if len(tweet_line) != 4:
                print 'Error to read TrainSet. Must have 4 args. Line: ', line
            tweet = {}
            tweet['SID'] = tweet_line[0]
            tweet['UID'] = tweet_line[1]
            sentiment = tweet_line[2][1:-1]
            # classes objective and neutral merged as proposed in the task
            if sentiment in ['objective','objective-OR-neutral']:
                sentiment = 'neutral'
            tweet['SENTIMENT'] = sentiment
            tweet['MESSAGE'] = tweet_line[3]
            tweets.append(tweet)

        self.trainset = tweets

        # For DevSet
        tweets = []
        pt = open(self.dev_path,'r')
        for line in pt:
            tweet_line = line.split('\t')
            if len(tweet_line) != 4:
                print 'Error to read DevSet. Must have 4 args. Line: ', line
            tweet = {}
            tweet['SID'] = tweet_line[0]
            tweet['UID'] = tweet_line[1]
            sentiment = tweet_line[2]
            # classes objective and neutral merged as proposed in the task
            if sentiment in ['objective','objective-OR-neutral']:
                sentiment = 'neutral'
            tweet['SENTIMENT'] = sentiment
            tweet['MESSAGE'] = tweet_line[3]
            tweets.append(tweet)

        self.devset = tweets

        # For TestSet
        tweets = []
        pt = open(self.test_path,'r')
        for line in pt:
            tweet_line = line.split('\t')
            if len(tweet_line) != 4:
                print 'Error to read DevSet. Must have 4 args. Line: ', line
            tweet = {}
            tweet['SID'] = tweet_line[0]
            tweet['UID'] = tweet_line[1]
            sentiment = tweet_line[2]
            tweet['SENTIMENT'] = sentiment
            tweet['MESSAGE'] = tweet_line[3]
            tweets.append(tweet)

        self.testset = tweets
