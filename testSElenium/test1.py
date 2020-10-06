from action_funtion import *


def setup2():
    driver.get("https://rationalcld.dl.net/qm/web/console/ID%20%28Test%29#action=com.ibm.rqm.planning.home.actionDispatcher&subAction=viewSER&id=244409")
    #driver.maximize_window()

    # Login to webpage
    Send_Tag_htlm(ID_tag, timeout, IDuser_id)
    Send_Tag_htlm(ID_tag, timeout, password_id)
    Click_Tag_htlm(text_Tag, timeout, Login_text)

    # Click Run
    Click_Tag_htlm(aria_label_tag ,timeout, Run_btn_arialable)
    Click_Tag_htlm(Class_tag, timeout, Run_testsuit_class)
    Click_Father_Son_Tag_htlm_Dbl(style_tag,timeout,testcase_1, Machine_style)
#     time.sleep(3)
#     #xpath = "//tr[@name= '_IMTthl-EEeqc9ZermTj1qQ-row']//span[text()=\"TEST02-PC\"]"
#     #xpath = "//*[@id=\"com_ibm_asq_common_web_ui_internal_widgets_tableViewer_TableViewer_0\"]/div[3]/div/table/tbody/tr[1]/td[4]"
#     xpath = "/html/body/div[6]/div[2]/div[2]/div[3]/div/div[1]/div[1]/div[3]/div[2]/div/div/div[4]/div[2]/div/div/div[3]/div/table/tbody/tr[1]/td[4]/div/div"
#     #"/html/body/div[6]/div[2]/div[2]/div[3]/div/div[1]/div[1]/div[3]/div[2]/div/div/div[4]/div[2]/div/div/div[3]/div/table/tbody/tr[1]/td[4]/div/div/div"
#     find_element = driver.find_element_by_xpath(xpath)
#     print(find_element)
#     actionChains = ActionChains(driver)
#     actionChains.double_click(find_element).perform()
#     print("1")
#    # ActionChains.double_click(find_element).perform()
#     print("2")

def Click_Tag_htlm2(tag, timeout_item, path_item):
    global error_flag
    count = 0
    done = 0
    if(error_flag == 0):  
        while(count < timeout_item):
            try:
                xpath = "//*[" +tag+ "=\"" +path_item[1]+ "\"]"
                print(xpath)
                find_element = driver.find_elements_by_xpath(xpath)[0]
                display = find_element.is_displayed()  # check if the path displays
                if(display is True):
                    WebDriverWait(driver, timeout_item).until(EC.presence_of_element_located((By.XPATH, xpath)), message=("Can not find: "+path_item[0])) # check if the path is clickable          
                    #print("display: " + str(display))
                    #time.sleep(1)
                    find_element.click()
                    print("good: "+ tag + " was clicked")
                    done = 1 
                    break
            except:
                time.sleep(1)
                print("Waiting for Click " + tag)
                count = count + 1   
        if(done == 0):   # try: was not run
            error_flag = 1 # have error





# def generate_xpath(element, current):
#     child_tag = str(element.tag_name)
#     if child_tag == "html":
#     return "/html[1]" + current
#     parentElements = element.find_element_by_xpath("..")
#     childrenElements = parentElements.find_elements_by_xpath("*")
#     count = 0
#     for e in childrenElements:
#     childrenElementTag = e.tag_name
#     if child_tag == childrenElementTag:
#     count = count + 1
#     if element == e:
#     return generate_xpath(parentElements, "/" + child_tag + "[" + str(count) + "]" + current)

def main():
    setup2()
   # inputElement = driver.find_element_by_name("This is labelSuiteStepForDialog table")
    #generate_xpath(inputElement, "").double_click()
    # A ='TestExecute-PC'
    # Click_Tag_htlm(title_tag, timeout, A)
    # xpathresult = '//*[@id="com_ibm_asq_common_web_ui_internal_widgets_tableViewer_TableViewer_0"]/div[3]/div/table/tbody/tr[1]'
    # resultdiv = driver.find_element_by_xpath(xpathresult)
    # resultdiv.double_click()
    # class="clip-cell-nowrap table-cell-resize-marker"
    # summary="This is labelSuiteStepForDialog table"
    # name="_IMTthl-EEeqc9ZermTj1qQ-row"
    # Class_id_choose_Machine = "clip-cell-nowrap table-cell-resize-marker"
    # Click_Tag_htlm2(Class_tag, timeout,Class_id_choose_Machine)
   
   

if __name__ == "__main__":
    main()
    