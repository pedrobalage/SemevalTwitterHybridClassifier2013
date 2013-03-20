
Author: Pedro Paulo Balage Filho
Version: 1.0
Date: 12/03/13

These python scripts provide the HybridClassifier I used for the Semeval 2013 Task2 - Twitter Classification - Track B (http://www.cs.york.ac.uk/semeval-2013/task2/)

You can reproduce my results or adapt my code for your experiments. 
In order to run this code, you must have a python 2.x version and the CLiPS Pattern installed (http://www.clips.ua.ac.be/pages/pattern)
In ubuntu, I install this library using these commands in the terminal

    sudo aptitude install python-pip
    sudo pip install pattern

You must also provide the training data and dictionaries used. I do not provide these files for copyright reasons.
Please see the Data/README.md for more information how to get these files.

After placing the required data in Data/ folder, you can reproduce my Semeval results with the command:

    python run_Semeval_classifier.py

It is going to generate two files: 

    task2-TEAM-B-twitter-constrained.output
    task2-TEAM-B-sms-constrained.output

which contains the predictions.


If you like to use (without any warranty) my TwitterHybridClassifier, you may call it in python using the follow statements:

    from TwitterHybridClassifier import TwitterHybridClassifier
    # you must build a trainset. See the SemevalTwitter.py to check the trainset format
    classifier = TwitterHybridClassifier(trainset)
    prediction = classifier.classify(tweet_message)

Any doubts or suggestions, please contact me at: pedrobalage (at) gmail (dot) com

