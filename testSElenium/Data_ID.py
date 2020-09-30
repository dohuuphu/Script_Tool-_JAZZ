import csv
with open('Data_ID.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Test Machine", "Buid Record", "Status"])
    writer.writerow(["IDuser_id", "jazz_app_internal_LoginWidget_0_userId",""])
    writer.writerow(["password_id", "jazz_app_internal_LoginWidget_0_password",""])
    writer.writerow(["login_button_xpath", "//*[@id=\"jazz_app_internal_LoginWidget_0\"]/div[1]/div[1]/div[3]/form/button",""])
    writer.writerow(["ID_test_id", "ID (Test)",""])
    writer.writerow(["Plannningbox_id", "jazz_ui_MenuPopup_7",""])
