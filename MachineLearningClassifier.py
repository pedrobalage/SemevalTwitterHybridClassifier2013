# -*- coding: utf-8 -*-

####
#### Author: Pedro Paulo Balage Filho
#### Version: 1.0
#### Date: 12/03/13
####

# Requires Pattern library (http://www.clips.ua.ac.be/pages/pattern)
from pattern.vector import SVM, CLASSIFICATION, LINEAR
from pattern.en     import tag
from pattern.en.wordlist import STOPWORDS as stopwords

from PreProcess import pre_process
from operator import itemgetter
from copy import copy

#### Provides a Machine Learning Sentiment Analysis classifier.
class MachineLearningClassifier(object):

    def __init__(self, trainset=[]):

        # initializes a SVM classifier
        self.classifier = SVM(type=CLASSIFICATION, kernel=LINEAR)

        self.bag_of_words = []
        self.classifier.probability = True
        self.train(self.classifier,trainset)


    # Extract features for ML process
    def extract_features(self, tweet_message):

        if len(self.bag_of_words) == 0:
            printf('Bag-of-Words empty!')
            return None

        tweet_words = [word.lower() for word, tag in tweet_message if word not in stopwords and not word.isdigit()]
        tweet_tags = [tag[:2] for word, tag in tweet_message if word not in stopwords and not word.isdigit()]

        feature_set = {}

        # 1st set of features: bag-of-words
        for word in self.bag_of_words:
            feature_set['has_'+word] = (word in tweet_words)

        # 2nd set of features: the tags present in the message
        for tag in ['NN','VG','CD','JJ','CC','RB']:
            feature_set['has_'+tag] = (tag in tweet_tags)

        # 3rd feature: negation is present?
        negators = set(['not', 'none', 'nobody', 'never', 'nothing', 'lack', 't','n\'t','dont', 'no'])
        if len(negators.intersection(set(tweet_words))) > 0:
            feature_set['has_negator'] = True

        return feature_set


    # train the classifier
    # Tweets argument must be a list of dicitionaries. Each dictionary must
    # have the keys ['MESSAGE'] and ['SENTIMENT'] with the message string and
    # the classificationclass, respectively.
    def train(self,classifier,tweets):

        # build the bag-of-words list using the 1k most frequent words in
        # the corpus
        bag_of_words = {}
        for tweet in tweets:
            words = [w.lower() for w,t in pre_process(tweet['MESSAGE']) if w not in stopwords and not w.isdigit()]
            for word in words:
                bag_of_words[word] = bag_of_words.get(word,0) + 1

        # get the 1000 most frequent words
        self.bag_of_words = [w for w,freq in sorted(bag_of_words.items(),key=itemgetter(1),reverse=True)[:1000]]

        # perform the training step
        for tweet in tweets:
            classifier.train(self.extract_features(pre_process(tweet['MESSAGE'])),type=tweet['SENTIMENT'])


    # classify a new message. Return the scores (probabilities) for each
    # classification class
    def classify(self, tweet_message):
        scores = self.classifier.classify(self.extract_features(tweet_message))
        return scores

