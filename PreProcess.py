#!/usr/bin/env python
# -*- coding: utf-8 -*-

####
#### Author: Pedro Paulo Balage Filho
#### Version: 1.0
#### Date: 12/03/13
####

from string import punctuation, letters
import re

# Requires Pattern library (http://www.clips.ua.ac.be/pages/pattern)
from pattern.en     import tag
from pattern.vector import stem, PORTER

### Provides a pre-process for tweet messages.
### Replace emoticons, hash, mentions and urls for codes
### Correct long seguences of letters and punctuations
### Apply the Pattern part-of_speech tagger to the message
### Requires the Pattern library to work (http://www.clips.ua.ac.be/pages/pattern)
def pre_process(tweet_message):
    # Pattern tag -> a fast tagger

    # assures the message can be converted to unicode. Reject the encoding
    # errors
    tweet_message = tweet_message.decode('utf8',errors='ignore')

    # substitute hashes
    tweet_message = re.sub(re.escape('#')+r'(\w+)','&hash \g<1>',tweet_message)

    # substitute users mentions
    tweet_message = re.sub(re.escape('@')+r'(\w+)','&mention \g<1>',tweet_message)

    # substitute urls
    tweet_message = re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+','&url',tweet_message)

    # look for emoticons.
    # Some elements from http://en.wikipedia.org/wiki/List_of_emoticons
    emoticons = { ':-)'   : '&happy',
                    ':)'    : '&happy',
                    ':o)'   : '&happy',
                    ':]'    : '&happy',
                    ':3'    : '&happy',
                    ':c)'   : '&happy',
                    ':>'    : '&happy',
                    '=]'    : '&happy',
                    '8)'    : '&happy',
                    '=)'    : '&happy',
                    ':}'    : '&happy',
                    ':^)'   : '&happy',
                    ':-))'  : '&happy',
                    '|;-)'  : '&happy',
                    ":'-)"  : '&happy',
                    ":')"   : '&happy',
                    '\o/'   : '&happy',
                    '*\\0/*': '&happy',
                    ':-D'   : '&laugh',
                    ':D'    : '&laugh',
                    '8-D'   : '&laugh',
                    '8D'    : '&laugh',
                    'x-D'   : '&laugh',
                    'xD'    : '&laugh',
                    'X-D'   : '&laugh',
                    'XD'    : '&laugh',
                    '=-D'   : '&laugh',
                    '=D'    : '&laugh',
                    '=-3'   : '&laugh',
                    '=3'    : '&laugh',
                    'B^D'   : '&laugh',
                    '>:['   : '&sad',
                    ':-('   : '&sad',
                    ':('    : '&sad',
                    ':-c'   : '&sad',
                    ':c'    : '&sad',
                    ':-<'   : '&sad',
                    ':<'    : '&sad',
                    ':-['   : '&sad',
                    ':['    : '&sad',
                    ':{'    : '&sad',
                    ':-||'  : '&sad',
                    ':@'    : '&sad',
                    ":'-("  : '&sad',
                    ":'("   : '&sad',
                    'D:<'   : '&sad',
                    'D:'    : '&sad',
                    'D8'    : '&sad',
                    'D;'    : '&sad',
                    'D='    : '&sad',
                    'DX'    : '&sad',
                    'v.v'   : '&sad',
                    "D-':"  : '&sad',
                    '(>_<)' : '&sad',
                    ':|'    : '&sad',
                    '>:O'   : '&surprise',
                    ':-O'   : '&surprise',
                    ':-o'   : '&surprise',
                    ':O'    : '&surprise',
                    '°o°'   : '&surprise',
                    ':O'    : '&surprise',
                    'o_O'   : '&surprise',
                    'o_0'   : '&surprise',
                    'o.O'   : '&surprise',
                    '8-0'   : '&surprise',
                    '|-O'   : '&surprise',
                    ';-)'   : '&wink',
                    ';)'    : '&wink',
                    '*-)'   : '&wink',
                    '*)'    : '&wink',
                    ';-]'   : '&wink',
                    ';]'    : '&wink',
                    ';D'    : '&wink',
                    ';^)'   : '&wink',
                    ':-,'   : '&wink',
                    '>:P'   : '&tong',
                    ':-P'   : '&tong',
                    ':P'    : '&tong',
                    'X-P'   : '&tong',
                    'x-p'   : '&tong',
                    'xp'    : '&tong',
                    'XP'    : '&tong',
                    ':-p'   : '&tong',
                    ':p'    : '&tong',
                    '=p'    : '&tong',
                    ':-Þ'   : '&tong',
                    ':Þ'    : '&tong',
                    ':-b'   : '&tong',
                    ':b'    : '&tong',
                    ':-&'   : '&tong',
                    ':&'    : '&tong',
                    '>:\\'  : '&annoyed',
                    '>:/'   : '&annoyed',
                    ':-/'   : '&annoyed',
                    ':-.'   : '&annoyed',
                    ':/'    : '&annoyed',
                    ':\\'   : '&annoyed',
                    '=/'    : '&annoyed',
                    '=\\'   : '&annoyed',
                    ':L'    : '&annoyed',
                    '=L'    : '&annoyed',
                    ':S'    : '&annoyed',
                    '>.<'   : '&annoyed',
                    ':-|'   : '&annoyed',
                    '<:-|'  : '&annoyed',
                    ':-X'   : '&seallips',
                    ':X'    : '&seallips',
                    ':-#'   : '&seallips',
                    ':#'    : '&seallips',
                    'O:-)'  : '&angel',
                    '0:-3'  : '&angel',
                    '0:3'   : '&angel',
                    '0:-)'  : '&angel',
                    '0:)'   : '&angel',
                    '0;^)'  : '&angel',
                    '>:)'   : '&devil',
                    '>;)'   : '&devil',
                    '>:-)'  : '&devil',
                    '}:-)'  : '&devil',
                    '}:)'   : '&devil',
                    '3:-)'  : '&devil',
                    '3:)'   : '&devil',
                    'o/\o'  : '&highfive',
                    '^5'    : '&highfive',
                    '>_>^'  : '&highfive',
                    '^<_<'  : '&highfive',
                    '<3'    : '&heart'
                }

    # substitute emoticons using regular expression
    for symbol in emoticons:
        tweet_message = re.sub(r'('+re.escape(symbol)+r')[^a-z0-9A-Z]',' \g<1> '+emoticons[symbol]+' ',tweet_message+' ')

    # normalize punctuation signals, like ..., !!!!!!!!, ???????, etc
    tweet_message = re.sub(re.escape('...'),'.' + ' &dots',tweet_message)
    for symbol in punctuation:
        tweet_message = re.sub(re.escape(symbol)+r'{3,}',' ' + symbol + ' &emphasis',tweet_message)

    # normalize long sequence of letters coooool -> col, looooove -> love,
    # gooooodd -> god
    # (always keep one letter)
    for symbol in letters:
        tweet_message = re.sub(re.escape(symbol)+r'{3,}', symbol ,tweet_message)

    # remove many blank spaces.
    tweet_message = re.sub(' +',' ' ,tweet_message)
    tweet_message = tweet_message.strip()

    # Include POS information
    tweet_message = tag(tweet_message, tokenize=False)

    # Stemmer?
    #tweet_message = [(stem(w, stemmer=PORTER),t) for w,t in tweet_message]

    # return the twitte in the format [(word,tag),...]
    return tweet_message
