numbers = []
while True:
    user_num = int(input("please enter the number: "))
    if user_num not in numbers:
        numbers.append(user_num)
        print(numbers)
    else:
        print("lotfan adad tekrari vared nakonid")    