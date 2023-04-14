sentence = input("please enter your sentence: ")
counter = 0
for i in range (len(sentence)):
    if sentence[i] == " ":
        counter = counter + 1

print(counter + 1)        
