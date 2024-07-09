import numpy as np


class Vocabulary:
    def __init__(self, sentences=None):
        self.__vocabulary_list = self.sentences_to_one_clean_list(sentences)

            
            

    def __len__(self):
        return len(self.__vocabulary_list)
        

    def create_vocabulary(self, sentences):
        self.__vocabulary_list = []
        self.__init__(sentences)


    def extend_vocabulary(self, new_sentences):
        new_sentences_list = self.sentences_to_one_clean_list(new_sentences)
        new_voc_list = sorted(new_sentences_list + self.__vocabulary_list)
        end_voc_list = []
        for word in new_voc_list: 
            if not word in end_voc_list: 
                end_voc_list.append(word)
           
        self.__vocabulary_list = end_voc_list
        
        # for word in new_vocabulary_list:
        #     if not word in self.__vocabulary_list:
        #         self.__vocabulary_list.append(word)
        # self.__vocabulary_list = sorted(self.__vocabulary_list)
    
    def tokenize(self, sentence):
        pass

    def get_vocabulary(self):
        return self.__vocabulary_list
    
    def __getitem__(self, key):
        if isinstance(key,int):
            return self.__vocabulary_list[key]
        if isinstance(key,tuple):
            items_list = []
            for num in key:
                items_list.append(self.__vocabulary_list[num])
            return items_list
        if isinstance(key,str):
            return self.__vocabulary_list.index(key)
        if isinstance(key,list):
            result_list = []
            for item in key:
                result_list.append(self[item])
            return result_list
                

       
    
    def sentences_to_one_clean_list(self, sentences):
        new_vocabulary_str = str(sentences).lower()
        # print(new_vocabulary_str)

        for char in new_vocabulary_str:
                if not "a" <= char <= "z":
                    new_vocabulary_str = new_vocabulary_str.replace(char, " ", 1)
        # print(new_vocabulary_str)

        new_vocabulary_list = sorted(new_vocabulary_str.split())

        end_vocabulary_list = []
        for i, word in enumerate(new_vocabulary_list):
            if i < len(new_vocabulary_list): 
                if not word in end_vocabulary_list:
                    end_vocabulary_list.append(word)
        
        return end_vocabulary_list

        

class OneHotEncoder:
    def __init__(self, vocabulary):
        pass

    def encode(self, sentence):
        pass

    def decode(self, encoding):
        pass


class SumEncoder:
    def __init__(self, vocabulary):
        pass

    def encode(self, sentence):
        pass

    def decode(self, encoding):
        pass


class BagOfWordsEncoder:
    def __init__(self, vocabulary):
        pass

    def sentence_to_bag_of_words(self, sentence):
        pass

    def calculate_word_frequency(self, sentences):
        pass


def most_frequent_words(sentences):
    pass


def cosine_similarity(sentence1, sentence2, vocabulary):
    pass


def closest_sentences(sentences, vocabulary):
    pass

voc = Vocabulary(["The cat sat on the mat"])
print(voc.get_vocabulary())

voc.create_vocabulary(["The cat, Alexa, sat on the mat.", "The dog, Bob, sat on the log"])
print(voc.get_vocabulary())

voc.extend_vocabulary(["The cat sat on the mat"])
print(voc.get_vocabulary())

print(voc[2])
print(voc[0])
print(voc[3,7])
print(voc["cat"])
print(voc[["cat", "dog"]])
print(voc[["cat", 5]])

# print(voc.tokenize("the dog, Alexa, sat on Bob!"))
# print(voc.tokenize("the dog, Alexa, sat on the log"))

# ['cat', 'mat', 'on', 'sat', 'the']
# ['alexa', 'bob', 'cat', 'dog', 'log', 'mat', 'on', 'sat', 'the']
# ['alexa', 'bob', 'cat', 'dog', 'log', 'mat', 'on', 'sat', 'the']
# cat
# alexa
# ['dog', 'sat']
# 2
# [2, 3]
# [2, 'mat']
# ['the', 'dog', 'alexa', 'sat', 'on', 'bob']
# None