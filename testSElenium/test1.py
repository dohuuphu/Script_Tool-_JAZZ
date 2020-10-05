from action_funtion import *

def setup2():
    driver.get("https://rationalcld.dl.net/qm/web/console/ID%20%28Test%29#action=com.ibm.rqm.planning.home.actionDispatcher&subAction=viewSER&id=244409")
    #driver.maximize_window()

     # Login to webpage
    Send_key_id(timeout,IDuser_id, login_ID)
    Send_key_id(timeout, password_id, login_password)
    Click_button_xpath(timeout, login_button_xpath)

    # Click Run
    Click_Tag_htlm(aria_label_tag ,timeout, Run_btn_arialable)
    Click_Tag_htlm(text_Tag, timeout, Run_text)



def main():
    setup2()


if __name__ == "__main__":
    main()
    