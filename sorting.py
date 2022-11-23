import pandas as pd 

""" ATUdata = pd.read_csv("atu.csv")


# organizing the info I need 

ATUid = ATUdata["atu_id"]
ATUtale = ATUdata["tale_name"]
ATUtype = ATUdata["tale_type"]
print (ATUid, ATUtale, ATUtype)

newATUcsv = pd.DataFrame()
newATUcsv["ID"] = ATUid
newATUcsv["Name"] = ATUtale
newATUcsv["Type"] = ATUtype
print (newATUcsv) """


# newATUcsv.to_csv("newATUcsv.csv") 


# need to create another new csv with just the cinderella, sleeping beauty, little red riding hood (and related) data, 
# will ask user just about those related tale types. 

editATU = pd.read_csv("newATUcsv.csv")

cinderella = editATU.iloc[2150: 2196, 1: 4]      # Cinderella is part of a group of tales within these rows in the csv
# print (cinderella)

sleepingbeauty = editATU.iloc[2040: 2086, 1: 4] # ditto for sleeping beauty
# print (sleepingbeauty)

redridinghood = editATU.iloc[2084: 2151, 1: 4]   # ditto for red riding hood
# print (redridinghood) 

# put these groups in another new csv (talegroup.csv)

cinderella.to_csv("cinderella.csv")

sleepingbeauty.to_csv("sleepingbeauty.csv")

redridinghood.to_csv("redridinghood.csv")






