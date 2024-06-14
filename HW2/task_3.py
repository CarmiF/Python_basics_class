import copy
# q1.a
def linear_sum(x, result):
    if result == 0:
        return True
    if x == []:
        return False
    
    with_x0 = linear_sum(x[1:], result- x[0])
    no_x0 = linear_sum(x[1:], result)
    
    if with_x0 == True or no_x0 == True:
        return True
    else:
        return False
    

# print(linear_sum( [1, 2, 3, 4, 5], 11))
# print("f")

# q1.b
def return_sliced_str(str, char):
    if char in str[0]:
        return str[2:]
    else: 
        return return_sliced_str(str[1:],char)
    
def ordered_subset(str1,str2):
    if str2== "":
        return True
    if str1 == "":
        return False
    
    if(str2[0] in str1):
        return ordered_subset(return_sliced_str(str1, str2[0]), str2[1:])
    return False

# q2.a
def find_max_from_list(lst):

    if len(lst)!= 1:
        if(lst[0]<=lst[1]):
            lst = find_max_from_list(lst[1:])
        else:
            lst = [lst[0]] + lst[2:]
            lst = find_max_from_list(lst)
    return lst
    # print(find_max_from_list([3,2,10,4,5,6]))

def find_zero_time_and_sum_grades(lst, grade):
        print("activate")
        if len(lst) == 0:
            return grade
        if (lst[0])[0] == 0:
            grade = grade + (lst[0])[1]
        grade = find_zero_time_and_sum_grades(lst[1:], grade)
        return grade

# print(find_zero_time_and_sum_grades([[0, 5], [20, 5], [10, 3]], 0))

def solve_test(questions, total_time):
    grade_with = 0
    grade_keeper = 0

    if len(questions) == 1 or  total_time <= 0:
        if len(questions)>1:
                # grade_with = grade_with +  find_zero_time_and_sum_grades(0, questions[1:])
                grade_with=0
        else:
            if (questions[0])[0]<= total_time:
                grade_with = grade_with + (questions[0])[1]
        # print(grade_with)
        return grade_with
    
    if (questions[0])[0]<= total_time:
        grade_keeper = (questions[0])[1]

    # print("grade kepper" + str(grade_keeper))
    # print(questions)
    with_x0 = solve_test(questions[1:], total_time - (questions[0])[0])
    grade_with = grade_keeper + with_x0 + grade_with
    no_x0 = solve_test(questions[1:], total_time) 

    # print(grade_with , no_x0)
    if grade_with > no_x0:
        return grade_with
    else:
        return no_x0 

# print(solve_test([[15, 10], [20, 5], [10, 3]], 25))


# q2.b
def floor_half(num):
    if num - int(num) == 0.5:
        return int(num-0.5)
    else:
        return int(num)
def solve_test_with_factor_helper(questions, total_time, index_to_change, grade_old):
    
    if len(questions) == index_to_change:
        return grade_old
    
    if index_to_change == -1:
        grade_new = solve_test(questions, total_time)
    else:
        fix_time = (questions[index_to_change])[0]
        (questions[index_to_change])[0]=0
        fix_grade =  (questions[index_to_change])[1]
        (questions[index_to_change])[1]= floor_half(((questions[index_to_change])[1])/2)
        grade_new = solve_test(questions, total_time)


    # print(questions_to_send, total_time)
    # print(grade_new)
    if grade_new > grade_old:
        grade_old = grade_new    
    if index_to_change > -1:
        (questions[index_to_change])[0] = fix_time
        (questions[index_to_change])[1] = fix_grade

    return solve_test_with_factor_helper(questions, total_time, index_to_change+1, grade_old)

def solve_test_with_factor(questions, total_time):
    return solve_test_with_factor_helper(questions, total_time, -1, 0)  

print(solve_test_with_factor([[10, 2], [20, 4], [30, 6]], 60))


# q3.a
def directory_depth_helper(dir):
    dir_max_deep = 0
    if not isinstance(dir, dict):
        return(0)

    for key in dir.keys():
        key_dir_deep = directory_depth_helper(dir.get(key))+1
        if dir_max_deep < key_dir_deep:
            dir_max_deep = key_dir_deep
        key_dir_deep = 0
    
    return dir_max_deep

def directory_depth(dir):
    if not isinstance(dir, dict):
        return("dir is not a dict")
    directory_depth = directory_depth_helper(dir) -1
    if directory_depth < 0:
        directory_depth = 0 
    return int(directory_depth)
    

# print(directory_depth({}))

# print(directory_depth({"a": 1, "b":2}))
# print(directory_depth({"c": {"a":1, "b":2}}))
# print(directory_depth({"c": {"a": 1, "b": 2}, "d": {"c": {"a": 1, "b": 2}, "b": 2}}))
# print(directory_depth({"a": {"a":1, "b":2}, "b":2}))

# q3.b
def directory_music_size(dir,is_music=False):
    total_folder_size = 0
    if not isinstance(dir, dict):
        if  is_music==True:
            return dir
        else:
            return 0
        
    if is_music == True:
        for key in dir.keys():
            total_folder_size = directory_music_size(dir.get(key),True) + total_folder_size
    else:
        for key in dir.keys():
            if "music" in key:
                total_folder_size = directory_music_size(dir.get(key),True) + total_folder_size
            else:
                total_folder_size = directory_music_size(dir.get(key),False) + total_folder_size
    
    return total_folder_size




# q4.a
def distance(row1, col1, row2, col2):
    row_distance = row1 - row2 
    col_distance = col1 - col2
    if row_distance < 0:
        row_distance = row_distance*(-1)
    if col_distance < 0:
        col_distance = col_distance*(-1)

    return col_distance + row_distance

# q4.b
def add_tower(board, d, row, col):
    if d< len(board):
        add_tower = True
        if row != 0:
            cut_board = board[0:row]
            for row_tower, col_tower in enumerate(cut_board):
                # print(distance(row_tower, col_tower, row, col))
                if d >= distance(row_tower, col_tower, row, col):
                    return False
        board[row]= col
        return True
    return False
# q4.c
def n_tower_helper(iteration_num, n, d, board, row ,col):
    if n == 0:
        return board
    # print(n, d, board, row ,col)
    # print(add_tower(board, d, row, col))
    if add_tower(board, d, row, col):
        board[row]= col
        col = 0 
        outcome = n_tower_helper(iteration_num, n-1, d, board, row+1 ,col)
    else:
        if col == len(board)-1:
            if iteration_num == len(board)-1:
                return [] 
            outcome = n_tower_helper(iteration_num+1, len(board), d, board, 0 ,iteration_num+1)
        else:
            outcome = n_tower_helper(iteration_num, n, d, board, row ,col+1) 

    return outcome
    

def n_towers(n, d):
    board = [0]
    board = board * n
    if d < n:
        return n_tower_helper(0, n, d, board, 0, 0)
    else:
        return []
       

# print(n_towers(4,2))
# input_list = [1,6,52,8]
# result = 3
# print(linear_sum(input_list, result)) 
# print(ordered_subset("ladbxcfe","abc"))