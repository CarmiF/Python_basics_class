arr1 = [1,2,3,4,5,6,7,8]
arr2 = [8,7,6,5,4,3,2,1]
SIZE = 8

four_div_1 = []
four_div_2 = []

for i in range(SIZE):
    four_div_1.append((-1)*int(arr1[i]%4 != 0))
    four_div_2.append((-1)*int(arr2[i]%4 != 0))

print(four_div_1)
print(four_div_2)
