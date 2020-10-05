
import pandas as pd
Check_Active_Machine_Colum = 5 
Name_Colum =  2
x = 0
Check_row= 0
Note = "True"

def CheckActive(FileName,num,colum):
        csv = pd.read_csv(FileName)
        row = csv[csv.Num == num].values[0]
        Status = row[colum]
        # print (row[colum])
        print (Status)
        return row[colum]
def GetDataName(FileName,num,colum):
        csv = pd.read_csv(FileName)
        row = csv[csv.Num == num].values[0]
        Check_row = row[colum]
        # print (row[colum])
        #Check_row = convert(Check_row))
        if  Check_row == Note  :
                print (Check_row)
        # print (Check_row)
        return Check_row

for i in range(5):
        x = x+1
        A = CheckActive('Data_Main.csv',x,Check_Active_Machine_Colum)
        print ('AAA is', A)
        print(A,'is',bool(A))
        # if A(True):
        #         print('MAchine',CheckActive('Data_Main.csv',x,2))
        # else:
        #         print('MAchine Not equal ',CheckActive('Data_Main.csv',x,2))
        # GetDataName('Data_Main.csv', x ,Check_Active_Machine_Colum)

        # print(Status)
        # print (Check_row)
        # GetDataName('Data_Main.csv', x ,Name_Colum)
        # print (Check_Active_Machine_Colum)
# CheckActive('Data_Main.csv',1,3)
# CheckActive('Data_Main.csv',1,5)
# A = CheckActive('Data_Main.csv',2,5)
# print ('AAA', A)

# else:
#   print("Finally finished!")
# for (i=1; i < 5; i++)
#         {
#              GetDataName('Data_Main.csv',i,Check_Active_Machine)   

#         }
# GetDataName('Data_Main.csv',1,Check_Active_Machine)
# GetDataName('Data_ID.csv','IDuser_id',1)
# def GetData():
#         csv = pd.read_csv(Data_Main.csv)
#         row = csv[csv.Name == 'CommandlineTest - Load configuration with Script Formatting from PC_Matrix M300N'].values[0]
#         print (row[1])
#         return row[1]
# GetData();

# adj = ["red", "big", "tasty"]
# fruits = ["apple", "banana", "cherry"]

# for x in adj:
#   for y in fruits:
#     print(x, y)