import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split

# load the data from csv files
train_df = pd.read_csv('train_pp.csv')
test_df = pd.read_csv('test_pp.csv')

train_df.fillna('', inplace=True)
test_df.fillna('', inplace=True)

# extracting the features
vectorizer = TfidfVectorizer(stop_words='english')
train_features = vectorizer.fit_transform(train_df['title1_en'] + ' ' + train_df['title2_en'])
test_features = vectorizer.transform(test_df['title1_en'] + ' ' + test_df['title2_en'])

# extracting the labels
train_labels = train_df['label']

# splitting training data into training and validation set
train_features_train, train_features_val, train_labels_train, train_labels_val = train_test_split(train_features, train_labels, test_size=0.2, random_state=42)

# training the model
classifier = LogisticRegression(max_iter=5000)
classifier.fit(train_features_train, train_labels_train)

# evaluating predictions on validation data
value_predictions = classifier.predict(train_features_val)
value_accuracy = accuracy_score(train_labels_val, value_predictions)
print(f'Validation accuracy for Logistic Regression : {value_accuracy*100:.2f}%')
print(classification_report(train_labels_val, value_predictions))

# generating confusion matrix
conf_mat = confusion_matrix(train_labels_val, value_predictions)
print(conf_mat)


# predicting on the test data
test_predictions = classifier.predict(test_features)

# saving the predictions to submission csv file
submission_df = pd.read_csv('sample_submission.csv')
submission_df['label'] = test_predictions
submission_df.to_csv('submission.csv', index=False)
