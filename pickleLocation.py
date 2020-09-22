import csv
import pandas as pd
pickled_df = pd.read_pickle("ID_Location_Dic2.pickle")
f = open('USstates.csv', mode='w')
address_writer = csv.writer(f, delimiter=',', quotechar='"')
address_writer.writerow(["City","County","State"])
raw = pickled_df.values()
states = []
city = []
county = []
for rw in raw:
    rw2 = rw.split(",")
    if(len(rw2) == 2):
        address_writer.writerow(["","",rw2[0].lstrip(' ')])
    elif(len(rw2) == 3):
        if ("County" in rw2[0]):
            address_writer.writerow(["",rw2[0], rw2[1].lstrip(' ')])
        else:
            address_writer.writerow([rw2[0].lstrip(' '),"", rw2[1].lstrip(' ')])
    elif(len(rw2) == 4):
        string = rw2[2]
        if (string[1].isnumeric() or string[0].isnumeric()):
            address_writer.writerow([rw2[0].lstrip(' '),"", rw2[1].lstrip(' ')])
        else:
            address_writer.writerow([rw2[0].lstrip(' '), rw2[1].lstrip(' '), rw2[2].lstrip(' ')])
    elif(len(rw2) == 5):
        string = rw2[3]
        if(string[1].isnumeric() or string[0].isnumeric()):
            address_writer.writerow([rw2[0].lstrip(' '), rw2[1].lstrip(' '), rw2[2].lstrip(' ')])
        else:
            address_writer.writerow([rw2[0].lstrip(' '), rw2[2].lstrip(' '), rw2[3].lstrip(' ')])
    elif (len(rw2) == 6):
        string = rw2[4]
        if (string[1].isnumeric() or string[0].isnumeric()):
            address_writer.writerow([rw2[1].lstrip(' '), rw2[2].lstrip(' '), rw2[3].lstrip(' ')])
        else:
            address_writer.writerow([rw2[2].lstrip(' '), rw2[3].lstrip(' '), rw2[4].lstrip(' ')])
    elif(len(rw2) == 7):
        string = rw2[5]
        if (string[1].isnumeric() or string[0].isnumeric()):
            address_writer.writerow([rw2[2].lstrip(' '), rw2[3].lstrip(' '), rw2[4].lstrip(' ')])
        else:
            address_writer.writerow([rw2[3].lstrip(' '), rw2[4].lstrip(' '), rw2[5].lstrip(' ')])
    elif (len(rw2) == 8):
        string = rw2[6]
        if (string[1].isnumeric() or string[0].isnumeric()):
            address_writer.writerow([rw2[3].lstrip(' '), rw2[4].lstrip(' '), rw2[5].lstrip(' ')])
        else:
            address_writer.writerow([rw2[4].lstrip(' '), rw2[5].lstrip(' '), rw2[6].lstrip(' ')])
    elif (len(rw2) == 9):
        string = rw2[7]
        if (string[1].isnumeric() or string[0].isnumeric()):
            address_writer.writerow([rw2[4].lstrip(' '), rw2[5].lstrip(' '), rw2[6].lstrip(' ')])
        else:
            address_writer.writerow([rw2[5].lstrip(' '), rw2[6].lstrip(' '), rw2[7].lstrip(' ')])
    elif (len(rw2) == 10):
        address_writer.writerow([rw2[5].lstrip(' '), rw2[6].lstrip(' '), rw2[7].lstrip(' ')])
    elif (len(rw2) == 11):
        address_writer.writerow([rw2[6].lstrip(' '), rw2[7].lstrip(' '), rw2[8].lstrip(' ')])
