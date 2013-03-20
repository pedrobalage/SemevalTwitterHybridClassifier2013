This directory must have the following files:

- Semeval Task2 - Twitter Classification - Data
    In order to reproduce my results, you must provide the trainset, devset and testset from the Semeval Task2, Track B
    This data can be placed under the folder Data/
    You may have the following files. You can modify the file names, but you will have to modify the run_Semeval script

        Data/tweeti-b.dist.data
        Data/twitter-dev-gold-B.tsv
        Data/twitter-test-input-B.tsv
        Data/sms-test-input-B.tsv


- Lexicon-based Data
    It uses the dictionaries provided by SentiStrengh
    The dicionaries must be downloaded and places under the folder Data/
    Download link: http://sentistrength.wlv.ac.uk/download.html
    You must have the following files in order to run the HybridClassifier:

        Data/EmotionLookupTable.txt
        Data/EmoticonLookupTable.txt
        Data/NegatingWordList.txt
        Data/BoosterWordList.txt
