#!/usr/bin/env python
# -*- coding: utf-8 -*-

####
#### Author: Pedro Paulo Balage Filho
#### Version: 1.0
#### Date: 12/03/13
####

#### This python script provides a tempalte  to run the hybrid sentiment classifier for Semeval 2013 Task 2
#### Information about Semeval format can be found at:
####    http://www.cs.york.ac.uk/semeval-2013/task2/
####

from SemevalTwitter import SemevalTwitter
from TwitterHybridClassifier import TwitterHybridClassifier

train_path='Data/tweeti-b.dist.data'
dev_path='Data/twitter-dev-gold-B.tsv'
test_path='Data/twitter-test-input-B.tsv'

semeval = SemevalTwitter(train_path,dev_path,test_path)
trainset = semeval.trainset
devset = semeval.devset
testset = semeval.testset

# Training the supervised model
print "Training..."
classifier = TwitterHybridClassifier(trainset + devset)

# Apply the classifier for all tweets in the testset
output_file = 'task2-TEAM-B-twitter-constrained.output'
fp = open(output_file,'w')
for num,tweet in enumerate(testset):
    print "Processing...",num
    tweet_class = classifier.classify(tweet['MESSAGE'])
    line = tweet['SID'] + '\t' + tweet['UID'] + '\t' + tweet_class + '\t' + tweet['MESSAGE']
    fp.write(line)
fp.close()


# Apply the classifier for all sms data in the testset
train_path='Data/tweeti-b.dist.data'
dev_path='Data/twitter-dev-gold-B.tsv'
test_path='Data/sms-test-input-B.tsv'

semeval = SemevalTwitter(train_path,dev_path,test_path)
testset = semeval.testset

output_file = 'task2-TEAM-B-sms-constrained.output'
fp = open(output_file,'w')
for num,tweet in enumerate(testset):
    print "Processing...",num
    tweet_class = classifier.classify(tweet['MESSAGE'])
    line = tweet['SID'] + '\t' + tweet['UID'] + '\t' + tweet_class + '\t' + tweet['MESSAGE']
    fp.write(line)
fp.close()
