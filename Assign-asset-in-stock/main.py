from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
options = webdriver.ChromeOptions()

import time

# enter automation with shear point that will take us to log in page 
mainURL = "https://office365lds.sharepoint.com/sites/GSDGlobalSupport/MLUOps/SitePages/Missionary-Operations-Team.aspx"
# driver = webdriver.Chrome() 
options = webdriver.ChromeOptions()
userdatadir = "C:\\Users\\Camcamman\\AppData\\Local\\Google\\Chrome\\User Data"
options.add_argument(f"--user-data-dir={userdatadir}")
options.add_argument("--window-size=1300,1000")  # Set initial window size
driver = webdriver.Chrome(options=options)

driver.get(mainURL)
wait = WebDriverWait(driver, 20)

time.sleep(120)

# enter the email in the email box
try: 
    signInTextBox = wait.until(EC.element_to_be_clickable((By.NAME, "loginfmt")))
    signInTextBox.send_keys("camcamman@churchofjesuschrist.org" + Keys.ENTER) 

except TimeoutException: 
    print ("failed on clicking the sign in button to put in email")


# enter the username 
try: 
    signInTextBoxUsername = wait.until(EC.element_to_be_clickable((By.ID, "input28")))
    usernameBox = driver.find_element(By.ID, "input28")
    print (usernameBox)   
    usernameBox.send_keys("camcamman" + Keys.ENTER) 

except: 
    print("input username failed")


# while loop for while i log into the part that i cant automate 
while driver.current_url != mainURL: 
    time.sleep(5)
    print("waiting")

# made it to the main page 
print("made it to main page")

time.sleep(10000)
driver.quit()