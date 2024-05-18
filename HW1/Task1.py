# Functions

def arrange_int_list_from_big_to_small(lst):
    arranged_lst = []
    rank_counter=0
    for i in lst:
        arranged_lst.append(0)
    for item_fund in lst:
        for item_chng in lst:
            if item_fund< item_chng:
                rank_counter = rank_counter + 1
        while arranged_lst[rank_counter] != 0:
            rank_counter = rank_counter + 1
        arranged_lst[rank_counter] = item_fund
        rank_counter = 0    
    return arranged_lst
    
def exercise_1():
    month_with_31_days=(1,3,5,7,8,10,12)
    month_with_30_days=(4,6,9,11)
    valid_date = True
    day = int(input("Enter a day:"))
    month = int(input("Enter a month:")) 
    year = int(input("Enter a year:"))
    if(month in month_with_31_days):
        if(day>0 and day<32):
            print("The date is valid.")
            return
    if(month in month_with_31_days):
        if(day>0 and day<31):
            print("The date is valid.")
            return
    if(month == 2):
        if((year % 400 == 0) or (year % 4 == 0 and year % 100 != 0) and day>0 and day<30):
            print("The date is valid.")
            return    
    print("Invalid date.")

def exercise_2(n):
    for line in range(n):
        line_to_print = ""
        for space in range(n-line-1):
            line_to_print = line_to_print + " "
        for stars in range(line+1):
            line_to_print = line_to_print + "* "
        print(line_to_print)

def exercise_3(n):
    find_next_bigger(find_bigger_primery(n))

def find_next_bigger(n):
    n_list = []
    number_found=False
    while number_found==False:
        number_found=True
        n = n + 1
        n_list = number_to_list(n)
        for i in range(len(n_list)-1):
            if(n_list[i]<n_list[i+1]):
                number_found=True
            else:
                number_found=False
                break             
    
    print("The first number with digits in ascending order as a List is: " + str(n_list))
    return n_list   

def number_to_list(n):

    lst =[]
    while n!=0:
        lst.insert(0, int(n%10))
        n=(n - n%10)/10
    return lst

def find_bigger_primery(n):
    original_n=n
    primery_number = False
    while primery_number==False:
        n=n+1
        for i_fund in range(n):
            for i_chng in range(n):
                if((i_fund+2)*(i_chng+2) == n):
                    n=n+1
                    i_fund=0
                    break
                if((i_fund+2)*(i_chng+2) > n):
                    break
        primery_number=True

    print("The first prime number greater than "+ str(original_n) + " is: "+ str(n))
    return int(n)

def exercise_4(triangle_sides_lst):
    
    big_side= triangle_sides_lst[0]
    medium_side= triangle_sides_lst[1]
    small_side= triangle_sides_lst[2]
    
    if len(triangle_sides_lst)!=3:
        print("Illegal triangle")
        return
    
    if medium_side+small_side<=big_side:
        print("Illegal triangle")
        return
    
    if ( big_side == medium_side == small_side):
        print("Equilateral","Acute")
        return ("Equilateral","Acute")
    
    if (big_side * big_side == small_side * small_side + medium_side * medium_side):
        if(big_side==medium_side or medium_side == small_side):
            print("Isosceles","Right")
            return("Isosceles","Right")
        else:
            print("Scalene","Right")
            return("Scalene","Right")
    
    if(medium_side == small_side):
        print("Isosceles","Obtuse")
        return("Isosceles","Obtuse")

    if(big_side==medium_side):
        print("Isosceles","Acute")
        return ("Isosceles","Acute")
    
    if(big_side/2<(medium_side+small_side)):
        print("Scalene","Obtuse")
        return ("Scalene","Obtuse")
    else:
        print ("Scalene","Obtuse")
        return ("Scalene","Obtuse")


# Display the menu
print("Question numbers:")
print("1. Exercise 1")
print("2. Exercise 2")
print("3. Exercise 3")
print("4. Exercise 4")

# Get user input for exercise choice
question = int(input("Enter your choice (1-4): "))
if question == 1:
    exercise_1()
elif question == 2:
    for i in range(3):
        n = int(input("Input number of rows (between 1 and 10): "))
        if(n<11 and n >0):
            exercise_2(n)
            break
        if(i==2):
            print("3 mistakes, Bye Bye!")
    
elif question == 3:
    n = int(input("Enter an integer: "))
    exercise_3(n)

elif question == 4:
    triangle_sides_lst = []
    triangle_sides_str = str(input("Enter 3 numbers:"))
    list_cell = 0
    number_collector = ""
    for item in triangle_sides_str:
        if item==" " and number_collector!="":
            triangle_sides_lst.append(int(number_collector))
            number_collector = ""
        else:
            number_collector=number_collector + item
    if number_collector!="": triangle_sides_lst.append(int(number_collector))
    triangle_sides_lst = arrange_int_list_from_big_to_small(triangle_sides_lst)
    exercise_4(triangle_sides_lst)

