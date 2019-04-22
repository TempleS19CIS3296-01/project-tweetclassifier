from parse_data import build_data, extract_features
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

train_dir = "train_data/"
test_dir = "test_data/"
predict_dir = "predict_data/"

if __name__=='__main__':
    print("Building data")
    build_data(train_dir, 3500)

    print("Extracting features")
    train_matrix, train_labels = extract_features(train_dir, 3500, 100000)

    model = MultinomialNB()
    model.fit(train_matrix, train_labels)
    p_l2 =model.predict(train_matrix)
    print('Accuracy of train predictions:', accuracy_score(train_labels, p_l2) * 100)

    
    test_matrix, test_labels = extract_features(test_dir, 3500, 100000)

    # Predicting on test data
    predicted_labels = model.predict(test_matrix)
    print('Accuracy of test predictions:', accuracy_score(test_labels, predicted_labels) * 100)

    #making prediction on new data
    num_tweets = 3240
    to_predict_matrix, to_predict_tweets = extract_features(predict_dir, 3500, num_tweets)
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
