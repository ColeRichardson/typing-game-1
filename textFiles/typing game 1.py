import random
x = 0
lines = open("words_alpha.txt").readlines()
points = 0
wordlist = ""
a = 0
numwords = random.randint(0,15)

while (a <= 10):

    rando = random.randint(0, 370100)
    line = lines[rando]
    words = line.split()
    myword = random.choice(words)
    wordlist = wordlist + myword + ' '
    a += 1
while x == 0:
    attempt = str(input(wordlist))
    if attempt == wordlist:
        points += 1
        print("correct")
        x = 1
    else:
        print('try again')
    
    
