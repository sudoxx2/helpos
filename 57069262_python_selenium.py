from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# these two imports are for setting up firefox driver and options 
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
# import these three lines below if you are having synchronization issues
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


profile = webdriver.FirefoxProfile()
# here is where you need to set your language explicitly if its defaulting to an undesired language
# just replace the second parameter with your 2 character language code
# this line is not needed if your desired language is locale
profile.set_preference("intl.accept_languages",'de')
# throw in your path here <insert_your_gecko_driver_path_here>
driver = webdriver.Firefox(firefox_profile=profile, executable_path='<insert_your_gecko_driver_path_here>')

driver.get("https://instagram.com/")

# added these two lines below to solve synchronization issue 
# element wasnt clickable until page finished loading
wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Melde dich an.")))
#next command fails 
driver.find_element_by_link_text("Melde dich an.").click()

#if the first command is skipped by entering in the url 
#in driver.get(https://www.instagram.com/accounts/login/?source=auth_switcher)
#the following command fails as well.
driver.find_element_by_name("username").send_keys("HereIsTheUsername")
driver.find_element_by_name("password").send_keys("HereIsThePassword")
driver.find_element_by_name("password").send_keys(Keys.RETURN)
driver.close()
