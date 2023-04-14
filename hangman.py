import random
word_bank = ["cucumber", "banana", "kiwi", "orange", "apple", "pineapple", "melon", "lemon", "mushroom", "peach"]

computer_choice = random.randint(0, len(word_bank) - 1)
word = word_bank[computer_choice]

user_mistakes = 0
good_chars = []
bad_chars = []
while user_mistakes != 6:
    counter = 0
    for i in range(len(word)):
        if word[i] in good_chars:
            print(word[i], end=" ")
            counter += 1
        else:
            print("- ", end=" ") 
    if counter == len(word):
        print("you won the game")
        break
    user_char = input("please enter your character: ")
    user_char = user_char.lower()
    if len(user_char) == 1:
        if user_char in word:
            good_chars.append(user_char)
            print("yes")
        else:
            bad_chars.append(user_char)
            user_mistakes = user_mistakes + 1
            print("no")    
    else:
        print("please enter just one character")
    

     
if user_mistakes == 6:
    print("you lost")