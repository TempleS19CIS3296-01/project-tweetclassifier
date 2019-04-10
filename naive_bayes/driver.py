from parse_data import build_data, extract_features
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

MAIN_FILE = "training.1600000.processed.noemoticon.csv"
DATA_DIR = "sentiment140/tweetdata01.csv"

if __name__=='__main__':
    print("Building data")
    build_data(DATA_DIR)

    print("Extracting features")
    training_feature, training_labels, testing_features, testing_labels = extract_features(DATA_DIR)
    

    model = GaussianNB()
    model.fit(training_feature, training_labels)


    # Predicting
    predicted_labels = model.predict(testing_features)
    print('Accuracy:', accuracy_score(testing_labels, predicted_labels) * 100)
