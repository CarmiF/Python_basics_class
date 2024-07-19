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
                

    def only_abc_remain(self, str1):
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
        str1 = str(list(sentence_words)).replace("]", "",1)
        str1 = str1.replace("[", "",1)
        str1 = str1.replace(",", "")
        str1 = str1.replace("'", "")


        return str1

class SumEncoder:
    def __init__(self, vocabulary):
        self.__vocabulary = vocabulary
        self.__oneHotEncoder = OneHotEncoder(self.__vocabulary)



    def encode(self, sentence):
        
        # Find indices of '1' in each row
        encoded_matrix = self.__oneHotEncoder.encode(sentence)
        indices = np.argmax(encoded_matrix, axis=1)

        # Create a mask to set all elements before '1' in each row to 1
        mask = np.arange(encoded_matrix.shape[1]) <= indices[:, np.newaxis]

        # Apply the mask to the original matrix
        modified_matrix = mask.astype(int)
        return modified_matrix

    def decode(self, encoding):
        # Find the indices where each row has the first '1'
        indices = np.argmax(encoding == 0, axis=1)-1
        # print(indices)
        indices[indices == -1] = len((self.__vocabulary.get_vocabulary()))-1
        # print(indices)

        # Create a mask to reset the modified rows back to their original form
        mask = np.arange(encoding.shape[1]) == indices[:, np.newaxis]
        # print(mask)
        # Reset the modified_matrix using the mask
        original_matrix = mask.astype(int)
        # print(original_matrix)
        sen = self.__oneHotEncoder.decode(original_matrix)

        return sen
    


class BagOfWordsEncoder:
    def __init__(self, vocabulary):
        self.__vocabulary = vocabulary


    def sentence_to_bag_of_words(self, sentence):
        tokenized_sentence = self.__vocabulary.tokenize(sentence)
        tokenized_sentence = (tokenized_sentence)
        voc = self.__vocabulary.get_vocabulary()
        
        
        if isinstance(sentence, list):
            for word in sentence:
                if not word in self.get_vocabulary():
                    raise ValueError("Not all words of the provided sentence are in vocabulary")
                    
        if isinstance(sentence, str):
            sentence_list = self.__vocabulary.tokenize(sentence)
            for word in sentence_list:
                if not word in self.__vocabulary.get_vocabulary():
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
        
        print(type(percentage_vec))
        return percentage_vec

        
def most_frequent_words(sentences):
    voc = Vocabulary(sentences)
    bag = BagOfWordsEncoder(voc)
    freq_vec = bag.calculate_word_frequency(sentences)
    max_value = np.max(freq_vec)
    # print(type(max_value))
    max_indices = (np.where(freq_vec == max_value)[0])
    # pr/int(type(max_indices))

    return voc[max_indices]



def cosine_similarity(sentence1, sentence2, vocabulary):
    bag = BagOfWordsEncoder(vocabulary)
    count_vec_sen1 = (bag.sentence_to_bag_of_words(sentence1))
    sen1_l2_norm =  np.linalg.norm(count_vec_sen1)
    count_vec_sen2 = (bag.sentence_to_bag_of_words(sentence2))
    sen2_l2_norm =  np.linalg.norm(count_vec_sen2)
    scalar_sen1_sen2= count_vec_sen1 * count_vec_sen2
    scalar_sen1_sen2_l2 = sen1_l2_norm * sen2_l2_norm
    return np.round(scalar_sen1_sen2/scalar_sen1_sen2_l2,4).sum()


def get_similarity(i, j, sentences, vocabulary):
    return cosine_similarity(sentences[int(i)], sentences[int(j)], vocabulary)

def closest_sentences(sentences, vocabulary):
    sentences_len = len(sentences)
    indices = np.indices((sentences_len, sentences_len))
    
    # Vectorize the get_similarity function
    vectorized_similarity = np.vectorize(lambda i, j: get_similarity(i, j, sentences, vocabulary))
    
    # Compute the similarity matrix
    similarities = vectorized_similarity(indices[0], indices[1])
    similarities[similarities >= 1] = 0

    # Find the maximum similarity and its indices
    max_similarity = np.max(similarities)
    max_indices = np.unravel_index(np.argmax(similarities, axis=None), similarities.shape)
    
    # Extract the sentences with the highest similarity
    sentence_pair = [sentences[max_indices[0]], sentences[max_indices[1]]]
    
    return list(max_indices)

# voc = Vocabulary(["The cat sat on the mat"])
# print(voc.get_vocabulary())

# voc.create_vocabulary(["The cat, Alexa, sat on the mat.", "The dog, Bob, sat on the log"])
# print(voc.get_vocabulary())

# voc.extend_vocabulary(["The cat sat on the mat"])
# print(voc.get_vocabulary())

# print(voc[2])
# print(voc[0])
# print(voc[3,7])
# print(voc["cat"])
# print(voc[["cat", "dog"]])
# print(voc[["cat", 5]])

# print(voc.tokenize("the dog, Alexa, sat on Bob!"))
# print(voc.tokenize("the dog, Alex, sat on the log"))

# # ['cat', 'mat', 'on', 'sat', 'the']
# # ['alexa', 'bob', 'cat', 'dog', 'log', 'mat', 'on', 'sat', 'the']
# # ['alexa', 'bob', 'cat', 'dog', 'log', 'mat', 'on', 'sat', 'the']
# # cat
# # alexa
# # ['dog', 'sat']
# # 2
# # [2, 3]
# # [2, 'mat']
# # ['the', 'dog', 'alexa', 'sat', 'on', 'bob']
# # None


# voc = Vocabulary(["The cat sat on the mat!", "The cat, Alexa, sat on the mat.", "The dog, Bob, sat on the log"])
# print(voc.get_vocabulary())
# one_hot_encoder = OneHotEncoder(voc)
# encoded = one_hot_encoder.encode("the dog, Alexa, sat on Bob!")
# print(encoded)
# decoded = one_hot_encoder.decode(encoded)
# print(decoded)

# # ['alexa', 'bob', 'cat', 'dog', 'log', 'mat', 'on', 'sat', 'the']
# # [[0 0 0 0 0 0 0 0 1]
# # [0 0 0 1 0 0 0 0 0]
# # [1 0 0 0 0 0 0 0 0]
# # [0 0 0 0 0 0 0 1 0]
# # [0 0 0 0 0 0 1 0 0]
# # [0 1 0 0 0 0 0 0 0]]
# # the dog alexa sat on bob

# voc = Vocabulary(["The cat sat on the mat!", "The cat, Alexa, sat on the mat.", "The dog, Bob, sat on the log"])
# print(voc.get_vocabulary())
# sum_encoder = SumEncoder(voc)
# encoded = sum_encoder.encode("The dog Alexa, sat on Bob!")
# print(encoded)
# decoded = sum_encoder.decode(encoded)
# print(decoded)


# # # ['alexa', 'bob', 'cat', 'dog', 'log', 'mat', 'on', 'sat', 'the']
# # # [[1 1 1 1 1 1 1 1 1]
# # # [1 1 1 1 0 0 0 0 0]
# # # [1 0 0 0 0 0 0 0 0]
# # # [1 1 1 1 1 1 1 1 0]
# # # [1 1 1 1 1 1 1 0 0]
# # # [1 1 0 0 0 0 0 0 0]]
# # # the dog alexa sat on bob

# print(most_frequent_words(["This is an example","The example is just study proposes.","Example is the best thing for practice!"]))
# # ['example', 'is']
# sentences = ["This is an example", "The example is just study proposes", "Example is the best thing for practice!"]


voc = Vocabulary(["The cat sat on the mat!", "The cat, Alexa, sat on the mat.", "The dog, Bob, sat on the log"])
print(voc.get_vocabulary()) 
bow = BagOfWordsEncoder(voc)
encoded = bow.sentence_to_bag_of_words("the dog, Alexa, sat on the log!")
print(encoded)
freq = bow.calculate_word_frequency(["the dog, Alexa, sat on the log!", "the cat Alexa", "Bob sat on log"])
print(freq)


# # # ['alexa', 'bob', 'cat', 'dog', 'log', 'mat', 'on', 'sat', 'the']
# # # [1 0 0 1 1 0 1 1 2]
# # # [14.2857 7.1429 7.1429 7.1429 14.2857 0. 14.2857 14.2857 21.4286]

# voc = Vocabulary(sentences)
# print(voc.get_vocabulary())
# print(cosine_similarity(sentences[0], sentences[1], voc))
# print(cosine_similarity(sentences[0], sentences[2], voc))
# print(cosine_similarity(sentences[1], sentences[2], voc))
# print(closest_sentences(sentences,voc))

# # # # ['an', 'best', 'example', 'for', 'is', 'just', 'practice', 'proposes', 'study', 'the', 'thing', 'this']
# # # # 0.4082
# # # # 0.378
# # # # 0.4629
# # # # [1, 2]