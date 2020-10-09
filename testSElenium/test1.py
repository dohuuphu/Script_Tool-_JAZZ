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
    Machine_name_title_csv = "TestComplete14_"
    # title value:
    Machine_name_title = ["Machine_name_title", Machine_name_title_csv]


    # title value:
    Machine_title = ["Machine_title", "Edit"]
    Machine_name_title = ["Machine_name_title", machine_name]

    # style value:
    Machine_style = ["Machine_style", "width: 177px;"]

    #dojoattachpoint value;
    dojoattachpoint = ["dojoattachpoint","tableContainerFormNode"]
    #name value:
    Machine_row_name = ["Machine_row_name", '//input[@name="com_ibm_asq_common_web_ui_internal_widgets_tableViewer_TableViewer_1-radio-group"]']
    # Tag_html
    style_tag = "@style"
    title_tag = "@title"
    dojoattachpoint_tag ="@dojoattachpoint"
    name_tag = "@name"
    if Machine_name_title_csv == "TestComplete14_":
        Machine_row_father = '//tr[@name="39-row"]'

        
         







    Click_Tag_htlm(title_tag, timeout, Machine_name_title)





def generate_xpath(element, current):
    child_tag = str(element.tag_name)
    if child_tag == "html":
        return "/html[1]" + current
    parentElements = element.find_element_by_xpath("..")
    childrenElements = parentElements.find_elements_by_xpath("*")
    count = 0
    for e in childrenElements:
        childrenElementTag = e.tag_name
        if child_tag == childrenElementTag:
            count = count + 1
        if element == e:
            return generate_xpath(parentElements, "/" + child_tag + "[" + str(count) + "]" + current)

def main():
    setup2()
    generate_xpath()

   
   

if __name__ == "__main__":
    main()
    