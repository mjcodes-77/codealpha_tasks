import random 

#list of Predfined Words for game 
words= ['beautiful', 'programming', 'weather', 'country', 'breach']

#Randomly selects one word from the list 
word= random.choice(words)

#stores the guessed letters of user
guessed_letters= []

#keeps track of wrong variables
wrong_guess= 0
max_guess= 6
print("Welcome to Hangman Game!")

#Continues the game until the user reaches maximum guess limit 
while wrong_guess < max_guess:

    #displays the correct progress of the word
    display_word= " "
    for letter in word: 
        if letter in guessed_letters:
            display_word+= letter + " "
        else:
            display_word+= "_"
    print("Word: ",display_word)

    #checks if the guessed letter is in word
    if "_" not in display_word:
        print("Congratulations!You guessed it right!")
        break 

    #Takes letters as input from user
    guess= input("Enter a letter: ")

    #ensures only one letter is entered at a time
    if len(guess) !=1: 
        print("Please print one letter at a time.")
        continue

    #Avoids any repeation of the word
    if guess in guessed_letters:
        print("You have already guessed this letter.")

    #stores the guessed_letters
    guessed_letters.append(guess)

    #Checks if the word guessed is correct
    if guess in word:
        print("Correct Guess!")
    else: 
        wrong_guess+=1
        print("Wrong Guess!")
        print("Remaining guesses: ", max_guess-wrong_guess)

#Display the word upon completion of the game
if max_guess== wrong_guess:
    print("Game Over")
    print("The word was: ", word)




