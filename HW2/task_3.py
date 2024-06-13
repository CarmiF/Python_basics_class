# q1.a


def linear_sum(x, result):
    if x == []:
        return False
    if result == 0:
        return True
    
    with_x0 = linear_sum(x[1:], result- x[0])
    if with_x0 == True:
        return True
    else:
        no_x0 = linear_sum(x[1:], result)
    return no_x0


# q1.b
def return_sliced_str(str, char):
    if char in str:
        if char in str[0]:
            return str
        else: 
            return return_sliced_str(str[1:],char)
    else:
        return False

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

def solve_test(questions, total_time):
    grade_with = 0
    grade_keeper = 0
    if len(questions)==0:
        return grade_with
    if total_time < 0:
        return grade_with
    
    if (questions[0])[0]<= total_time:
        grade_keeper = (questions[0])[1]
    with_x0 = solve_test(questions[1:], total_time - (questions[0])[0])
    grade_with = grade_keeper + with_x0
    no_x0 = solve_test(questions[1:], total_time) 
    
    if grade_with > no_x0:
        return grade_with
    else:
        return no_x0 
    


# q2.b

def floor_half(num):
    if num - int(num) == 0.5:
        return num-0.5
    else:
        return num

def solve_test_with_factor_helper(questions, total_time, index_to_change, grade_old):
    
    if len(questions) == index_to_change:
        return grade_old
    questions_to_send = questions
    (questions_to_send[index_to_change])[0]=0

    (questions_to_send[index_to_change])[1]= floor_half(((questions[index_to_change])[1])/2)
    grade_new = solve_test(questions_to_send, total_time)
    if grade_new > grade_old:
        grade_old = grade_new    
    return solve_test_with_factor_helper(questions, total_time, index_to_change+1, grade_old)
    


def solve_test_with_factor(questions, total_time):
    return solve_test_with_factor_helper(questions, total_time, 0, 0)
    
# print(solve_test_with_factor([[20,5], [40,9] ,[35,8] ,[35,7]], 55))

# q3.a
def directory_depth(dir):
    # Delete the pass command and insert you code below
    pass

# q3.b
def directory_music_size(dir,is_music=False):
    # Delete the pass command and insert you code below
    pass

# q4.a
def distance(row1, col1, row2, col2):
    # Delete the pass command and insert you code below
    pass

# q4.b
def add_tower(board, d, row, col):
    # Delete the pass command and insert you code below
    pass

# q4.c
def n_towers(n, d):
    # Delete the pass command and insert you code below
    pass


# input_list = [1,6,52,8]
# result = 3
# print(linear_sum(input_list, result)) 
# print(ordered_subset("ladbxcfe","abc"))