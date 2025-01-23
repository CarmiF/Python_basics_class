"""Checking if a date is valid or not"""
def exercise_1():
    day = int(input("Enter a day:"))
    month = int(input("Enter a month:"))
    year = int(input("Enter a year:"))
    date_is_valid = True
    """Checking correctness of the month number"""
    if month < 1 or month > 12:
        date_is_valid = False
        print("Invalid date.")
        return
    if day>31 or day<1:
        date_is_valid = False
        print("Invalid date.")
        return
    """Checking the day number according to the proper days of each month"""
    if month in (1, 3, 5, 7, 8, 10, 12):
        if day <1 or day >31:
            date_is_valid = False
    elif month == 2:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            if day >= 30 or day <= 0:
                date_is_valid = False
        elif (day >= 29 or day <= 0):
            date_is_valid = False
    elif (day >30 or day <1):
        date_is_valid = False

    """Checking whether the date is valid or invalid according all conditions"""
    if date_is_valid:
        print("The date is valid.")
    else:
        print("Invalid date.")

"""Getting a row number and returning a pyramid"""
def exercise_2(row_number):
    """Checking whether row number is in range"""
    if not 1 <= row_number <= 10:
        """Giving two more chances to enter a proper number of rows"""
        for a in range(2):
            row_number = int(input("Input number of rows (between 1 and 10): "))
            if 1 <= row_number <= 10:
                break
    if row_number > 10 or row_number < 1:
        print("3 mistakes, Bye Bye!")
    else:
        """Printing a pyramid by given row number"""
        for i in range(1, row_number + 1):
            for j in range(1, row_number + 1 - i):
                print(" ", end="")
            for k in range(1, i + 1):
                print("*", end=" ")
            print()

"""Getting a number and returning the first bigger prime number"""
def exercise_3_1(random_num):
    optional_prime_num = int(random_num)
    is_prime_num = False
    if optional_prime_num + 1 == 2:
        is_prime_num = True
        optional_prime_num += 1
    while is_prime_num == 0:
        optional_prime_num += 1
        for i in range(2, (int(optional_prime_num ** 0.5)) + 2):
            if optional_prime_num % i == 0:
                is_prime_num = False
                break
            else:
                is_prime_num = True
    return optional_prime_num

"""Finding first ascending order number that larger than the first prime number and printing prime number and returning ascending list number"""
def exercise_3(random_num):
    optional_ascending_order_num = exercise_3_1(random_num)
    is_ascending_order = False
    if optional_ascending_order_num + 1 <= 9:
        is_ascending_order = True
        optional_ascending_order_num = str(optional_ascending_order_num + 1)
        num_len = 1
    while not is_ascending_order:
        optional_ascending_order_num = int(optional_ascending_order_num) + 1
        optional_ascending_order_num = str(optional_ascending_order_num)
        num_len = len(optional_ascending_order_num)
        for i in range(1, num_len):
            if optional_ascending_order_num[i - 1] >= optional_ascending_order_num[i]:
                is_ascending_order = False
                break
            else:
                is_ascending_order = True
    ascending_order_num =[int(optional_ascending_order_num[a]) for a in range(0,num_len)]
    print("The first prime number greater than %s is: %d" % (random_num, exercise_3_1(random_num)))
    return ascending_order_num

"""Getting 3 sides and returning triangle sides definition"""
def exercise_4_1(first_num, second_num, third_num):
    if first_num != second_num != third_num:
        return "Scalene"
    if first_num == second_num and second_num == third_num:
        return "Equilateral"
    else:
        return "Isosceles"

"""Getting 3 sides and checking angeles definitions"""
def exercise_4_2(first_num, second_num, third_num):
    first_num_sqr = first_num ** 2
    second_num_sqr = second_num ** 2
    third_num_sqr = third_num ** 2
    if first_num_sqr + second_num_sqr == third_num_sqr or first_num_sqr + third_num_sqr == second_num_sqr or second_num_sqr + third_num_sqr == first_num_sqr:
        return "Right"
    elif first_num_sqr + second_num_sqr > third_num_sqr and first_num_sqr + third_num_sqr > second_num_sqr and second_num_sqr + third_num_sqr > first_num_sqr:
        return "Acute"
    else:
        return "Obtuse"

"""Getting a string of 3 numbers, checking if it's possible to make a triangle, if possible checking triangle type"""
def exercise_4(sides_of_a_triangle):
    triangle_list = sides_of_a_triangle.split()
    first_num = int(triangle_list[0])
    second_num = int(triangle_list[1])
    third_num = int(triangle_list[2])
    if first_num + second_num <= third_num or second_num + third_num <= first_num or third_num + first_num <= second_num:
        return "Illegal triangle"
    triangle_type = (exercise_4_1(first_num, second_num, third_num), exercise_4_2(first_num, second_num, third_num))
    return triangle_type


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
    row_number = int(input("Input number of rows (between 1 and 10): "))
    exercise_2(row_number)
elif question == 3:
    random_num = input("Enter an integer: ")
    print("The first number with digits in ascending order as a List is: " + str(exercise_3(random_num)))

elif question == 4:
    size_of_sides = input("Enter 3 numbers:")
    print(exercise_4(size_of_sides))
else:
    print("Invalid choice.")



