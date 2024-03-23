import nltk

# Get text data (replace with your own text)
text = "They are running very quickly towards the finish line."

# Tokenize the text
tokens = nltk.word_tokenize(text)

# Stemming using PorterStemmer
stemmer = nltk.PorterStemmer()
stemmed_words = [stemmer.stem(word) for word in tokens]

# Lemmatization using WordNetLemmatizer
lemmatizer = nltk.WordNetLemmatizer()
lemmatized_words = [lemmatizer.lemmatize(word) for word in tokens]

# Print results
print("Original Text:", text)
print("\nStemmed Words:", stemmed_words)
print("\nLemmatized Words:", lemmatized_words)
