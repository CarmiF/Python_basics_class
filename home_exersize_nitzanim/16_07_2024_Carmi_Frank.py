def q1():
    # counter = 1
    num = int(input("Enter a number:"))
    print((str(num)), end=" ")
    while num != 1:
        print("->", end=" ")
        if num%2 == 0:
            num = int(num/2) 
            print((str(num)), end=" ")
            # counter +=1 
        else:
            num = num*3+1
            print(str(num), end=" ")
            # counter +=1 
    print("-> Done")
    # print(counter)


# q1()

# while True:
#     num = int(input("Enter a number:"))
#     divider = 2
#     while divider < num//2 :
#         print(num % divider)
#         if num % divider == 0:
#             print ('False')
#             break
#         divider += 1
#     if num == 4:
#         print("False")
#     elif divider == num // 2 or num == 1 or num== 2 or num==3:
#         print('True')

# ********** Q3 ********** #
# class Store():
#     def __init__(self, store_name):
#         self.store_name = store_name
#     def get_store_name(self):
#         return self.store_name
#     def set_store_name(self, store_name):
#         self.store_name = store_name

# class Tolls(Store):
#     def __init__(self, name, price, target):
#         super().__init__(name)  
#         self.name = name
#         self.price = price
#         self.target = target
    
    
#     def get_toll_name(self):
#         return self.name
#     def get_target(self):
#         return self.target
#     def get_price(self):
#         return self.price
    
#     def set_toll_name(self, name):
#         self.name = name
#     def set_target(self, target):
#         self.target = target
#     def set_price(self, price):
#         self.price = price


# input_list = [
# ['Mona Lisa', 5341, 67],
# ['Starry night', 8908, 27],
# ['A girl with a pearl earring', 5914, 13],
# ['This Kiss', 3922, 20],
# ['Las Meninas', 5046, 61],
# ['birth of venus', 5576, 44],
# ['Guernica', 5627, 43],
# ['Arrangement in gray and black', 6680, 46],
# ['the night watch', 4361, 75],
# ['The Last Supper', 4907, 13],
# ['Sunrise impression', 3580, 68],
# ['Freedom leads the people', 5657, 20],
# ['The gypsy woman', 3862, 60],
# ['The sailors\' feast', 5332, 27],
# ['Night hawks', 4420, 44],
# ['The jellyfish raft', 7026, 71],
# ['the swing', 9594, 73],
# ['June flames', 9340, 69],
# ['son of man', 9847, 38],
# ['A storm in the Sea of Galilee', 7555, 56]
# ]
# input_list = [
# # ['Mona Lisa', 5341, 67],
# ['Starry night', 8908, 27],
# ['A girl with a pearl earring', 5914, 13],
# # ['This Kiss', 3922, 20],
# # ['Las Meninas', 5046, 61],
# # ['birth of venus', 5576, 44],
# # ['Guernica', 5627, 43],
# # ['Arrangement in gray and black', 6680, 46],
# # ['the night watch', 4361, 75],
# ['The Last Supper', 4907, 13],
# # ['Sunrise impression', 3580, 68],
# ['Freedom leads the people', 5657, 20],
# # ['The gypsy woman', 3862, 60],
# # ['The sailors\' feast', 5332, 27],
# # ['Night hawks', 4420, 44],
# # ['The jellyfish raft', 7026, 71],
# # ['the swing', 9594, 73],
# # ['June flames', 9340, 69],
# ['son of man', 9847, 38],
# ['A storm in the Sea of Galilee', 7555, 56]
# ]


# def wrapper_q4(input_list, money):
#     with_lst= []
#     no_lst =[]
#     if money <= 0:
#         return 0, [], 0
#     if money - int(input_list[0][1]) <= 0 or len(input_list) == 0:
#         return 0, [], money
#     if len(input_list) == 1:
#         return input_list[0][2], input_list, money - int(input_list[0][1])
    
#     # print(money)
#     people_amount_return, with_lst, money_remain_with = wrapper_q4(input_list[1:], money- int(input_list[0][1]))
    
#     people_amount_with = people_amount_return + input_list[0][2]
#     with_lst.append(input_list[0][0])
#     if  money_remain_with == 0:
#         money_remain_with = money
    
#     people_amount_no, no_lst, money_remain_no = wrapper_q4(input_list[1:], money)
#     if money_remain_no == 0:
#         money_remain_no = money

#     if people_amount_with > people_amount_no:
#         # print(with_lst)
#         return people_amount_with, with_lst, money_remain_with
#     else:
#         # print(no_lst)

#         return people_amount_no, no_lst, money_remain_no
    
# def q4(input_list, money):
#     people_amount, output_lst, money_remain = wrapper_q4(input_list,money)
#     print(output_lst)

#     print(f"Tomer bought {str(len(output_lst))} pictures")
#     print("Total "+ str(people_amount) + " people came")
#     money_lst = output_lst[1::3]
#     print("The budjet left to Tomer is "+ str(money_remain))

# q4(input_list, 80000)

# counter = 1

# matrix = [[0]*12 for a in range(12)]
# for col in range(12):
#     for row in range(12):
#         matrix[col][row] = counter
#         counter += 1
# print(matrix)

# for row in range(12):
#     for col in range(12):
#         matrix[col][row] = counter
#         counter += 1
# סיבוב בכיוון השעון
def rotate_clockwise(submatrix):
    return [
        [submatrix[1][0], submatrix[0][0]],
        [submatrix[1][1], submatrix[0][1]]
    ]

# # סיבוב נגד כיוון השעון
def rotate_counter_clockwise(submatrix):
    return [
        [submatrix[0][1], submatrix[1][1]],
        [submatrix[0][0], submatrix[1][0]]
    ]



def q2():
    # חלק 1: יצירת מטריצה בגודל 12x12 עם המספרים מ-1 עד 144
    matrix = []
    n = 12

    # יצירת המטריצה
    for i in range(n):
        row = []
        for j in range(n):
            # חישוב הערך הנכון לתא הנוכחי
            value = i * n + j + 1
            row.append(value)
        matrix.append(row)

    # הדפסת המטריצה
    print("The Matrix:")
    for row in matrix:
        print(row)

    
    # הגדרת מיקומים לסיבובים בכיוון השעון (ירוק)
    green_rotations = [(i, j) for i in range(0, n-1, 2) for j in range(0, n-1, 4)]
    # print(green_rotations)
    # הגדרת מיקומים לסיבובים נגד כיוון השעון (כתום)
    orange_rotations = [(i, j) for i in range(0, n-1, 2) for j in range(2, n-1, 4)]

    # סיבוב המטריצה
    for i, j in green_rotations:
        # יצירת תת-מטריצה לסיבוב
        submatrix = [matrix[i][j:j+2], matrix[i+1][j:j+2]]
        # print(submatrix)
        # סיבוב תת-המטריצה
        rotated = rotate_clockwise(submatrix)
        # print(rotated)
        # עדכון המטריצה המקורית
        matrix[i][j:j+2] = rotated[0]
        matrix[i+1][j:j+2] = rotated[1]

    for i, j in orange_rotations:
        # יצירת תת-מטריצה לסיבוב
        submatrix = [matrix[i][j:j+2], matrix[i+1][j:j+2]]
        # סיבוב תת-המטריצה
        rotated = rotate_counter_clockwise(submatrix)
        # עדכון המטריצה המקורית
        matrix[i][j:j+2] = rotated[0]
        matrix[i+1][j:j+2] = rotated[1]

    # הדפסת המטריצה לאחר הסיבובים
    print("The rotated Matrix:")
    for row in matrix:
        print(row)

    for i in range(0, n-1, 4):
        for j in range(0, n-1, 4):
            submatrix_1 =[matrix[i][j:j+2], matrix[i+1][j:j+2]]
            submatrix_2 = [matrix[i+2][j+2:j+4], matrix[i+3][j+2:j+4]]
            matrix[i][j:j+2] = submatrix_2[0]
            matrix[i+1][j:j+2] = submatrix_2[1]
            matrix[i+2][j+2:j+4] = submatrix_1[0]
            matrix[i+3][j+2:j+4] = submatrix_1[1]

    for row in range(0, n-1, 4):
        for col in range(2, n-1, 4):
            submatrix_upper =[matrix[row][col:col+2], matrix[row+1][col:col+2]]
            # print(submatrix_upper)
            submatrix_buttom = [matrix[row+2][col-2:col], matrix[row+3][col-2:col]]
            # print(submatrix_buttom)

            matrix[row][col:col+2] = submatrix_buttom[0]
            matrix[row+1][col:col+2] = submatrix_buttom[1]
            matrix[row+2][col-2:col] = submatrix_upper[0]
            matrix[row+3][col-2:col] = submatrix_upper[1]
    

    # הדפסת המטריצה לאחר הסיבובים
    print("The transformed Matrix:")
    for row in matrix:
        print(row)





q2()