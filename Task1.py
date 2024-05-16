# Functions
def exercise_1():
    month_with_31_days=(1,3,5,7,8,10,12)
    month_with_30_days=(4,6,9,11)
    valid_date = True
    day = int(input("Enter a day:"))
    month = int(input("Enter a month:")) 
    year = int(input("Enter a year:"))
    if(month in month_with_31_days):
        if(day>0 and day<32):
            print("Valid date.")
            return
    if(month in month_with_31_days):
        if(day>0 and day<31):
            print("Valid date.")
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

def exercise_3(arg):
    print("hello3")
def exercise_4(arg):
    print("hello4")



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
    pass

elif question == 4:
    pass

else:
    print("Invalid choice.")
