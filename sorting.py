import pandas as pd

ATUdata = pd.read_csv("atu.csv")


# organizing the info I need 

ATUid = ATUdata["atu_id"]
ATUtale = ATUdata["tale_name"]
ATUtype = ATUdata["tale_type"]
print (ATUid, ATUtale, ATUtype)

newATUcsv = pd.DataFrame()
newATUcsv["ID"] = ATUid
newATUcsv["Name"] = ATUtale
newATUcsv["Type"] = ATUtype
print (newATUcsv)

newATUcsv.to_csv("newATUcsv.csv")



