# -*- coding: utf-8 -*-

####
#### Author: Pedro Paulo Balage Filho
#### Version: 1.0
#### Date: 12/03/13
####

#### Provides a Lexicon-based sentiment analysis classifier.
#### It uses the dictionaries provided by SentiStrengh.
#### The dicionaries must be downloaded and places under the folder Data/
#### Download link: http://sentistrength.wlv.ac.uk/download.html
class LexiconClassifier(object):


    def __init__(self):
        # Load SentiStrengh dictionaries
        self.dictionary = self.read_SentiStrengh_dict()
        self.booster    = self.read_SentiStrengh_booster()
        self.negation   = self.read_SentiStrengh_negation()

    # Read SentiStrengh dictionary of emotions and emoticons
    def read_SentiStrengh_dict(self):
        dictionary={}

        # read emotion list
        fp = open("Data/EmotionLookupTable.txt");
        for line in fp:
            line = line.split('\t')
            if len(line) >= 2:
                word = line[0].strip()
                word = word.decode()
                so = line[1].strip()
                dictionary[word] = float(so)
        fp.close()

        # read emoticons list
        fp = open("Data/EmoticonLookupTable.txt");
        for line in fp:
            line = line.split('\t')
            if len(line) >= 2:
                word = line[0].strip()
                word = word.decode(errors='replace')
                so = line[1].strip()
                dictionary[word] = float(so)
        fp.close()

        return dictionary

    # Read SentiStrengh negatingWordList
    def read_SentiStrengh_negation(self):
        negation_list=[]
        fp = open("Data/NegatingWordList.txt");
        for line in fp:
            word = line.strip()
            word = word.decode()
            negation_list.append(word)
        fp.close()
        return negation_list

    # Read SentiStrengh booster WordList
    def read_SentiStrengh_booster(self):
        booster_list={}
        fp = open("Data/BoosterWordList.txt");
        for line in fp:
            line = line.split('\t')
            if len(line) >= 2:
                word = line[0].strip()
                word = word.decode()
                so = line[1].strip()
                booster_list[word] = float(so)
        fp.close()
        return booster_list

    # Find a word in SentiStrengh diciontary. Matches words with wildcards, ex:
    # anxiety -> anxi*; angry -> angr*
    def find_word(self, word, word_list):
        result = None
        # Inneficient, but easy to implement
        matches = [w for w in sorted(word_list) if ( w==word ) or ( w[-1]=='*' and word.startswith(w[:-1]) ) ]
        # look for the longest match
        longest_match = 0
        for match in matches:
            if len(match) >  longest_match:
                longest_match = len(match)
                result = match
        return result

    # Applies the lexicon-based classifier
    # Receives a pre-processed tweet message. Format: [ (word,tag), ... ]
    # Returns a tuple with (num_of_positive_words, num_of_negative_words)
    def classify(self, tweet_message):

        # get only the words
        tweet_message = [w.lower() for w,tag in tweet_message]

        # initialize some variables
        pos_so = 0.0
        neg_so = 0.0
        intensifier = 0
        negation = False
        i_neg, i_int = 0,0
        lookup_window = 5

        # Iterate over the words
        for i,w in enumerate(tweet_message):

            # verify the word or closest match present in the dictionary
            w = self.find_word(w, self.dictionary.keys())

            if w in self.dictionary:

                    # Get the semantic orientation
                    so = self.dictionary[w]

                    # Modify if found negation. Shift 4 values, same operations
                    # of SO-Cal (Look for Taboada paper at ACL Journal)
                    if negation and (i-i_neg) <= lookup_window:
                        if so > 0:
                            so = so - 4
                        else:
                            so = so + 4

                    # Modify if found an intensifier
                    if intensifier and (i-i_int) <= lookup_window:
                        so = so + ( so * intensifier )

                    if so >0:
                        pos_so += so
                    else:
                        neg_so += so

                    # Negation and intensifiers are only valid for the next word.
                    negation = False
                    intensifier = 0
                    i_neg, i_int = 0,0

            if w in self.negation:
                negation = True
                i_neg = i

            if w in self.booster:
                intensifier = self.booster[w]
                i_int = i

        return (pos_so,neg_so)
