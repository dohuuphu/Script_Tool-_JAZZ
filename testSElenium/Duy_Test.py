from action_funtion import * 
from selenium.webdriver.support.ui import WebDriverWait

Get_Machine_from_Web = ""
# Machine_name_title_excel = "TEST02-PC" #delete	

Machine_name_title_excel = "TestExecute-PC" #delete


def setup2():
    #global style_tag
    cf.driver.get("https://rationalcld.dl.net/qm/web/console/ID%20%28Test%29#action=com.ibm.rqm.planning.home.actionDispatcher&subAction=viewSER&id=244409")
    #cf.driver.maximize_window()

    # Login to webpage
    Send_Tag_htlm(cf.ID_tag, cf.timeout, cf.IDuser_id)
    Send_Tag_htlm(cf.ID_tag, cf.timeout, cf.password_id)
    Click_Tag_htlm(cf.text_Tag, cf.timeout, cf.Login_text)

    # Click Run
    Click_Tag_htlm(cf.aria_label_tag ,cf.timeout, cf.Run_btn_arialable)
    Click_Tag_htlm(cf.Class_tag, cf.timeout, cf.Run_testsuit_class)
    # Get_Text_Element()
    # Click_Father_Son_Tag_htlm_Dbl(style_tag,timeout,testcase_1, Machine_style)
    # Get_Element_Row_Name_and_Health_Machine(10)

    print(Get_TimesPage())
    # Demo_Test_NumPage(7)
    Change_Machine_For_Testcase(cf.timeout, 'TestExecute-PC',Get_TimesPage())

def Get_Text_Element():
    global Get_Machine_from_Web
    time.sleep(5)
    # Click_Tag_htlm(Class_tag, timeout, Run_testsuit_class)
    Machine_Element_link= '//td[@class="table-cell-editable"]//div[@class="clip-cell-nowrap table-cell-resize-marker"]//span'
    Machine_Element = cf.driver.find_elements_by_xpath(Machine_Element_link)
    Get_Machine_from_Web = Machine_Element[0].text
    LenText = len(Get_Machine_from_Web)
    print("length",LenText )
    print('Get_Machine_from_Web: ',Get_Machine_from_Web)
def Finish_Click():  
    time.sleep(5)
    # Click_Tag_htlm(Class_tag, timeout, Run_testsuit_class)
    Finish_Click_link= '//button[@class="moreMargin button-primary primary-button"]'
    Finish = cf.driver.find_element_by_xpath(Finish_Click_link)
    Finish.click()

def Demo_Test_NumPage(page):
    for N in range(page):
        Click_Next_Button_Select_Machine()
def Click_OK_Button_Select_Machine():
    time.sleep(10)
    Button_OK_link='//div[@class="actions-container"]//button[@tabindex="0"]'
    Button_OK_Xpath = cf.driver.find_elements_by_xpath(Button_OK_link)[0]
    Button_OK_Xpath.click()
def Click_Next_Button_Select_Machine():
    time.sleep(5)
    Button_Next_link= '//a[@class="button"]//span[@style="display: inline;"]'
    Button_Next_Xpath = cf.driver.find_elements_by_xpath(Button_Next_link)[1]
    Button_Next_Xpath.click()
    time.sleep(2)
def Change_Machine_For_Testcase(timeout_item ,Machine_name_title_excel, TimesPage):
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
    if (Machine_name_title_excel != Get_Machine_from_Web and cf.error_flag == 0):
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
                find_Full = cf.driver.find_elements_by_xpath(Full)[0]
                display_find_Full = find_Full.is_displayed()  # check if the path displays
                if(display_find_Full is True):
                    print("find_Full: ", find_Full)
                    #actionChains.double_click(find_Full).perform()
                    # Click_OK_Button_Select_Machine()
                    # Get_Element_Row_Name_and_Health_Machine(10)
                    #time.sleep(5)
                    rowint = 0
                    Header = '//table[@summary="This is Machine Adapter table"]/tbody'
                    # Header = '//*[@id="com_ibm_asq_common_web_ui_internal_widgets_tableViewer_TableViewer_1"]/div[3]/div/table/tbody'
                    for r in range(10): # Numbers of machine
                        # time.sleep(2)
                        done = 0
                        count = 0
                        actionChains = ActionChains(cf.driver)
                        actionChains.double_click(find_Full).perform()
                        while(count < timeout_item):
                            try:
                                xpath = "//*[@class='content-container']"
                                time.sleep(1)
                                count = count + 1 
                                find_element = cf.driver.find_elements_by_xpath(xpath)[0]
                                display = find_element.is_displayed()  # check if the path displays
                                if(display is True):      
                                    done = 1 
                                    break
                            except:
                                time.sleep(1)
                                count = count + 1   
                                print("waiting Machine table")
                            if(done == 0):   # try: was not run
                                cf.error_flag = 1 # have error
                        if(done == 1 and cf.error_flag == 0 ):
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
                            WebDriverWait(cf.driver, cf.timeout).until(EC.element_to_be_clickable((By.XPATH, Element_Row_Choose)))
                            Element_Row_Name = cf.driver.find_elements_by_xpath(Element_Row_Name)[2]
                            Element_Row_Health = cf.driver.find_elements_by_xpath(Element_Row_Health)[0]
                            Element_Row_Choose = cf.driver.find_elements_by_xpath(Element_Row_Choose)[0]
                        # Click_Tag_htlm()
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
                    # Click_OK_Button_Select_Machine()
                    Click_Father_Son_Tag_htlm(cf.Class_tag, cf.timeout, cf.ok_father, cf.ok_class)


            Click_Next_Button_Select_Machine()
            time.sleep(3)
        Finish_Click()
    else:
        print( "It match don't need change")
        Finish_Click()
    


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
        Element_Row_Name = cf.driver.find_elements_by_xpath(Element_Row_Name)[2]
        Element_Row_Health = cf.driver.find_elements_by_xpath(Element_Row_Health)[0]
        Element_Row_Choose = cf.driver.find_elements_by_xpath(Element_Row_Choose)[0]
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
                
                # find_Full = cf.driver.find_elements_by_xpath(Full)[0]
                # actionChains = ActionChains(cf.driver)
                # actionChains.double_click(find_Full).perform()
    Click_OK_Button_Select_Machine()



def Get_TimesPage():
    TimesPage_Link= '//div[@class="content-status-area"]'
    
    WebDriverWait(cf.driver, cf.timeout).until(EC.element_to_be_clickable((By.XPATH, TimesPage_Link)))
    TimesPage = cf.driver.find_elements_by_xpath(TimesPage_Link)[0]
    # displayTimesPage = TimesPage.is_displayed()  # check if the path displays
    #     if(displayTimesPage is True):
    Times = TimesPage.text

    A = (int(Times.index("of")+3))
    B = (int(Times.index("items") -1))
    TimesPage = int(int(Times[A:B])/10)+ 1
    print(TimesPage)
    return TimesPage

def main():
    setup2()
    # generate_xpath()
    # Get_Text_Element()
    # Get_TimesPage()

   
   

if __name__ == "__main__":
    main()
    