# random story-picker function
import pandas as pd
import random
def getrandomstory (csv):
   storydf = pd.read_csv(csv)
   storyindex = random.randint(0, len(storydf.axes[0])) #figuring out random index within number of rows in selected story csv
   storyoutput = storydf.iloc[storyindex, 0:4] #find story line corresponding. Has to be 4 so that tale type is included 
   return storyoutput.to_csv()


while True:
    userintro = input ("are you ready to learn about stories? ")
    if userintro == str("yes") or str("Yes") or str("YES") or str("Y") or str("y"):
        print (" Hooray! Did you know that stories from all over the world\n can be organized by their similarities into something called the Aarnes-Thompson-Uther Index?\n The ATU index logs almost every story you can think of.")
    else: 
        print ("No time for games. There's stories to hear.")
        print ("The Aarnes-Thompson-Uther index organizes almost every story you can think of \nfrom all over the world, by their plot or other literary motifs.")

    userchoice = input ("type \"c\", \"s\", or \"r\" to explore more about \nthe tale groups that include \nCinderella, Sleeping Beauty, or Red Riding Hood" )

    if userchoice == str("c"):
        print ("The story widely known as CINDERELLA is part of an ATU group known as: ")
        print ("SUPERNATURAL HELPERS")
        print ()
        print ()
        print ("... can you guess why?")
        randomtale1 = input ("Would you like to see a random tale from this group? (y/n) \n")  # if statement inside if statement?
        if randomtale1 == str("y"):
            print (getrandomstory("cinderella.csv")) # call function to select random cinderella-related story
    
    elif userchoice == str("s"):
        print ("The story that quite often goes by SLEEPING BEAUTY is part of an ATU group called: ") 
        print ("SUPERNATURAL AND/OR ENCHANTED WIVES") 
        print ()
        print ()
        print ("... Why do you think that is?") 
        randomtale2 = input ("Would you like to see a random tale from this group? (y/n) \n ")
        if randomtale2 == str("y"):
            print (getrandomstory("sleepingbeauty.csv")) # call function to select random related story

    elif userchoice == str("r"):
        print ("The story LITTLE RED RIDING HOOD is part of a group of tales called SUPERNATURAL ADVERSARIES")
        print ()
        print ()
        print ("... I wonder why.")
        randomtale3 = input ("Would you like to see a random tale from this group? (y/n) \n ")
        if randomtale3 == str("y"):
            print (getrandomstory("redridinghood.csv")) # call function to select random related story

        