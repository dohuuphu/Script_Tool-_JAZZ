
import pandas as pd
Check_Machine_Colum = 3 
Name_Colum =  2
Total_Test = 5
x = 0
Check_row= 0

def CheckActive(FileName,num,colum):
        csv = pd.read_csv(FileName)
        row = csv[csv.Num == num].values[0]
        Status = row[colum]
        # print (row[colum])
        # print (Status)
        return row[colum]
        
# def GetDataName(FileName,num,colum):
#         csv = pd.read_csv(FileName)
#         row = csv[csv.Num == num].values[0]
#         Check_row = row[colum]
#         # print (row[colum])
#         #Check_row = convert(Check_row))
#         if  Check_row == Note  :
#                 print (Check_row)
#         # print (Check_row)
#         return Check_row

for i in range(Total_Test):
        x = x+1
        Machine = CheckActive('Data_Main.csv',x,Check_Machine_Colum)
        
        if Machine != 'None':
                print("Machine Chosen", CheckActive('Data_Main.csv',x,Name_Colum))
        else :
                print("Don't Choose Machine: " , Machine)
