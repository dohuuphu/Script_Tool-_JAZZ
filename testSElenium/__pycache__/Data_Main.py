import csv
with open('Data_Main.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Num", "Name", "Test Machine", "Buid Record", "Status"])
    writer.writerow([1, "Test 1", "M1","","Yes"])
    writer.writerow([2, "Test 2", "M2","","Yes"])
    writer.writerow([3, "Test 3", "M3","","Yes"])