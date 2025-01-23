# q1.a
def linear_sum(x, result):
    # Base conditions.
    if result == 0:
        return True
    if x == []:
        return False
    
    # 2 recursive calls
    # 1- Check if the current x include x[0] much conditions  
    with_x0 = linear_sum(x[1:], result- x[0])
    # 2- Check if the current x exclude x[0] much conditions
    no_x0 = linear_sum(x[1:], result)
    #  If one of the recursive calls True, return true
    if with_x0 == True or no_x0 == True:
        return True
    else:
        return False
    
print(linear_sum([10,20], 0))

# q1.b
# function taking string and a char. If the char in the string, return sliced string without the char and one index after it.  
def return_sliced_str(str, char):
    # If char exist at x[0] in the current string return the sliced string. 
    if char in str[0]:
        return str[2:]
    # Continue look for the string 
    else: 
        return return_sliced_str(str[1:],char)
    
def ordered_subset(str1,str2):
    # Base conditions- if one of the strings eulas "" return True oor False respective to the ended string
    if str2== "":
        return True
    if str1 == "": 
        return False
    
    # start recursion, if str2[0] exists in str1 
    if(str2[0] in str1):
        return ordered_subset(return_sliced_str(str1, str2[0]), str2[1:])
    return False

# q2.a

# Unused function
# def find_max_from_list(lst):
#     if len(lst)!= 1:
#         if(lst[0]<=lst[1]):
#             lst = find_max_from_list(lst[1:])
#         else:
#             lst = [lst[0]] + lst[2:]
#             lst = find_max_from_list(lst)
#     return lst
   
# Unused function
# def find_zero_time_and_sum_grades(lst, grade):
#         # print("activate")
#         if len(lst) == 0:
#             return grade
#         if (lst[0])[0] == 0:
#             grade = grade + (lst[0])[1]
#         grade = find_zero_time_and_sum_grades(lst[1:], grade)
#         return grade

def solve_test(questions, total_time):
    # Define two variables 
    grade_with = 0
    grade_keeper = 0

    # Base conditions
    if len(questions) == 1 or  total_time <= 0:
        if len(questions)>1:
                grade_with=0
        else:
            if (questions[0])[0]<= total_time:
                grade_with = grade_with + (questions[0])[1]
        return grade_with
    
    if (questions[0])[0]<= total_time:
        grade_keeper = (questions[0])[1]
    
    #  Start recursion for checking maximal grade with current questions[0] 
    with_x0 = solve_test(questions[1:], total_time - (questions[0])[0])
    # Combining all variables collecting the current grade found with questions[0]
    grade_with = grade_keeper + with_x0 + grade_with
    #  Start recursion for checking maximal grade with current questions[0] 
    no_x0 = solve_test(questions[1:], total_time) 
    
    #  Compare the grades found with questions[0] and without, return the bigger one
    if grade_with > no_x0:
        return grade_with
    else:
        return no_x0 

# q2.b
# I wasn't sure if we can use floor so I built a basic one will floor the numbers we are checking in the question
def floor_half(num):
    if num - int(num) == 0.5:
        return int(num-0.5)
    else:
        return int(num)

# Warapper to solve the qustion
def solve_test_with_factor_helper(questions, total_time, index_to_change, grade_old):
    
    # Base condition
    if len(questions) == index_to_change:
        return grade_old
    
    # Check the original list to see if it can be the maximum 
    if index_to_change == -1:
        grade_new = solve_test(questions, total_time)
    else:
        # Change questions only for sending it to check
        fix_time = (questions[index_to_change])[0]
        (questions[index_to_change])[0]=0
        fix_grade =  (questions[index_to_change])[1]
        (questions[index_to_change])[1]= floor_half(((questions[index_to_change])[1])/2)
        grade_new = solve_test(questions, total_time)

    if grade_new > grade_old:
        grade_old = grade_new
    # Fixing questions for the next round    
    if index_to_change > -1:
        (questions[index_to_change])[0] = fix_time
        (questions[index_to_change])[1] = fix_grade

    return solve_test_with_factor_helper(questions, total_time, index_to_change+1, grade_old)

def solve_test_with_factor(questions, total_time):
    return solve_test_with_factor_helper(questions, total_time, -1, 0)  

# q3.a
# Wrapper for directory_depth
def directory_depth_helper(dir):
    dir_max_deep = 0
    # Base condition
    if not isinstance(dir, dict):
        return(0)
    # Starting recursion for every key in dir
    for key in dir.keys():
        key_dir_deep = directory_depth_helper(dir.get(key))+1
        # Check maximal dir deep
        if dir_max_deep < key_dir_deep:
            dir_max_deep = key_dir_deep
        key_dir_deep = 0
    
    return dir_max_deep

def directory_depth(dir):
    # Check if dir is a dictionary
    if not isinstance(dir, dict):
        raise TypeError("dir is not a dict")
    # Start recursion
    directory_depth = directory_depth_helper(dir) -1
    # Fix in case directory_depth is -1
    if directory_depth < 0:
        directory_depth = 0 
    return int(directory_depth)
    
# q3.b
def directory_music_size(dir,is_music=False):
    total_folder_size = 0
    # Base conditions
    if not isinstance(dir, dict):
        if  is_music==True:
            return dir
        else:
            return 0
    # Check if exists "music" in the folder's path or name 
    if is_music == True:
        
        for key in dir.keys():
            total_folder_size = directory_music_size(dir.get(key),True) + total_folder_size
    else:
    # Check if exists "music" in the inner folder's path or name 

        for key in dir.keys():
            if "music" in key:
                total_folder_size = directory_music_size(dir.get(key),True) + total_folder_size
            else:
                total_folder_size = directory_music_size(dir.get(key),False) + total_folder_size
    
    return total_folder_size

# q4.a
def distance(row1, col1, row2, col2):
    #  Finding the distance by average
    row_distance = row1 - row2 
    col_distance = col1 - col2
    # Do absolute to the outcome's value  
    if row_distance < 0:
        row_distance = row_distance*(-1)
    if col_distance < 0:
        col_distance = col_distance*(-1)

    return col_distance + row_distance

# q4.b
def add_tower(board, d, row, col):
    # start check only if d < len(board)
    if d < len(board):
        # Check if we can add the tower
        add_tower = True
        if row != 0:
            cut_board = board[0:row]
            for row_tower, col_tower in enumerate(cut_board):
               if d >= distance(row_tower, col_tower, row, col):
                    return False
        board[row]= col
        return True
    return False

# q4.c
# Wrapper for n_towers
def n_tower_helper(iteration_num, n, d, board, row ,col):
    # Base conditions
    if n == 0:
        return board
    
    #  Check if it is possible to locate the current checked tower. If so, locate it. Else, move forward one colum
    if add_tower(board, d, row, col):
        # board[row]= col
        col = 0 
        # Calling recursive helper
        outcome = n_tower_helper(iteration_num, n-1, d, board, row+1 ,col) 
        # If it is not possible to locate the tower, start iteration on the next colum 
    else:
        if col == len(board)-1:
            # If condition is "True", end the script and return "[]"
            if iteration_num == len(board)-1:
                return [] 
            # Check the last colum in row 0 for possible paths
            outcome = n_tower_helper(iteration_num+1, len(board), d, board, 0 ,iteration_num+1)
        else:
            # If it is not the last colum continue check the next colum
            outcome = n_tower_helper(iteration_num, n, d, board, row ,col+1) 

    return outcome
    
def n_towers(n, d):
    board = [0]
    board = board * n
    #  If distance is bigger than n return "[]"
    if d < n:
        return n_tower_helper(0, n, d, board, 0, 0)
    else:
        return []