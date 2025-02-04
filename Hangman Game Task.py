import random
def hangman():

    list_of_words = ['eduyear', 'hangman', 'india', 'laptop']
    word = random.choice(list_of_words)
    turns = 10
    guessmade = ''
    valid_entry = set('abcdefghijklmnopqurstuvwxyz')

    while len(word)>0:
        main_word = ""
        missed = 0

        for letter in word:
            if letter in guessmade:
                main_word = main_word+letter
            else:
                main_word=main_word+"_ "

        if main_word == word:
            print(main_word)
            print("you won!!")
            break

                
        print("guess the words ", main_word)
        guess= input()

        if guess in valid_entry:
            guessmade + guessmade+guess
        else:
            print("enter valid character")
            guess=input()

        if guess not in word:
            turns = turns-1

            if turns == 9:
                print("9 turns left!!!")
                print("---------------")

            if turns == 8:
                print("8 turns left!!!")
                print("---------------")
                print("       0       ")

            if turns == 7:
                print("7 turns left!!!")
                print("---------------")
                print("       0       ")
                print("       |       ")

            if turns == 6:
                print("6 turns left!!!")
                print("---------------")
                print("       0       ")
                print("       |       ")
                print("      /        ")

            if turns == 5:
                print("5 turns left!!!")
                print("---------------")
                print("       0       ")
                print("       |       ")
                print("      / \      ")

            if turns == 4:
                print("4 turns left!!!")
                print("---------------")
                print("       0       ")
                print("      /|       ")
                print("      / \      ")

            if turns == 3:
                print("3 turns left!!!")
                print("---------------")
                print("       0       ")
                print("      /|\      ")
                print("      / \      ")

            if turns == 2:
                print("2 turns left!!!")
                print("---------------")
                print("       0       ")
                print("      /|\|     ")
                print("      / \      ")

            if turns == 1:
                print("Only 1 turns left!!! Hangman On His Last Breath")
                print("---------------")
                print("       0       ")
                print("      /|\_|    ")
                print("      / \      ")

            if turns == 0:
                print("You Will Loose!!!")
                print("You Let a Good Man Die")
                print("---------------")
                print("       0_|     ")
                print("      /|\       ")
                print("      / \      ")
                break
               
name = input("ENTER YOUR NAME -> ")
print("Welcome",name,"!")
print("----------------")
print("try to guess the word in less than 10 attempts")
hangman()
