from action_funtion import *

Get_Machine_from_Web = ""
# Machine_name_title_excel = "TEST02-PC" #delete	

Machine_name_title_excel = "TestExecute-PC" #delete


def setup2():
    #global style_tag
    driver.get("https://rationalcld.dl.net/qm/web/console/ID%20%28Test%29#action=com.ibm.rqm.planning.home.actionDispatcher&subAction=viewSER&id=244409")
    #driver.maximize_window()

    # Login to webpage
    Send_Tag_htlm(ID_tag, timeout, IDuser_id)
    Send_Tag_htlm(ID_tag, timeout, password_id)
    Click_Tag_htlm(text_Tag, timeout, Login_text)

    # Click Run
    Click_Tag_htlm(aria_label_tag ,timeout, Run_btn_arialable)
    Click_Tag_htlm(Class_tag, timeout, Run_testsuit_class)
    # Get_Text_Element()
    # Click_Father_Son_Tag_htlm_Dbl(style_tag,timeout,testcase_1, Machine_style)
    # Get_Element_Row_Name_and_Health_Machine(10)
    Demo_Test_NumPage(7)
    Change_Machine_For_Testcase('TestExecute-PC',9)

def Get_Text_Element():
    global Get_Machine_from_Web
    time.sleep(5)
    # Click_Tag_htlm(Class_tag, timeout, Run_testsuit_class)
    Machine_Element_link= '//td[@class="table-cell-editable"]//div[@class="clip-cell-nowrap table-cell-resize-marker"]//span'
    Machine_Element = driver.find_elements_by_xpath(Machine_Element_link)
    Get_Machine_from_Web = Machine_Element[0].text
    LenText = len(Get_Machine_from_Web)
    print("length",LenText )
    print('Get_Machine_from_Web: ',Get_Machine_from_Web)
def Finish_Click():  
    time.sleep(5)
    # Click_Tag_htlm(Class_tag, timeout, Run_testsuit_class)
    Finish_Click_link= '//button[@class="moreMargin button-primary primary-button"]'
    Finish = driver.find_element_by_xpath(Finish_Click_link)
    Finish.click()

def Demo_Test_NumPage(page):
    for N in range(page):
        Click_Next_Button_Select_Machine()
def Click_OK_Button_Select_Machine():
    time.sleep(2)
    Button_OK_link='//div[@class="actions-container"]//button[@tabindex="0"]'
    Button_OK_Xpath = driver.find_elements_by_xpath(Button_OK_link)[0]
    Button_OK_Xpath.click()
def Click_Next_Button_Select_Machine():
    time.sleep(2)
    Button_Next_link= '//a[@class="button"]//span[@style="display: inline;"]'
    Button_Next_Xpath = driver.find_elements_by_xpath(Button_Next_link)[1]
    Button_Next_Xpath.click()
    time.sleep(2)
def Change_Machine_For_Testcase(Machine_name_title_excel,TimesPage):
    # Machine_name_title_csv = "TestComplete14_"
    # Machine_name_title_excel = "TestExecute-PC" #delete
    global Get_Name_Machine
    global Full
    global Num
    global Body
    global find_Full
    global NumTr
    Get_Text_Element()
    time.sleep(2)
    if (Machine_name_title_excel != Get_Machine_from_Web):
        print(" Run Test")
        # Machine_name_title_excel = "TestExecute-PC"
        Header = '//table[@summary="This is labelSuiteStepForDialog table"]//tbody'
        End = "//td[4]//div//div//div//span"
        for t in range(TimesPage):
            Num = 0
            NumTr = 0
            for x in range(10):
                time.sleep(2)
                Header = '//table[@summary="This is labelSuiteStepForDialog table"]//tbody'
                End = "//td[4]//div//div//div//span"
                Num = Num + 1
                NumTr = Num
                NumTr = str(NumTr) 
                print("NumTr", NumTr)
                Body = '//tr['+ NumTr +']'
                Full = Header + Body + End
                print("full is : ", Full)
                find_Full = driver.find_elements_by_xpath(Full)[0]
                display_find_Full = find_Full.is_displayed()  # check if the path displays
                if(display_find_Full is True):
                    print("find_Full: ", find_Full)
                    actionChains = ActionChains(driver)
                    actionChains.double_click(find_Full).perform()
                    # Click_OK_Button_Select_Machine()
                    # Get_Element_Row_Name_and_Health_Machine(10)
                    time.sleep(5)
                    rowint = 0
                    Header = '//table[@summary="This is Machine Adapter table"]/tbody'
                    # Header = '//*[@id="com_ibm_asq_common_web_ui_internal_widgets_tableViewer_TableViewer_1"]/div[3]/div/table/tbody'
                    for r in range(10): # Numbers of machine
                        time.sleep(2)
                        actionChains.double_click(find_Full).perform()
                        
                        rowint = rowint + 1
                        row = str(rowint)
                        End = '/tr['+ row + ']'
                        Child_Name = '//div[@class="clip-cell-nowrap table-cell-resize-marker"]'
                        Child_Health = "/td[7]//img"
                        Choose_Machine = '//td[@class="table-non-content-cell"]'
                        Element_Row_Choose= Header + End+ Choose_Machine
                        Element_Row_Name = Header + End + Child_Name
                        Element_Row_Health = Header + End + Child_Health
                        print("Element_Row_Choose",Element_Row_Choose )
                        print("Element_Row_Name",Element_Row_Name )
                        print("Element_Row_Health",Element_Row_Health )
                        # print("Element_Row_Name_and_Health", rowint," : ",Element_Row_Name)
                        Element_Row_Name = driver.find_elements_by_xpath(Element_Row_Name)[2]
                        Element_Row_Health = driver.find_elements_by_xpath(Element_Row_Health)[0]
                        Element_Row_Choose = driver.find_elements_by_xpath(Element_Row_Choose)[0]
                        displayName = Element_Row_Name.is_displayed()  # check if the path displays
                        if(displayName is True):
                            Row_Name_machine= Element_Row_Name.text
                            # print("Have element Name : ", rowint )
                            # print(Row_Name_machine)
                        displayHealth = Element_Row_Health.is_displayed()  # check if the path displays
                        if(displayHealth is True):
                            Status = Element_Row_Health.get_attribute("title")
                            # print ("HAVE ELEMENT HEALTH : ",rowint)
                            # print(Status)
                        if (Machine_name_title_excel == Row_Name_machine ):
                            if (Status == Health_Available ):
                                print ( "Click di ban eeeiiiiiiiii")
                                Element_Row_Choose.click()
                                Element_Row_Choose.click()
                                break
                    Click_OK_Button_Select_Machine()


            Click_Next_Button_Select_Machine()
            time.sleep(3)
    else:
        print( "It match don't need change")


# def Arrange_Heath_Machine():
#     fgggggg
def Get_Element_Row_Name_and_Health_Machine(number_row):
    global Get_Name_Machine
    global Full
    global Num
    global Body
    global find_Full
    global NumTr
    # global Machine_name_title_excel
    time.sleep(5)
    rowint = 0
    Header = '//*[@id="com_ibm_asq_common_web_ui_internal_widgets_tableViewer_TableViewer_1"]/div[3]/div/table/tbody'
    for r in range(number_row):
        time.sleep(5)
        rowint = rowint + 1
        row = str(rowint)
        End = '/tr['+ row + ']'
        Child_Name = '//div[@class="clip-cell-nowrap table-cell-resize-marker"]'
        Child_Health = "/td[7]//img"
        Choose_Machine = '//td[@class="table-non-content-cell"]'
        Element_Row_Choose= Header + End+ Choose_Machine
        Element_Row_Name = Header + End + Child_Name
        Element_Row_Health = Header + End + Child_Health
        print("Element_Row_Choose",Element_Row_Choose )
        print("Element_Row_Name",Element_Row_Name )
        print("Element_Row_Health",Element_Row_Health )
        # print("Element_Row_Name_and_Health", rowint," : ",Element_Row_Name)
        Element_Row_Name = driver.find_elements_by_xpath(Element_Row_Name)[2]
        Element_Row_Health = driver.find_elements_by_xpath(Element_Row_Health)[0]
        Element_Row_Choose = driver.find_elements_by_xpath(Element_Row_Choose)[0]
        displayName = Element_Row_Name.is_displayed()  # check if the path displays
        if(displayName is True):
            Row_Name_machine= Element_Row_Name.text
            # print("Have element Name : ", rowint )
            # print(Row_Name_machine)
        displayHealth = Element_Row_Health.is_displayed()  # check if the path displays
        if(displayHealth is True):
            Status = Element_Row_Health.get_attribute("title")
            # print ("HAVE ELEMENT HEALTH : ",rowint)
            # print(Status)
        if (Machine_name_title_excel == Row_Name_machine ):
            if (Status == Health_Available ):
                print ( "Click di ban eeeiiiiiiiii")
                Element_Row_Choose.click()
                Element_Row_Choose.click()
                
                # find_Full = driver.find_elements_by_xpath(Full)[0]
                # actionChains = ActionChains(driver)
                # actionChains.double_click(find_Full).perform()
    Click_OK_Button_Select_Machine()


def main():
    setup2()
    # generate_xpath()
    # Get_Text_Element()

   
   

if __name__ == "__main__":
    main()
    