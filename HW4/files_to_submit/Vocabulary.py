voc_ran_example = False
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
        
    def tokenize(self, sentence):
        new_sen_str  = str(sentence).lower()

        for char in new_sen_str:
                if not char.isalpha():
                    new_sen_str = new_sen_str.replace(char, " ", 1)
        
        new_sen_lst = new_sen_str.split()
        for word in new_sen_lst:
            if not word in self.__vocabulary_list:
                return None
        
        return new_sen_lst

    def get_vocabulary(self):
        return self.__vocabulary_list
    
    def __getitem__(self, key):
        if isinstance(key,int) or isinstance(key,np.int64) or isinstance(key,np.int32):
            if len(self.__vocabulary_list) > key:
                return self.__vocabulary_list[key]
            else: 
                raise IndexError("Index is out of range")
        if isinstance(key,tuple):
            items_list = []
            for num in key:
                items_list.append(self.__vocabulary_list[num])
            return items_list
        if isinstance(key,str):
            if key in self.__vocabulary_list:
                return self.__vocabulary_list.index(key)
            else:
                raise ValueError("Word is not in vocabulary")

        if isinstance(key,list):
            result_list = []
            for item in key:
                result_list.append(self[item])
            return result_list
                

    def only_abc_remain(str1):
        str1 = str1.lower()
        for char in str1:
            if not char.isalpha():
                str1 = str1.replace(char, " ", 1)
        return str1
    
    def contain(self, key):
       
        if isinstance(key, list):
            for word in key:
                if not word in self.get_vocabulary():
                    print(word + " is not in vocabulary")
                    return False
                    
            return True
        if isinstance(key, str):
            self.contain(self.tokenize(key))
        return None
        
    

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
    





    


if voc_ran_example == True:
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

    print(voc.tokenize("the dog, Alexa, sat on Bob!"))
    print(voc.tokenize("the dog, Alex, sat on the log"))

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
