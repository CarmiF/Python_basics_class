import numpy as np
from OneHotEncoder import OneHotEncoder
from Vocabulary import Vocabulary
from BagOfWordsEncoder import BagOfWordsEncoder
 

        
def most_frequent_words(sentences):
    voc = Vocabulary(sentences)
    bag = BagOfWordsEncoder(voc)
    freq_vec = bag.calculate_word_frequency(sentences)
    max_value = np.max(freq_vec)
    # print(type(max_value))
    max_indices = list(np.where(freq_vec == max_value)[0])
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



def closest_sentences(sentences, vocabulary):
    pass


# print(most_frequent_words(["This is an example","The example is just study proposes.","Example is the best thing for practice!"]))
# ['example', 'is']
sentences = ["This is an example", "The example is just study proposes", "Example is the best thing for practice!"]
voc = Vocabulary(sentences)
print(voc.get_vocabulary())
print(cosine_similarity(sentences[0], sentences[1], voc))
# print(cosine_similarity(sentences[0], sentences[2], voc))
# print(cosine_similarity(sentences[1], sentences[2], voc))
# print(closest_sentences(sentences,voc))

# ['an', 'best', 'example', 'for', 'is', 'just', 'practice', 'proposes', 'study', 'the', 'thing', 'this']
# 0.4082
# 0.378
# 0.4629
# [1, 2]