import random
from typing import List
from tkinter import *

def create_sentence(list_of_words: str): #sentence: str:
    """
    creates the list of words that make a sentence from the chosen file
    >>> create_sentence
    """
    num_words = random.randint(0,10)

    return num_words
    return sentence

def create_paragraph(sentence: str): #-> paragraph:
    """
    creates a paragraph from the sentences created in create_sentence
    """
    pass

def main_game(sentence: str):
    """
    presents the user with the sentence they have to type, returns if they got the word right and the time it took to type
    """
    attempt = str(input('type this sentence: ' + sentence))
    if attempt == sentence:
        return True
    else:
        return False
def get_wpm():
    pass

def game_window(sentence):
    top = Tk()
    var = StringVar()
    label = Label(top, textvariable=var, relief=RAISED)
    var.set('please type this sentence: \n' + sentence)
    label.pack()
    entry = Entry(top, text = 'Attempt')
    entry.pack()
    answer = entry.get()
    print(answer)
    top.mainloop()


#if __name__ == 'main':
sentence = 'this is a test!'
avg_word = 5.5 #assuming length of average word in english is 4.5 letters + 1 to account for spaces
game_window(sentence)
play_count = str(input('Welcome to typemaster 7, read notes for info, would you like to play ? (y/n)'))
#'type the presented sentence perfectly, including capitals and punctuation, after you have typed the sentence, your wpm will be presented

while play_count == 'y':
    #query = create_sentence("words_alpha.txt")
    if main_game(sentence) == True:
        print ('correct, you win!')
    else:
        print('sorry you did not get the word right!')
    play_count = str(input('would you like to play again ? (y/n)'))
print('thanks for playing!')




