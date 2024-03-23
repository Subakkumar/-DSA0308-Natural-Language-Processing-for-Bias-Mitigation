from nltk.stem import PorterStemmer

# Define your list of words
words = ["running", "jumps", "better", "writing", "written"]

# Create a Porter Stemmer object
stemmer = PorterStemmer()

# Apply stemming to each word and store the results
stemmed_words = [stemmer.stem(word) for word in words]

print("Original Words:", words)
print("Stemmed Words:", stemmed_words)
