# -*- coding: utf-8 -*-
####
#### Author: Pedro Paulo Balage Filho
#### Version: 1.0
#### Date: 12/03/13
####

#### Provides a rule-based classifier
class RulesClassifier(object):

    # Classifies the tweet_message using rules. These looks for emoticons,  basically.
    # The message myst be pre-processed in the format (w,tag)
    def classify(self, tweet_message):

        positive_patterns = []
        negative_patterns = []

        # emoticons are substituted by codes in the pre-process step
        pos_patterns = ['&happy',
                        '&laugh',
                        '&wink',
                        '&heart',
                        '&highfive',
                        '&angel',
                        '&tong',
                       ]

        neg_patterns = ['&sad',
                        '&annoyed',
                        '&seallips',
                        '&devil',
                       ]

        # how many positive and negative emoticons are in the message?
        matches_pos = [token for token,tag in tweet_message if token in pos_patterns]
        matches_neg = [token for token,tag in tweet_message if token in neg_patterns]

        # return (positive_score , negative_score). Number of emoticons for
        # each sentiment
        return ( len(matches_pos),-len(matches_neg) )
