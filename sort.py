user_array = []
i = 0
print("computer will recieve the numbers until you type 00")
while True:
    user_num = int(input("please enter number: "))   
    if user_num != 00:    
        user_array.append(user_num)
        print(user_array)
    else:
        print(user_array)
        break
while i < len(user_array):
    if(user_array[i] < user_array[i+1]):
        i = i + 1
        if i == len(user_array) - 1 :
            print(user_array)
            print("array is sorted")
    else:
        print(user_array)
        print("the array is not sorted")
        break


