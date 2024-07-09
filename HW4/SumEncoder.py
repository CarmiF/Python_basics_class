from Vocabulary import Vocabulary
from OneHotEncoder import OneHotEncoder
import numpy as np
sumEncoder_ran_example = True
        


class SumEncoder(OneHotEncoder):
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
        print(indices)
        indices[indices == -1] = len((self.__vocabulary.get_vocabulary()))-1
        print(indices)

        # Create a mask to reset the modified rows back to their original form
        mask = np.arange(encoding.shape[1]) == indices[:, np.newaxis]
        print(mask)
        # Reset the modified_matrix using the mask
        original_matrix = mask.astype(int)
        print(original_matrix)
        sen = self.__oneHotEncoder.decode(original_matrix)

        return sen
    



    
sumEncoder_ran_example = True
if sumEncoder_ran_example == True:
    voc = Vocabulary(["The cat sat on the mat!", "The cat, Alexa, sat on the mat.", "The dog, Bob, sat on the log"])
    print(voc.get_vocabulary())
    sum_encoder = SumEncoder(voc)
    encoded = sum_encoder.encode("The dog Alexa, sat on Bob!")
    print(encoded)
    decoded = sum_encoder.decode(encoded)
    print(decoded)


# ['alexa', 'bob', 'cat', 'dog', 'log', 'mat', 'on', 'sat', 'the']
# [[1 1 1 1 1 1 1 1 1]
# [1 1 1 1 0 0 0 0 0]
# [1 0 0 0 0 0 0 0 0]
# [1 1 1 1 1 1 1 1 0]
# [1 1 1 1 1 1 1 0 0]
# [1 1 0 0 0 0 0 0 0]]
# the dog alexa sat on bob