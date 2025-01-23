from Vocabulary import Vocabulary
from OneHotEncoder import OneHotEncoder
from SumEncoder import SumEncoder
import numpy as np
class BagOfWordsEncoder:
    def __init__(self, vocabulary):
        self.__vocabulary = vocabulary


    def sentence_to_bag_of_words(self, sentence):
        tokenized_sentence = self.__vocabulary.tokenize(sentence)
        tokenized_sentence = (tokenized_sentence)
        voc = self.__vocabulary.get_vocabulary()
        if self.__vocabulary.contain(sentence):
            raise ValueError("Not all words of the provided sentence are in vocabulary")
        count_vec = np.zeros(len(voc), dtype=np.int32)
        for i, word in enumerate(voc):
            count = tokenized_sentence.count(word)
            count_vec[i] = count
        self.count_vec = count_vec
        return count_vec
        
        

    def calculate_word_frequency(self, sentences):
        count_vec = np.zeros(len(self.__vocabulary), dtype=np.int32)
        percentage_vec = np.zeros(len(self.__vocabulary), dtype=np.float32)
        for one_sen in sentences:
            count_vec += self.sentence_to_bag_of_words(one_sen)
            # print(count_vec)
        
        total_words_amount = count_vec.sum()
        # print(total_words_amount)
        for i,dim in enumerate(count_vec):
            percentage_vec[i] =np.round((dim/total_words_amount)*100, 4)
        # print(percentage_vec.sum())
        self.percentage_vec = percentage_vec
        return percentage_vec

        


bagOfWords_tester =False
if bagOfWords_tester == True:
    voc = Vocabulary(["The cat sat on the mat!", "The cat, Alexa, sat on the mat.", "The dog, Bob, sat on the log"])
    print(voc.get_vocabulary()) 
    bow = BagOfWordsEncoder(voc)
    encoded = bow.sentence_to_bag_of_words("the dog, Alexa, sat on the log!")
    print(encoded)
    freq = bow.calculate_word_frequency(["the dog, Alexa, sat on the log!", "the cat Alexa", "Bob sat on log"])
    print(freq)


    # ['alexa', 'bob', 'cat', 'dog', 'log', 'mat', 'on', 'sat', 'the']
    # [1 0 0 1 1 0 1 1 2]
    # [14.2857 7.1429 7.1429 7.1429 14.2857 0. 14.2857 14.2857 21.4286]