import csv
import pandas as pd
Check_Machine_Colum = 1 
Name_Colum =  2
Total_Test = 5
x = 0
Check_row= 0
def Read_Data_ID():
    with open('Data_ID.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            name = row['Name']
            idxpath = row['ID_XPath']
            # print(f"{name} - {idxpath} ")
            print("Row :      ", row)
            print("Read:      ", reader)
            print("Name : ", name)
            print("idXpath : " ,idxpath)
        # print ("reader",reader)

Read_Data_ID()