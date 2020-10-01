from selenium import webdriver




email, password = 'your-own-email', 'your-own-password'
PATH = r"C:\Users\pdo2\Desktop\Script Tool\Src\Driver\chromedriver84.exe"

driver = webdriver.chrome(PATH)
driver.implicitly_wait(10)

driver.get("https://my.gumtree.com/login")
driver.find_element_by_name("username").send_keys(email)
driver.find_element_by_id("existingUser").click()
driver.find_element_by_id("fld-password").send_keys(password)
driver.find_element_by_xpath("//*[contains(text(), 'Continue')]").click()

driver.get("https://my.gumtree.com/postad")
driver.find_elements_by_xpath("//*[text()='For Sale']")[-1].click()
driver.find_element_by_xpath("//span[text()[normalize-space()='Appliances']]").click()
driver.find_element_by_xpath("//span[text()[normalize-space()='Home Appliances']]").click()
driver.find_element_by_xpath("//span[text()[normalize-space()='Other Home Appliances']]").click()