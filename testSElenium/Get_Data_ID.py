import csv
import pandas as pd
def Read_Data_ID(input_Name):
    with open('Data_ID.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            name = row['Name']
            idxpath = row['ID_XPath']
            if input_Name== name:
                print("Name : ", name)
                print("idXpath : " ,idxpath)

Read_Data_ID("IDuser_id")
Read_Data_ID("Plannningbox_id")