import csv
with open('Data_ID.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        name = row['Name']
        idxpath = row['ID_XPath']
        # print(f"{name} - {idxpath} ")
        print("Name : ", name)
        print("idXpath : " ,idxpath)
    print ("reader",reader)
   