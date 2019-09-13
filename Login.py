import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver=webdriver.Chrome("../Drivers/chromedriver")
driver.get("https://test.salesforce.com")


#Login Screen
driver.find_element_by_id("username").send_keys("chaitra@qa2.com.cfg4")

driver.find_element_by_id("password").send_keys("maxpl0re17")

time.sleep(1)

driver.find_element_by_id("Login").click()
driver.fullscreen_window()

#time.sleep(1)

#SetUpHome
driver.find_element_by_link_text('ServiceMax Setup').click()

driver.find_element_by_id("btnLinkGroup5").click()

driver.find_element_by_id("34").click()

#time.sleep(5)

#MobileConfiguration

profile= driver.find_element_by_id("j_id0:SVMX_FORM:mainBlock:ProfileId")
profilename=Select(profile)
profilename.select_by_visible_text("Technician-Demo-profile")
#driver.find_element_by_xpath("//*[@id='j_id0:SVMX_FORM:mainBlock:j_id89:0:j_id90']/input").click()
driver.find_element_by_name("j_id0:SVMX_FORM:mainBlock:j_id89:0:j_id90").click()
driver.close()
driver.quit()





