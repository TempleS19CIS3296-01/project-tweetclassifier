from parse_data import build_data, extract_features
from sklearn import tree
from sklearn.metrics import accuracy_score
from sklearn import svm

train_dir = "train_data/"
test_dir = "test_data/"

if __name__=='__main__':
    print("Building data")
    build_data(train_dir)

    print("Extracting features")
    train_matrix, train_labels = extract_features(train_dir)

    model = svm.linearSVC(gamma='scale')
   # model = tree.DecisionTreeClassifier()
    model.fit(train_matrix, train_labels)
    p_l2 =model.predict(train_matrix)
    print('Accuracy of train predictions:', accuracy_score(train_labels, p_l2) * 100)

    
    test_matrix, test_labels = extract_features(test_dir)

    # Predicting
    predicted_labels = model.predict(test_matrix)

    print('Accuracy of test predictions:', accuracy_score(test_labels, predicted_labels) * 100)

