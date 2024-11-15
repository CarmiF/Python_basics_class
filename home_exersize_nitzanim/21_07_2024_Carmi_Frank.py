# ********** Q1 **********

def q1():
    # Asking to input number
    num = int(input("Enter a number:"))
    # Print the input number
    print((str(num)), end=" ")
    
    # While num is not == 1 continue with the algorithm
    while num != 1:
        # Print the arrow between numbers
        print("->", end=" ")
        # Check if number can be divided by 2
        if num%2 == 0:
            # Dividing the number in 2
            num = int(num/2) 
            print((str(num)), end=" ")
        # If it can't be divided multiply the number in 3 and add 1
        else:
            num = num*3+1
            print(str(num), end=" ")
    print("-> Done")

# ********** Q2 **********
def q2():
    # This part of the code is for part 1 of the mission

    # Defining matrix   
    matrix = []
    #  Defining matrix size
    n = 12
    # Building the initial matrix
    for i in range(n):
        # Adding new row for every iteration   
        row = []
        # Adding each colum value as requested
        for j in range(n):
            value = i * n + j + 1
            row.append(value)
        # Adding the new raw to the matrix
        matrix.append(row)

    # This part of the code is for part 2 of the mission

    #  Determining coordinates for submatrixws to be rotated clockwise
    green_rotations = [(i, j) for i in range(0, n-1, 2) for j in range(0, n-1, 4)]
    #  Determining coordinates for submatrixws to be rotated non clockwise
    orange_rotations = [(i, j) for i in range(0, n-1, 2) for j in range(2, n-1, 4)]

    #  Iterating all coordinates and change matrix accordingly
    for i, j in green_rotations:
        # Add the matrix to be rotate to submatrix 
        submatrix = [matrix[i][j:j+2], matrix[i+1][j:j+2]]
        #  Rotating the submatrix
        rotated = rotate_clockwise(submatrix)

        # Changing the matrix accordingly
        matrix[i][j:j+2] = rotated[0]
        matrix[i+1][j:j+2] = rotated[1]

    for i, j in orange_rotations:
        # Add the matrix to be rotate to submatrix 

        submatrix = [matrix[i][j:j+2], matrix[i+1][j:j+2]]
        #  Rotating the submatrix
        submatrix = rotate_counter_clockwise(submatrix)
        # Changing the matrix accordingly
        matrix[i][j:j+2] = submatrix[0]
        matrix[i+1][j:j+2] = submatrix[1]

    # This part of the code is for part 3 of the mission
    for i in range(0, n-1, 4):
        for j in range(0, n-1, 4):
            # Saving the matrixes to be replaced in 2 variables
            submatrix_1 =[matrix[i][j:j+2], matrix[i+1][j:j+2]]
            submatrix_2 = [matrix[i+2][j+2:j+4], matrix[i+3][j+2:j+4]]
            # Updating the main matrix
            matrix[i][j:j+2] = submatrix_2[0]
            matrix[i+1][j:j+2] = submatrix_2[1]
            matrix[i+2][j+2:j+4] = submatrix_1[0]
            matrix[i+3][j+2:j+4] = submatrix_1[1]

    for i in range(0, n-1, 4):
        for j in range(2, n-1, 4):
            # Saving the matrixes to be replaced in 2 variables
            submatrix_1 =[matrix[i][j:j+2], matrix[i+1][j:j+2]]
            submatrix_2 = [matrix[i+2][j-2:j], matrix[i+3][j-2:j]]
            # Updating the main matrix

            matrix[i][j:j+2] = submatrix_2[0]
            matrix[i+1][j:j+2] = submatrix_2[1]
            matrix[i+2][j-2:j] = submatrix_1[0]
            matrix[i+3][j-2:j] = submatrix_1[1]
    

    # This part of the code is for answering the questions

    # Q2A
    # Sum of the numbers in col(defined below)
    col = 8
    counter = 0
    for row in range(0,n-1,1):
        counter += matrix[row][col]
    print("Q2A = " + str(counter))

    # Q2B
    # What row num(defined below) is
    num = 89
    for row in range(0, n-1, 1):
        for col in range(2, n-1, 1):
            if matrix[row][col]== num:
                print("Q2B = "+ str(row))
                break


    # Q2C 
    #  What is the biggest number divide in divider in raw(raw and divider defined below)
    divider = 7
    row = 7 
    answer = 0
    for col in range(0, n-1, 1):
        if matrix[row][col]%7 == 0:
            if  matrix[row][col] >answer:
                answer = matrix[row][col] 
        
    if answer == 0:
        pass
    else:
        print("Q2C = "+ str(answer))

"""
Helper functions for question 2 will be written here.
"""
def rotate_clockwise(submatrix):
    return [
        [submatrix[1][0], submatrix[0][0]],
        [submatrix[1][1], submatrix[0][1]]
    ]

def rotate_counter_clockwise(submatrix):
    return [
        [submatrix[0][1], submatrix[1][1]],
        [submatrix[0][0], submatrix[1][0]]
    ]

 

# ********** Q3 ********** #
# Defining Store class
class Store():
    def __init__(self, store_name):
        self.store_name = store_name
    def get_store_name(self):
        return self.store_name
    def set_store_name(self, store_name):
        self.store_name = store_name

# Defining Tolls class, inherited from Store
class Tolls(Store):
    def __init__(self, name, price, target):
        super().__init__(name)  
        self.name = name
        self.price = price
        self.target = target
    
    def get_toll_name(self):
        return self.name
    def get_target(self):
        return self.target
    def get_price(self):
        return self.price
    
    def set_toll_name(self, name):
        self.name = name
    def set_target(self, target):
        self.target = target
    def set_price(self, price):
        self.price = price



# ********** Q4 **********

input_list = [
['Mona Lisa', 5341, 67],
['Starry night', 8908, 27],
['A girl with a pearl earring', 5914, 13],
['This Kiss', 3922, 20],
['Las Meninas', 5046, 61],
['birth of venus', 5576, 44],
['Guernica', 5627, 43],
['Arrangement in gray and black', 6680, 46],
['the night watch', 4361, 75],
['The Last Supper', 4907, 13],
['Sunrise impression', 3580, 68],
['Freedom leads the people', 5657, 20],
['The gypsy woman', 3862, 60],
['The sailors\' feast', 5332, 27],
['Night hawks', 4420, 44],
['The jellyfish raft', 7026, 71],
['the swing', 9594, 73],
['June flames', 9340, 69],
['son of man', 9847, 38],
['A storm in the Sea of Galilee', 7555, 56]
]

def q4(input_list, money):
    # Sending the input to helper function will return output as required
    people_amount, output_lst, money_remain = helper_q4(input_list,money)

    # Answering the questions
    print(f"Q4A = {str(len(output_lst))}")
    print("Q4B = "+ str(people_amount))
    print("Q4C = "+ str(money_remain))


"""
Helper functions for question 4 will be written here.
"""
def helper_q4(input_list, money):

    with_lst= []
    no_lst =[]
    # If money is <= 0 stop recursion and start return 
    if money <= 0:
        return 0, [], 0
    if money - int(input_list[0][1]) <= 0 or len(input_list) == 0:
        return 0, [], money
    # if len of input_list is one return the values of the last picture
    if len(input_list) == 1:
        return input_list[0][2], input_list, money - int(input_list[0][1])
    # Start recursion with the current picture
    people_amount_return, with_lst, money_remain_with = helper_q4(input_list[1:], money- int(input_list[0][1]))
    # Updating the current data according to the data returned 
    people_amount_with = people_amount_return + input_list[0][2]
    with_lst.append(input_list[0][0])
    if  money_remain_with == 0:
        money_remain_with = money
    
    # Start recursion without the current picture
    people_amount_no, no_lst, money_remain_no = helper_q4(input_list[1:], money)
    # Updating the current data according to the data returned 
    if money_remain_no == 0:
        money_remain_no = money
    
    # Compare which list contain bigger number of people, and return the bigger one
    if people_amount_with > people_amount_no:
        return people_amount_with, with_lst, money_remain_with
    else:

        return people_amount_no, no_lst, money_remain_no
    





# Call the functions
# q1()
# q2()
# q4(input_list, 80000)
