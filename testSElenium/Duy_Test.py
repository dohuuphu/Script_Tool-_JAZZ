import pandas as pd
def GetDataName(FileName,name,colum):
        csv = pd.read_csv(FileName)
        row = csv[csv.Name == name].values[0]
        print (row[colum])
        return row[colum]


GetDataName('Data_Main.csv','Test 2',0)
GetDataName('Data_ID.csv','IDuser_id',1)