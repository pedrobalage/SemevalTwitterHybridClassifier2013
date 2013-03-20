# -*- coding: utf-8 -*-
####
#### Author: Pedro Paulo Balage Filho
#### Version: 1.0
#### Date: 12/03/13
####

from MachineLearningClassifier import MachineLearningClassifier
from RulesClassifier import RulesClassifier
from LexiconClassifier import LexiconClassifier
from PreProcess import pre_process

#### Provides a hybrid Sentiment Analysis classifier.
#### This classifier was originally designed for Semeval 2013 Task 2 - Twitter classification:
####    http://www.cs.york.ac.uk/semeval-2013/task2/
#### The trainset must be in SemevalTwitter format. See SemevalTwitter.py for information.
class TwitterHybridClassifier(object):

    def __init__(self, trainset=[]):
        self.rules_classifier = RulesClassifier()
        self.lexicon_classifier = LexiconClassifier()
        self.ml_classifier = MachineLearningClassifier(trainset)

    # Apply the classifier over a tweet message in String format
    def classify(self,tweet_text):

        # 0. Pre-process the text (emoticons, misspellings, tagger)
        tweet_text = pre_process(tweet_text)

        # 1. Rule-based classifier. Look for emoticons basically
        positive_score,negative_score = self.rules_classifier.classify(tweet_text)
        rules_score = positive_score + negative_score

        # 1. Apply the rules, If any found, classify the tweet here. If none found, continue for the lexicon classifier.
        if rules_score != 0:
            if rules_score > 0:
                sentiment = 'positive'
            else:
                sentiment = 'negative'
            return sentiment

        # 2. Lexicon-based classifier
        positive_score, negative_score = self.lexicon_classifier.classify(tweet_text)
        lexicon_score = positive_score + negative_score

        # 2. Apply lexicon classifier, If the lexicon score is
        # 0 (strictly neutral), >3 (positive with confidence) or
        # <3 (negative with confidence), classify the tweet here. If not,
        # continue for the SVM classifier
        if lexicon_score == 0:
            sentiment = 'neutral'
            return sentiment

        if lexicon_score >= 3:
            sentiment = 'positive'
            return sentiment

        if lexicon_score <= -3:
            sentiment = 'negative'
            return sentiment

        # 3. Machine learning based classifier - used the training set to define the best features to classify new instances
        scores = self.ml_classifier.classify(tweet_text)
        positive_conf = scores[0][1]
        negative_conf = scores[1][1]
        neutral_conf = scores[2][1]

        # 3. Apply machine learning classifier, If positive or negative
        # confidence (probability) is >=0.3, classify with the sentiment.
        # Otherwise, classify as neutral
        if positive_conf >= 0.3 and negative_conf < positive_conf:
            sentiment = 'positive'
        elif negative_conf >= 0.3:
            sentiment = 'negative'
        else:
            sentiment = 'neutral'

        return sentiment
