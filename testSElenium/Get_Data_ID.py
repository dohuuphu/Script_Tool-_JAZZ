import csv
import pandas as pd
def Read_Path(input_Name):
    with open('Data_ID.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            name = row['Name']
            path = row['ID_XPath']
            if input_Name == name:
                return [name, path]
            else:
                print("Name is not correct")

def Read_value(input_Name):
    with open('Data_ID.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            name = row['Name']
            value = row['Status']
            if input_Name == name:
                return value
            print("Name is not correct")

a = Read_Path("IDuser_id")
print(a)