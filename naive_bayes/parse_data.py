import os
import csv
from collections import Counter
import numpy as np

data = {}

MOST_COMMON = 3200 #this is the number of most common words to be analyzed in the model
delete_symbols = False #a boolean to check if symbols should be deleted from data
NUM_TWEETS = 100000 #this is the size of the dataset
NUM_TESTS = 10000
factor = 1 #factor by which we are reducing the matrice
#creates dictionary of most common N words and their corresponding frequency
def build_data(data_dir):
    all_words = []

    #opening and parsing file
    with open(data_dir, 'r', encoding="ISO-8859-1") as csv_file:
        reader = csv.reader(csv_file)
        
        i = 1
        for row in reader:
            if i%factor == 0:
                all_words += row[5].split() #adds each words to all_words list of words  
            i+=1

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


    train_matrix = np.zeros((NUM_TWEETS-NUM_TESTS, MOST_COMMON))
    train_labels = np.zeros(NUM_TWEETS-NUM_TESTS)

    test_matrix = np.zeros((NUM_TESTS, MOST_COMMON))
    test_labels = np.zeros(NUM_TESTS)

    train_count = 0
    test_count = 0
    counter = 1

    with open(data_dir, 'r', encoding="ISO-8859-1") as csv_file:
        reader = csv.reader(csv_file)
        for i, row in enumerate(reader, start = 1):
            if i%factor==0:
                line = row[5].split() #tweet contents

                #handling test data
                if counter <= NUM_TESTS//2 or counter > (NUM_TWEETS - (NUM_TESTS//2)):
                    for word in line:
                        if word in data:
                            test_matrix[test_count, data[word]] = line.count(word)
                    test_labels[test_count] = int(row[0])
                    test_count += 1
                #handling train data
                else:
                    for word in line:
                        if word in data:
                            train_matrix[train_count, data[word]] = line.count(word)
                    train_labels[train_count] = int(row[0])
                    train_count += 1
                counter += 1    
    return train_matrix, train_labels, test_matrix, test_labels    

