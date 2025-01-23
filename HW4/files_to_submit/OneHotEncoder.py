from Vocabulary import Vocabulary
import numpy as np

class OneHotEncoder:
    def __init__(self, vocabulary):
        self.__vocabulary = vocabulary
        

    def encode(self, sentence):
        tokenized_sentence = self.__vocabulary.tokenize(sentence)
    
        arr1 = np.array(tokenized_sentence)
        arr2 = np.array(self.__vocabulary.get_vocabulary())
        arr1 =arr1[:, np.newaxis]
        mask = (arr1 == arr2)
        return mask.astype(int)

    def decode(self, encoding):
        mask = np.argmax(encoding, axis=1)
        # Extract words using the mask
        sentence_words = np.take(self.__vocabulary.get_vocabulary(), mask)
        # print(sentence_words)


OneHotEncoderne_hot_encoder = False
if OneHotEncoderne_hot_encoder == True:
    voc = Vocabulary(["The cat sat on the mat!", "The cat, Alexa, sat on the mat.", "The dog, Bob, sat on the log"])
    print(voc.get_vocabulary())
    one_hot_encoder = OneHotEncoder(voc)
    encoded = one_hot_encoder.encode("the dog, Alexa, sat on Bob!")
    print(encoded)
    decoded = one_hot_encoder.decode(encoded)
    print(decoded)

# ['alexa', 'bob', 'cat', 'dog', 'log', 'mat', 'on', 'sat', 'the']
# [[0 0 0 0 0 0 0 0 1]
# [0 0 0 1 0 0 0 0 0]
# [1 0 0 0 0 0 0 0 0]
# [0 0 0 0 0 0 0 1 0]
# [0 0 0 0 0 0 1 0 0]
# [0 1 0 0 0 0 0 0 0]]
# the dog alexa sat on bob