# Functions

#Function getting a list of int veraibles and arrange it from big to small [biggest int,..., smallest int] 
def arrange_int_list_from_big_to_small(lst):
    # difine the finale list to return
    arranged_lst = []
    # Preapring list with "0" in ecah cell, they will be replaced in the original list's ints
    for i in lst:
        arranged_lst.append(0)

    # rank_counter- Counte how many numers are bigger in the list from the current checked number 
    rank_counter=0
    # item_fund- an indexed int in the original list
    for item_fund in lst:
        # item_chng- an indexed int in the original list
        for item_chng in lst:
            if item_fund< item_chng: 
                rank_counter = rank_counter + 1
        # the folloing while loop is checkining either there are doplicates numbers in the original list and if so, locate the item _fund that ranked in the next free cell 
        while arranged_lst[rank_counter] != 0:
            rank_counter = rank_counter + 1
        arranged_lst[rank_counter] = item_fund
        rank_counter = 0    
    return arranged_lst
    
def exercise_1():
    # preapering tuples for monthes we already knows how many days exists in
    month_with_31_days=(1,3,5,7,8,10,12)
    month_with_30_days=(4,6,9,11)
    # boll for the final answer
    valid_date = True
    # asking fir the input
    day = int(input("Enter a day:"))
    month = int(input("Enter a month:")) 
    year = int(input("Enter a year:"))
    # chock which category the input in.
    if(month in month_with_31_days):
        if(day>0 and day<32):
            print("The date is valid.")
            return
    if(month in month_with_30_days):
        if(day>0 and day<31):
            print("The date is valid.")
            return
    if(month == 2):
        # this if is intended to check rather the year is a leap year
        if((year % 400 == 0) or (year % 4 == 0 and year % 100 != 0) and day>0 and day<30):
            print("The date is valid.")
            return
    if (month==2 and day<29):
            print("The date is valid.")
            return    
    
    print("Invalid date.")

def exercise_2(n):
    # loop for printing each line
    for line in range(n):
        line_to_print = ""
        # loop for printing spaces
        for space in range(n-line-1):
            line_to_print = line_to_print + " "
        #  loop for printing "*"
        for stars in range(line+1):
            line_to_print = line_to_print + "* "
        print(line_to_print)

def exercise_3(n):
    # commentes in the functions
    find_next_bigger(find_bigger_primery(n))

# function takning an "int" and return the next bigger number which every number in it is bigger than the number as his left, as a list
def find_next_bigger(n):
    # final list to return
    n_list = []
    # bool, whemn true the number has found
    number_found=False
    #  loop loking for that number
    while number_found==False:
        number_found=True
        # adding 1 to the given number. Also increasing the number after it has been chacked.
        n = n + 1
        # Conveting n to list, so it will be easier to work with 
        n_list = number_to_list(n)
        # loop checking if eveary number in n_list follows the rule. if not, number_found will became False. 
        for i in range(len(n_list)-1):
            if(n_list[i]<n_list[i+1]):
                number_found=True
            else:
                number_found=False
                break             
    
    print("The first number with digits in ascending order as a List is: " + str(n_list))
    return n_list   

# Getting int return list in each cell one of the int's numbers. Exemple: input: 1023 output: [1,0,2,3]
def number_to_list(n):

    lst =[]
    while n!=0:
        lst.insert(0, int(n%10)) #% the input in to get the digit unit 
        n=(n - n%10)/10 # Subtract the digit unit and divide 10 to create new number witout the number already added to the list
    return lst

def find_bigger_primery(n):
    original_n=n # Veraible keeping the original n
    primery_number = False # Veraible indicates if the primery numeber has found
    while primery_number==False: 
        n=n+1 # Increse the input number in 1 as the requirments in the  mission
        # loop checking every number until n to find if there are two dividers differnt from 1 and n
        for i_fund in range(n): # first loop optional divider number one 
            for i_chng in range(n): # second loop optional divider number two 
                if((i_fund+2)*(i_chng+2) == n): # check if i_fund * i_chng equal n. start from 2 because 1 not count as a divider in the qustion 
                    n=n+1 # If dividers has been found move to the next number
                    i_fund=0. 
                    break
                if((i_fund+2)*(i_chng+2) > n): # If the * bigger than n, no need continue checking. 
                    break
        primery_number=True

    print("The first prime number greater than "+ str(original_n) + " is: "+ str(n))
    return int(n)

def exercise_4(triangle_sides_lst):
    # Put the sizes in veraibels
    big_side= triangle_sides_lst[0] 
    medium_side= triangle_sides_lst[1]
    small_side= triangle_sides_lst[2]
    
    # The folloing "if" conditions mention to check if the input matches the reqaierments
    # Check if there are 3 only sides in the input
    if len(triangle_sides_lst)!=3:
        print("Illegal triangle")
        return
    
    # Check if the input sizes are resonable in triangle
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
    # Loop asking for inputs, if the input meets the requrmenments, prints the "*" else asking for more inputes until 3.
    for i in range(3):
        n = int(input("Input number of rows (between 1 and 10): "))
        if(n<11 and n >0): # Check if the input between 1 to 10 
            exercise_2(n)
            break
        if(i==2): # If 3 tries failed print bye bye
            print("3 mistakes, Bye Bye!")
    
elif question == 3:
    n = int(input("Enter an integer: "))
    exercise_3(n)

elif question == 4:
    triangle_sides_lst = []
    triangle_sides_str = str(input("Enter 3 numbers:"))
    list_cell = 0
    number_collector = "" # Varaibels collects the chars between spacses
    for item in triangle_sides_str: # Loop dividing the input by spaces " " and create list of ints out of it. Example: input: 1 2 3 output [1,2,3]
        if item==" " and number_collector!="": # If the item in the input at the current index equls " " append the nuber collected from the input
            triangle_sides_lst.append(int(number_collector))
            number_collector = ""
        else:
            number_collector=number_collector + item #add the number to number_collector
    if number_collector!="": # Adding the last number to the list
        triangle_sides_lst.append(int(number_collector))
    triangle_sides_lst = arrange_int_list_from_big_to_small(triangle_sides_lst) #arrange the list from big  value to small value. 
    exercise_4(triangle_sides_lst)

