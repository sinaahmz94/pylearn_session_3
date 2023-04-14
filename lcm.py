number1 = int(input("please enter first number: "))
number2 = int(input("please enter second number: "))
for i in range(1 , (number1*number2) + 1):
    if i % number1 == 0 and i % number2 == 0:
        print("lcm is: ", i)