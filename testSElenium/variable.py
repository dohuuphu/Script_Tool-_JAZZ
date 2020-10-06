
#global_Variable
error_flag = 0

#   Const
#login_ID = "lhoang"
#login_password = "D@talogic7"
timeout = 60
filter_TestPlan = "1439"
ViewBuildRecord_table = "//div[@class=\"jazz-ui-StyledBox sbBlue sbDark shadow jazz-ui-Dialog-absolute com-ibm-asq-common-web-dialog\"]"

#path
# ID:
IDuser_id = ['IDuser_id', 'jazz_app_internal_LoginWidget_0_userId', "lhoang"]
password_id = ["password_id", "jazz_app_internal_LoginWidget_0_password", "D@talogic7"]
Plannningbox_id = ["Plannningbox_id", "jazz_ui_MenuPopup_7"]
Browse_testplan_id = ["Browse_testplan_id","jazz_ui_menu_MenuItem_0_text"]
Runbutton_id = ["Runbutton_id", "dijit_MenuItem_12_text"]

# Xpath:
login_button_xpath = ["login_button_xpath", "//*[@id=\"jazz_app_internal_LoginWidget_0\"]/div[1]/div[1]/div[3]/form/button"]

# Linktext:
ID_test_linktext = ["ID (Test)","ID (test)"]
TestPlan_linktext = ["1439","1439"]

# Text:
Login_text = ["Login_text" ,"Log In"]
Browse_TestPlan_text = ["Browse_TestPlan_text", "Browse Test Plans"]
Testsuit_records_text = ["Testsuit_records_text","Test Suite Execution Records"]
#Run_text = ["Run_text", "Run"]


# Aria lable:
Filter_TsPlan_arialable = ["Filter_TsPlan_arialable, ""This is Test Plans table: filter text input"]
TC1_arialable = ["TC1_arialable", "CommandlineTest - Load configuration with Script Formatting from PC_Matrix M300N"]
Run_btn_arialable= ["Run_btn_arialable", "Run Test Suite (Ctrl+Shift+X) Drop-Down Menu"]
Filter_record_arialable = ["Filter_record_arialable", "This is View Build Records table: filter text input","1.9.0 RC 01"]

# Title value:
Planning_title = ["Planning_title", "Planning"]
Clear_Associated_Build_title = ["Clear_Associated_Build_title", "Clear Associated Build"]
Change_Associated_Build_title = ["Change_Associated_Build_title", "Change Associated Build"]
Clear_Table_Filters_title = ["Clear_Table_Filters", "Clear Table Filters"]

# Name:
Clear_Text_Filter_name = ["Clear_Text_Filter", "This is View Build Records table Clear Filter Text"]

# Class:
Run_testsuit_class = ["Run_testsuit_class", "dijitIcon dijitMenuItemIcon execute-icon-image"]
Run_filter_buildrecord_class = ["Run_filter_buildrecord_class", "image-action primary-button"]
Select_BuildRecord_class = ["Select_BuildRecord", "dijit dijitReset dijitInline dijitRadio"]
Ok_buildRecord_class = ["Ok_buildRecord_class", "primary-button"]

# Tag_html
title_tag = "@title"
aria_label_tag = "@aria-label"
ID_tag = "@id"
Class_tag = "@class"
Name_tag = "@name"
text_Tag = "text()"
name_id= "@name"


