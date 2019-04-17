from parse_data import build_data, extract_features
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

train_dir = "train_data/"
test_dir = "test_data/"

if __name__=='__main__':
    print("Building data")
    build_data(train_dir)

    print("Extracting features")
    train_matrix, train_labels = extract_features(train_dir)

    model = GaussianNB()
    model.fit(train_matrix, train_labels)

    train_matrix = 1
    train_labels = 1
    
    test_matrix, test_labels = extract_features(test_dir)

    # Predicting
    predicted_labels = model.predict(test_matrix)
    print('Accuracy:', accuracy_score(test_labels, predicted_labels) * 100)
