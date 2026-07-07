import nltk

def preprocess(text):

    tokens = nltk.word_tokenize(text)

    tokens = [word.lower() for word in tokens]

    return tokens