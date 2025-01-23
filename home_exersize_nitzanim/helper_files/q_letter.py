while True:
    num = int(input("Enter a number:"))
    divider = 2
    while divider < num//2 :
        print(num % divider)
        if num % divider == 0:
            print ('False')
            break
        divider += 1
    if num == 4:
        print("False")
    elif divider == num // 2 or num == 1 or num== 2 or num==3:
        print('True')
