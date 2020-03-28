# Launch the code and it will open chrome with whatsapp automatically. Scan the QR Code with your mobile
# whatsapp so that your contacts load into webpage. You have to download Chromedriver first. You also  have to
# install selenium library. I did it by writing "pip install selenium" in command prompt. You have to make sure
# you have pip pre installed. Otherwise you have to install pip first and then selenium library.
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import os

def test():

    name=input("Enter the name of person or group: ")
    count=eval(input("How many times: "))
    sleeping=eval(input("How many seconds delay?: "))

    dir_path = os.path.dirname(os.path.realpath(__file__))
    driver=webdriver.Chrome(dir_path+"\chromedriver.exe")

    driver.get("https://web.whatsapp.com/")

    xpath='//span[@title="{}"]'.format(name)
    print(xpath)
    user=WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.XPATH,xpath)))

    try:
        user.click()
    except:
        print ('StaleElementReferenceException while trying to type password, trying to find element again')
        user=WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH,xpath)))
        user.click()

    
    msg_box=WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CLASS_NAME,'_1Plpp')))
    for i in range(count):
        user = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "[title^='Attach']"))
        )
        user.click()
        button=WebDriverWait(driver, 8).until(EC.element_to_be_clickable((By.CLASS_NAME, 'GK4Lv'))) # Purple icon
        driver.implicitly_wait(1)
        
        try:
            button.click()
        except:
            driver.implicitly_wait(1.5)
            button.click()
        dir_path = os.path.dirname(os.path.realpath(__file__))

        x=dir_path + r"\\urdu.exe"
        os.startfile(x)
        # os.startfile(r"D:\\Programming\\python\\whatsapp\\speech_voice\\urdu.exe")
        button=WebDriverWait(driver, 12).until(EC.element_to_be_clickable((By.CLASS_NAME, '_3nfoJ'))) # send icon
        button.click()
        time.sleep(4)
        time.sleep(sleeping)

test()