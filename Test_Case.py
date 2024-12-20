import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
import pyperclip

executable_path = 'C:/Users/UsamaSiddique/PycharmProjects/Galileo_Protocol/chromedriver/chromedriver.exe'

chrome_options = webdriver.ChromeOptions()
# '''
# Try this code to open Google account Profile and extensions
# Chrome_Profile = r'C:\Users\UsamaSiddique\AppData\Local\Google\Chrome\User Data'
# chrome_options.add_argument(f"user-data-dir={Chrome_Profile}")
# chrome_options.add_argument("--load-extension=C:/Users/UsamaSiddique/AppData/Local/Google/Chrome/User Data/extensions_crx_cache")
# driver.get("https://myaccount.google.com/")
# '''
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--start-maximized")


driver = webdriver.Chrome(options=chrome_options)

driver.get('https://staging.galileoprotocol.io/login')

Email = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/div[2]/div/div/div[2]/div/div[1]/div[2]/div/div/div/div/div/div/div[1]/div/ul/li/div/div[2]/div/input")))
Email.send_keys("user22@mailinator.com")

Email_Click = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH,"/html/body/div[1]/div[2]/div/div/div[2]/div/div[1]/div[2]/div/div/div/div/div/div/div[1]/div/ul/li/div/div[2]/div/button")))
Email_Click.click()

driver.execute_script("window.open('https://www.google.com','_blank');")

driver.switch_to.window(driver.window_handles[1])

driver.get('https://www.mailinator.com')
time.sleep(2)

GetFreeTrail = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/header[1]/div[2]/div/div/div/nav/ul/li[6]/a/span'))
)
GetFreeTrail.click()
time.sleep(2)

XButton = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/div/div/div[1]/button'))
)
XButton.click()
time.sleep(2)

SearchBar = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/main/div[2]/div[1]/div[5]/form/input'))
)
SearchBar.send_keys('user22')
time.sleep(2)

GoButton = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/main/div[2]/div[1]/div[5]/form/button'))
)
GoButton.click()
time.sleep(2)

MEmail = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, '/html/body/div[1]/main/div[2]/div[3]/div/div[4]/div/div/table/tbody/tr/td[2]'))
)
MEmail.click()
time.sleep(2)
iframe_index = 0
driver.switch_to.frame(iframe_index)

OTP = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/h2'))
)
time.sleep(5)

# Get the text from the element
text_to_copy = OTP.text

# Use pyperclip to copy text to the clipboard
pyperclip.copy(text_to_copy)

driver.switch_to.window(driver.window_handles[0])
time.sleep(5)

Enter_OTP = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH,
                                    "/html/body/div[1]/div[2]/div/div/div[2]/div/div[1]/div[2]/div/div/div/div/div/div/div[2]/form/div[2]/div/div[2]/input"))
)
Enter_OTP.click()
Enter_OTP.send_keys(Keys.CONTROL, 'V')
time.sleep(30)

Current_Url = driver.current_url

Expected_Url = 'https://staging.galileoprotocol.io/signUp'

if Current_Url == Expected_Url:
    FirstName = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "/html/body/div[1]/div[2]/div/div/div[2]/div/div[2]/div/form/div[1]/div/div/input"))
    )
    FirstName.send_keys("User")
    LastName = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "/html/body/div[1]/div[2]/div/div/div[2]/div/div[2]/div/form/div[2]/div/div/input"))
    )
    LastName.send_keys("20")
    Check_Box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "/html/body/div[1]/div[2]/div/div/div[2]/div/div[2]/div/form/div[5]/div[1]/label/span[1]/input"))
    )
    Check_Box.click()
    time.sleep(5)

    SignUp_Button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "/html/body/div[1]/div[2]/div/div/div[2]/div/div[2]/div/form/div[5]/div[4]/div/button"))
    )
    SignUp_Button.click()
    time.sleep(5)

    KYC_Later = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//button[text()='i’ll do it later']"))
    )
    KYC_Later.click()
    time.sleep(5)
else:
    print("")

Market_Place = WebDriverWait(driver, 10).until(
EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[1]/div[2]/div/div[1]/div[2]/div/span"))
)
Market_Place.click()
time.sleep(5)
NFT = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, " /html/body/div[1]/div[2]/div[1]/div[3]/div[2]/div/div/div/div[2]/div/button/div[1]/img"))
)
NFT.click()
time.sleep(5)
Redeem_Button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/div[2]/div[1]/div[3]/div[2]/div/div/div/div/div[1]/div[1]/div/div/div[2]/div/div/div/div[7]/div/div/div/button"))
)
Redeem_Button.click()
time.sleep(2)

driver.quit()
