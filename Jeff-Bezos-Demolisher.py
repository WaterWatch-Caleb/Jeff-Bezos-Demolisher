#neccesary modules to import
import random #for randomizer
import string
import fileinput #to manipulate files
import time #for giving the bot a sleep time before running again
import tweepy #python twitter api handler
#set twitter developer credentials and api
auth = tweepy.OAuthHandler("*******", "******")
auth.set_access_token("******", "*******")
api = tweepy.API(auth)
#setting main
def main():
    while True: 
        wordchoice1, wordchoice2, wordchoice3 = pickwords()
        combo = comstring(wordchoice1, wordchoice2, wordchoice3)
        tweetins(combo)
        time.sleep(43200) #adjust for sleep time (in seconds)
#opens the adjective holding file to read from and select from randomly
def pickwords():
    my_file = open('adj.txt', 'r')
    text = my_file.read()
    my_file.close()
    word = text.split('\n')
    wordchoice1 = random.choice(word)
    wordchoice2 = random.choice(word)
    wordchoice3 = random.choice(word)
    print(wordchoice1, wordchoice2, wordchoice3)
    #return it for comstring to take
    return wordchoice1, wordchoice2, wordchoice3
#combines the words and compares to the spent tweet list
def comstring(wordchoice1, wordchoice2, wordchoice3):
    combo = f"The {wordchoice1} {wordchoice2} {wordchoice3} Jeff Bezos"
    with open('spenttweets.txt') as f:
        if f'{combo}' in f.read():
            main() #starts over to prevent duplicate tweets which may end the program/return an error from twitter
        else:
            print(f"{combo}")
            my_file = open('spenttweets.txt' , 'a')
            my_file.write(combo)
            my_file.write('\n')
            my_file.close
            return combo #return combo for tweetins to take
            
def tweetins(combo): 
    api.update_status(combo) 

if __name__=="__main__":
    main()
