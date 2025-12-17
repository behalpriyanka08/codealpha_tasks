import random
words =["apple","train","water","tree","milk"]

s_words =random.choice(words)
guess_letter=[]
wrong_guess=0
max_wrong=6

print("---WELCOME TO HANGMAN GAME---")
print("Guess the word one letter at a time")
print(f"You are allowed only {max_wrong} incorrect guesses")

while True:
    display_word=" "
    for letter in s_words :
        if letter in guess_letter:
            display_word += letter + " "
        else:
            display_word += "_ "  
    print("Word :", display_word)

    if all(letter in guess_letter for letter in s_words):
       print("You guessed the correct letter",s_words)
       break
    guess = input("Enter letter :").lower()
    
    if len(guess)!=1 or not guess.isalpha():
       print("Please enter single letter")
       continue
    
    if guess in guess_letter:
       print("You already guessed the word")
       continue
 
    guess_letter.append(guess)

    if guess not in s_words:
        wrong_guess += 1
        print("Wrong guess ! ({wrong_guess}/{max_guess}) \n ")
        if wrong_guess==max_wrong:
             print("Game Over! You ran out the game")
             print("The Word was ",s_words)
             break
    else:
        print("Good Guess")

