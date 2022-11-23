import pandas as pd
import random
def getrandomstory (csv):
   storydf = pd.read_csv(csv)
   storyindex = random.randint(0, len(storydf.axes[0])) #figuring out random index within number of rows in selected story csv
   storyoutput = storydf.iloc[storyindex, 0:4] #find story line corresponding
   return (storyoutput.to_csv())

print (getrandomstory("cinderella.csv"))