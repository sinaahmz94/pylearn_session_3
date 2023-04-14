lenght = int(input("please enter the snake lenght: "))
for i in range(lenght) :
    if i % 2 == 0:
        print("*", end = " ")
    else:
        print("#", end = " ")        
