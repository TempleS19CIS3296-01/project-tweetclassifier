import os
import csv
from collections import Counter
import numpy as np

data = {}

delete_symbols = False #a boolean to check if symbols should be deleted from data

#creates dictionary of most common N words and their corresponding frequency
def build_data(data_dir, most_common, tweets_per_file):
    MOST_COMMON = most_common
    TWEETS_PER_FILE = tweets_per_file
    
    all_words = []

    tweet_files = [data_dir+file for file in os.listdir(data_dir)]
    #opening and parsing file
    for file in tweet_files:
        with open(file, 'r', encoding="ISO-8859-1") as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                all_words += row[5].split()

    dictionary = Counter(all_words) #returns counter object of all words


    if delete_symbols: #if we want to delete words with symbols and words of length 1
        list_to_remove = list(dictionary)
        for word in list_to_remove:
            if len(word)==1:
                del dictionary[word] 
            elif not word.isalpha(): #gets rid of symbols and non word words
                del dictionary[word]
                
    dictionary = dictionary.most_common(MOST_COMMON)#only keep MOST_COMMON words in dictionary
    count = 0
    for word in dictionary:
        data[word[0]] = count
        count += 1

def extract_features(data_dir):
    tweet_files = [data_dir+file for file in os.listdir(data_dir)]

    matrix = np.zeros((len(tweet_files)*TWEETS_PER_FILE, MOST_COMMON))
    labels = np.zeros(len(tweet_files)*TWEETS_PER_FILE)


    tweet_count = 0

    for file in tweet_files:
        with open(file, 'r', encoding="ISO-8859-1") as csv_file:
            reader = csv.reader(csv_file)
            for i, row in enumerate(reader, start = 1):
                line = row[5].split()
                for word in line:
                    if word in data:
                        matrix[tweet_count, data[word]] = line.count(word)
                labels[tweet_count] = int(row[0])
                tweet_count+=1 
    return matrix, labels  

