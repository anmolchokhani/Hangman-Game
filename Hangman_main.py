#will write all the funcions in different python file and import from there

from player_lives import Hangman_pics
from all_words import words
from random_word import random_word
from time import sleep

#choose a randomword 

#make its same length wala as _ _  _  _ _  _
def list_creation_of_same_length(random_word_choosen):
    dash=[]
    for _ in range(len(random_word_choosen)):
        dash += "_"
    return dash


def welcome_screen(Total_life):

    print(''' 
    ********************
    Lets start the game
    ********************
    ''')
    print(f"You will have {Total_life} lifes\n")


def life_track(Total_life,empty_list_created):
    print("Guessed letter is wrong, you lost a life")
    print(Hangman_pics[len(Hangman_pics)-Total_life],"\n")
    Total_life -=1
    print(f"Total life left {Total_life} \n\n {empty_list_created}")
    return Total_life


    


#take input from user
def doing_computation(from_user,random_word_choosen,empty_list_created,Total_life):
        if from_user in random_word_choosen:
            if from_user not in empty_list_created:
                print("You have guessed right\n")
                for position in range(len(random_word_choosen)):
                    if from_user == random_word_choosen[position]:
                        empty_list_created[position] = from_user
                print(empty_list_created, "\n")
                    
            else:
                print("You have already guessed this letter")
        else:
            Total_life= life_track(Total_life,empty_list_created)
            

        return empty_list_created, Total_life




def main():
    Total_life=7
    random_word_choosen , length_of_word = random_word()
    welcome_screen(Total_life)
    empty_list_created = list_creation_of_same_length(random_word_choosen)
    print(empty_list_created,"\n")
    while True:
        from_user= input('Enter your guess-> ').lower()
        if from_user.isdigit():
            print("\n Entered guess is a number, Enter a valid guess")
            continue
        print()
        empty_list_created, Total_life = doing_computation(from_user,random_word_choosen,empty_list_created,Total_life)
        if Total_life == 0:
            print(f''' 
                    *********************
                      The word was --->   {random_word_choosen} 
                    ********************* \n
                    ''')
            print(''' 
                    **********************
                      You lost, Game Over
                    **********************
                    ''')
            break
        if "_" not in empty_list_created:
            print("You won")
            break

main()




