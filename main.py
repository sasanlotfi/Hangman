import random
import sys
difficulty=0
########Menu#######
print("Welcome to Hangman game!")
print("In this game, a random word will be picked and its letters will be hidden to you. You have to find the word by guessing its letters.")
print("The number of wrong guesses allowed is equal to the number of letters in the word (after you reach that maximum, you will lose if you have any other wrong guess.)")
print("Enter 0 whenever you want to exit the game.")
print("Enter 1 if you want to go to the first menu and try another difficulty.")

print("\nThere are three difficulty levels for this game:")
print("1- Easy \n2- Medium\n3- Hard")
difficulty=int(input("Enter the number of the difficulty:"))
if(difficulty==0):
    print("Thanks for playing the game!")
    sys.exit()#exits the program



#Creating a list that contains the words of the game.
name_list=[["ball","east","west","time","book","school","bird","bread","meat","boy","ear","back","car","orange","red"],["room","beautiful","hello","bus","yellow","engineering","sign","carpet","kick","telephone","thunder","fail"],["outstanding","wow","howdy","zoo","tesla","texas","victory","youth","ifeluwa","nevada","trump","new","omg","lol"]]

index=random.randint(0,len(name_list[difficulty-1])-1)#the random index is used to pick the word from the list of the names

word=name_list[difficulty-1][index]#use the random index found in the previous line to pick the word from the appropriate difficulty level
dashed_word=[]

for i in word:
    dashed_word.append('-') #putting a dash for each letter in the word in order to hide them.

#The number of wrong guesses allowed
guess=len(word)+1
#a list to contain the guessed letters
guessed_letters=[]
value=None
print("\nNumber of guesses remained:", guess)
for i in dashed_word:
    print(i, end=" ")
print()

####The main loop of the game that keeps iterating until one of the conditions get wrong or a break command is executed
while(guess>0 and value!='0'):
    value=input("Guess a letter:")

    if(value=='0'):
        print("Thanks for playing the game!")
        break
    #The code that takes the user to the first menu if number 1 is enetered
    if(value=='1'):
        print("\nThere are three difficulty levels for this game:")
        print("1- Easy \n2- Medium\n3- Hard")
        difficulty = int(input("Enter the number of the difficulty:"))
        if (difficulty == 0):
            print("Thanks for playing the game!")
            sys.exit()
        index = random.randint(0, len(
            name_list[difficulty - 1]) - 1)  # the random index is used to pick the word from the list of the names

        word = name_list[difficulty - 1][
            index]  # use the random index found in the previous line to pick the word from the appropriate difficulty level
        dashed_word = []

        for i in word:
            dashed_word.append('-')  # putting a dash for each letter in the word in order to hide them.

        # The number of wrong guesses allowed
        guess = len(word) + 1
        # a list to contain the guessed letters
        guessed_letters = []
        value = None
        print("\nNumber of guesses remained:", guess)
        for i in dashed_word:
            print(i, end=" ")
        print()
        continue


    if(value in guessed_letters):
        print("You have guessed this letter before. Try another one.")
        continue

    guessed_letters.append(value)
    if(value in word):
        for i in range(len(word)):
            if(value==word[i]):
                dashed_word[i]=value
        print()
        for i in dashed_word:
            print(i,end=" ")
        print("\nThe letters guessed so far:",guessed_letters)
        print("Number of guesses remained:", guess)
    else:#If the guessed letter is not in the word, do the following
        print()
        for i in dashed_word:
            print(i, end=" ")
        guess-=1
        print("\nThe letters guessed so far:", guessed_letters)
        print("Number of guesses remained:", guess)

    if(not('-' in dashed_word)):#if there are no dashed left (all of the letters are guessed)
        print("\nYou won! The word was",word+".")
        break
    if(guess==0):
        print("\nYou ran out of guesses. The word was",word+".")

