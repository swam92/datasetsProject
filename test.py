import random
from nltk.corpus import movie_reviews
from textblob.classifiers import NaiveBayesClassifier
random.seed(1)
 
train = [
    ('I love this sandwich.', 'pos'),
    ('This is an amazing place!', 'pos'),
    ('I feel very good about these beers.', 'pos'),
    ('This is my best work.', 'pos'),
    ("What an awesome view", 'pos'),
    ('I do not like this restaurant', 'neg'),
    ('I am tired of this stuff.', 'neg'),
    ("I can't deal with this", 'neg'),
    ('He is my sworn enemy!', 'neg'),
    ('My boss is horrible.', 'neg')
]
test = [
    ('The beer was good.', 'neg'),
    ('I do not enjoy my job', 'neg'),
    ("I ain't feeling dandy today.", 'neg'),
    ("I feel amazing!", 'pos'),
    ('Gary is a friend of mine.', 'pos'),
    ("I can't believe I'm doing this.", 'neg')
]
 
cl = NaiveBayesClassifier(train)
 
# Grab some movie review data
reviews = [(list(movie_reviews.words(fileid)), category)
              for category in movie_reviews.categories()
              for fileid in movie_reviews.fileids(category)]
random.shuffle(reviews)
new_train, new_test = reviews[0:100], reviews[101:200]
 
# Update the classifier with the new training data
cl.update(new_train)
 
# Compute accuracy
accuracy = cl.accuracy(test + new_test)
print("Accuracy: {0}".format(accuracy))
 
# Show 5 most informative features
cl.show_informative_features(10)