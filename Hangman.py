import random
from collections import Counter
import string


from collections import Counter


t = 'Welcome to the game of Hangman '
print t

#list = ['clown', 'school', 'university', 'Philadelphia']
list = ['school','philadelphia']


#newrand = []

answer = []

rand_list = list[random.randrange(len(list))]
print rand_list


#index = list.index(rand_list)
#print index


print 'the number of letters in the word are : ' + str(len(rand_list))

p = "yes"

t = []






count = 0

#if rand_list in list[1]:
    #print "8 year olds version of prison "

if rand_list in list[0]:
    print " higher education"

elif rand_list in list[1]:
    print " Rocky from here "

elif rand_list in list[0]:
    print " everyone is scared of it and it works in the circus "

#guess = raw_input(" enter your 'guess': ")




#while True:
    #if p == "yes" or p == "y":
       # guess = raw_input("Guess the word :")
        #if guess.lower() == rand_list.lower():
            #print (" You guess correctly!!!!!!")
        #else:
           # print("sorry that's not the right word :(")
        #p = raw_input("Would you like to Guess again?:")
    #elif p == "no" or p =="n":
        #print("See ya next time")
        #break



for chr in rand_list:
    t.append("-")
    continue
print('  '.join(t))

#for chr in rand_list:
   # print('%s %d' % (chr, rand_list.index(chr)))



f = ('%s %d' % (chr, rand_list.index(chr)))

idx = -1


while True:



    chr = raw_input("guess the letters in the word: ")
    #t.pop(chr in rand_list)
    #t.append('%s , %d' % (chr, rand_list.index(chr[])))
    #may not have to pop !!

    #t.insert(rand_list.index(chr))

    if chr in rand_list:
        guessindex = rand_list.find(chr)
        t.insert(guessindex, chr)
        t.pop(guessindex +1)
        if t[guessindex] != '-':
            guessnextindex = rand_list.find(chr,guessindex +1)
            t.insert(guessnextindex, chr)
            t.pop(guessnextindex + 1)








        #print guessindex.index(chr + 1)























       #continue here as far as the action and position you want to be taken
       # (chr, rand_list.index(chr[0:-1])

        print ("correct")
       # t.append('%s, %d' % (chr, rand_list.index(chr[0])))
        #t = sorted(chr,rand_list.index(chr[+0]))

#find index in the randlist using guess variable

       # f = dict([([+1],[0]) for x in enumerate(rand_list)])

        #str.find(index in rand_list chr)

        print " ".join(t)
   # guessindex = rand_list.find(chr)
    #t.insert(guessindex,chr)

        #rand_list.insert(+1,chr)
        #print chr


   # t = str.find(index in rand_list)
    #print t



    else:
        print ("Sorry I'm Afraid that's wrong.....")



   # if chr == rand_list:
      #  print " You have correctly guess the word"
       # break



















# for i in range(rand_list):
# print(" - ")


# while guess  in rand_list:
# print " You have choose the correct letter "


# if guess in range(rand_list):
# print guess + "Correct "


# else:
# print " your guess is incorrect try again look at your hints!!! "


# while guess


# for loop  run however many guesses and need while loop within
# give a hint


# for char in rand_list:
# print char

# random_letter = random.randrange('a','z')
# guess = input("Enter your guess  ")
