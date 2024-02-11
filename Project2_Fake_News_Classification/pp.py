import nltk
import pandas as pd
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('stopwords')

# Load the training and test data
train_data = pd.read_csv('train.csv')
test_data = pd.read_csv('test.csv')


# Define a function to perform data cleaning and preprocessing
def preprocess_text(text):
    # Convert the text to lowercase
    text = text.lower()
    # Tokenize the text into words
    words = word_tokenize(text)
    # Remove stop words
    stop_words = set(stopwords.words('english'))
    words = [w for w in words if w not in stop_words]
    # Stem the words
    stemmer = PorterStemmer()
    words = [stemmer.stem(w) for w in words]
    # Join the words back into a single string separated by space
    text = ' '.join(words)
    return text


# Preprocessing title1 and title2 columns in the training and test data
train_data['title1_en'] = train_data['title1_en'].apply(preprocess_text)
train_data['title2_en'] = train_data['title2_en'].apply(preprocess_text)
test_data['title1_en'] = test_data['title1_en'].apply(preprocess_text)
test_data['title2_en'] = test_data['title2_en'].apply(preprocess_text)

# Save the preprocessed train_data DataFrame to a CSV file
train_data.to_csv('train_pp.csv', index=False)

# Save the preprocessed test_data DataFrame to a CSV file
test_data.to_csv('test_pp.csv', index=False)
