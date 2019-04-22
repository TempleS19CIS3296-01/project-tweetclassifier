from parse_data import build_data, extract_features
predict_dir = "predict_data/"
to_predict_matrix, to_predict_tweets = extract_features(predict_dir)
print(len(to_predict_matrix[0]))
    
