import random
import pyfiglet
import printy

try:
    wordsfile=open("RandomWords" , "r")
except:
    print("file not found")
global listofwords,wordtobeguessed,guessedword,lettersguessed,wordsguessed,tries,guessed,gameon
listofwords=wordsfile.readlines()
for i in range(len(listofwords)):
    listofwords[i]=listofwords[i].strip()
from HangmanStrages import HANGMAN
def initround():
    global listofwords, wordtobeguessed, guessedword, lettersguessed, wordsguessed, tries, guessed, gameon
    wordtobeguessed=random.choice(listofwords).upper()
    guessedword=[]
    for i in wordtobeguessed:
        guessedword.append("_")
    lettersguessed=[]
    wordsguessed=[]
    tries=6
    guessed=False

gameon=True

def printguessed():
    font = "js_stick_letters"
    toprint = pyfiglet.figlet_format(guessedword, font=font, width=200)
    printy.printy(toprint, "cB")
while gameon:
    initround()
    printy.printy(HANGMAN[6-tries],"pB")
    print("The word to be guessed is: ")
    printguessed()
    while tries>0 and not guessed:
        print("You have ", tries ," tries  remaining")
        guess=str(input("Enter a letter/ a word you want to guess ").upper())
        if not guess.isalpha():
            print("Invalid input please write a string")
            continue
        elif len(guess)>1 and len(guess)!= len(wordtobeguessed):
            print("You can only guess a word of the same length of thw word to be guessed or a single letter")
            continue
        elif (guess in lettersguessed) or (guess in wordsguessed):
            print("Word/Letter already guessed")
            continue
        if guess not in wordtobeguessed:
            print("Letter/ word not in the wort to be guessed Unlucky!")
            if len(guess)==1:
                lettersguessed.append(guess)
            else:
                wordsguessed.append(guess)
            tries -= 1
            printy.printy(HANGMAN[6 - tries], "pB")

        elif guess==wordtobeguessed:
            congratsmsg="Congrats you guessed the word" ,wordtobeguessed ,"correctly"
            printy.printy(congratsmsg,"rBU")
            guessed=True
        elif guess in wordtobeguessed:
            for i in range(len(wordtobeguessed)):
                if wordtobeguessed[i]==guess:
                    guessedword[i]=guess
            lettersguessed.append(guess)
        if "_" not in guessedword:
            guessed=True
            print("Congrats you won the word was" , wordtobeguessed)
            guessed=True
        if (tries==0 and not guessed):
            print("Unlucky the word was ", wordtobeguessed)
            choice=input("Do you want to play again? y/n").lower()
            while choice!='y' and choice!='n':
                choice=input("You can only enter y or n").lower()
            if choice=='n':
                gameon=False
        elif guessed:
            choice=input("Do you want to play again? y/n").lower()
            while choice!='y' and choice!='n':
                choice=input("You can only enter y or n").lower()
            if choice=='n':
                gameon=False
        else:
            printguessed()
