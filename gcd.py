number1_divisor = []
number2_divisor = []
common_divisors = []
number1 = int(input("please enter the first number: "))
number2 = int(input("please enter the second number: "))
for i in range(number1):
    if number1 % (i + 1) == 0:
        number1_divisor.append(i + 1)
for i in range(number2):
    if number2 % (i + 1) == 0:
        number2_divisor.append(i + 1) 
print(number1_divisor)
print(number2_divisor)        

for x in number1_divisor:
    if x in number2_divisor:
        common_divisors.append(x)
print("common divisors are: ", common_divisors) 
print("gcd is:", max(common_divisors))       