import csv
with open('Login.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "PassWord","Status"])
    writer.writerow(["lhoang", "D@talogic7",""])

