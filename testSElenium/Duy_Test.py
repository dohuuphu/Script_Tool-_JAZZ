import csv
with open('Data_ID.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        name = row['Name']
        idxpath = row['ID_XPath']
        print(f"{name} - {idxpath} ")
        print("row", row)
    print ("reader",reader)
import pandas as pd
def GetDataName(FileName,name,colum):
        csv = pd.read_csv(FileName)
        row = csv[csv.Name == name].values[0]
        print (row[colum])
        return row[colum]


GetDataName('Data_Main.csv','Test 2',0)
GetDataName('Data_ID.csv','IDuser_id',1)
