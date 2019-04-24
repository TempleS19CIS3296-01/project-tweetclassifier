from parse_data import build_data, extract_features
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.metrics import accuracy_score
from get_tweets import get_all_tweets

train_dir = "small_train_data/"
test_dir = "small_test_data/"
predict_dir = "predict_data/"

if __name__=='__main__':
    print("TRAINING WITH ADABOOSTED DECISION TREES")
    vocab_size = 1200
    tweets_per_file = 4000
    print("Building data")
    build_data(train_dir, vocab_size)

    print("Extracting features")
    train_matrix, train_labels = extract_features(train_dir, vocab_size, tweets_per_file)

    model = AdaBoostClassifier(DecisionTreeClassifier(), n_estimators=500,learning_rate = .5, algorithm="SAMME")
    
    model.fit(train_matrix, train_labels)
    p_l2 =model.predict(train_matrix)
    print('Accuracy of train predictions:', accuracy_score(train_labels, p_l2) * 100)

    
    test_matrix, test_labels = extract_features(test_dir, vocab_size, tweets_per_file)

    # Predicting on test data
    predicted_labels = model.predict(test_matrix)
    print('Accuracy of test predictions:', accuracy_score(test_labels, predicted_labels) * 100)


    #making prediction on new data
    answer = 1
    while answer:
        num_tweets = get_all_tweets()
        to_predict_matrix, to_predict_tweets = extract_features(predict_dir, vocab_size, num_tweets)
        prediction_labels_new_tweets = model.predict(to_predict_matrix)    
        pos = 0
        neg = 0
        for label in prediction_labels_new_tweets:
            if label == 0:
                neg += 1
            elif label == 4:
                pos+=1
            else:
                print("Error")
        print("Percentage of last", num_tweets, "tweets that were positive:", pos/num_tweets)
        print("Percentage of last", num_tweets, "tweets that were negative:", neg/num_tweets) 
        answer = int(input("Would you like to test a different twitter user?"))
    
