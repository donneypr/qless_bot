import os
import pyautogui
import pygetwindow as gw
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime, timedelta
import pytz  # 

#pop-up to get the user information such as first,last name and phone number

first_name = input("Please enter your first name: ")
last_name = input("Please enter your last name: ")
phone_number = input("Please enter your phone number: ")
student_id = input("Please enter your student number: ")
student_email = input("Please enter your student email: ")

# Store the data in variables, to avoid private data being available on github 
user_info = {
    "first_name": first_name,
    "last_name": last_name,
    "phone_number": phone_number,
    "student_id": student_id,
    "student_email": student_email
}


def wait_until_nine_am():
    toronto_tz = pytz.timezone("America/Toronto")

    now = datetime.now(toronto_tz)
    print(f"Current Toronto time: {now}")

    target_time = now.replace(hour=9, minute=0, second=0, microsecond=0)

    if now > target_time:
        target_time += timedelta(days=1)

    def countdown_to_target(target_time):
        while True:
            now = datetime.now(target_time.tzinfo)
            time_diff = target_time - now
            
            if time_diff.total_seconds() <= 0:
                print("Time reached!")
                break
        
            remaining_time = str(time_diff).split('.')[0]  
            print(f"Time remaining: {remaining_time}", end='\r')
            time.sleep(1)

    countdown_to_target(target_time)

    print("Starting the program...")

wait_until_nine_am()

# Now that it's 9:00 AM, the script will run

current_directory = os.getcwd()

# Join the directory with the chromedriver file name
chromedriver_path = os.path.join(current_directory, "chromedriver")

# Set up the Selenium driver (for Chrome) using the dynamic path
service = Service(executable_path=chromedriver_path)
driver = webdriver.Chrome(service=service)

driver.get("https://kiosk.ca1.qless.com/kiosk/app/home/19713")

try:
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "body.is-desktop:not(.is-preload)"))
    )
    print("Page is fully loaded and class is `is-desktop` without `is-preload`.")
    
    # Locate and enter first name
    x, y = pyautogui.locateCenterOnScreen("firstname.png", confidence=0.7)
    if x and y:
        pyautogui.moveTo(x / 2, y / 2)  # Adjust for Retina/HiDPI displays
        pyautogui.click()
        pyautogui.write(user_info["first_name"]) 

    # Locate and enter last name
    x1, y1 = pyautogui.locateCenterOnScreen("lastname.png", confidence=0.7)
    if x1 and y1:
        pyautogui.moveTo(x1 / 2, y1 / 2)
        pyautogui.click()
        pyautogui.write(user_info["last_name"]) 

    # Locate and enter cell phone number
    x2, y2 = pyautogui.locateCenterOnScreen("cellphone.png", confidence=0.7)
    if x2 and y2:
        pyautogui.moveTo(x2 / 2, y2 / 2)
        pyautogui.click()
        pyautogui.write(user_info["phone_number"]) 

    # Locate and click on the "Next" button
    x3, y3 = pyautogui.locateCenterOnScreen("next.png", confidence=0.7)
    if x3 and y3:
        pyautogui.moveTo(x3 / 2, y3 / 2)
        pyautogui.click()
    
    x4, y4 = pyautogui.locateCenterOnScreen("studentid.png", confidence=0.7)
    if x4 and y4:
        pyautogui.moveTo(x4 / 2, y4 / 2)
        pyautogui.click()    
        pyautogui.write(user_info["student_id"]) 


    x5, y5 = pyautogui.locateCenterOnScreen("next.png", confidence=0.7)
    if x5 and y5:
        pyautogui.moveTo(x5 / 2, y5 / 2)
        pyautogui.click()    

    x6, y6 = pyautogui.locateCenterOnScreen("interaction.png", confidence=0.7)
    if x6 and y6:
        pyautogui.moveTo(x6 / 2, y6 / 2)
        pyautogui.click()    

    x7, y7 = pyautogui.locateCenterOnScreen("telephone.png", confidence=0.7)
    if x7 and y7:
        pyautogui.moveTo(x7 / 2, y7 / 2)
        pyautogui.click()  

    x8, y8 = pyautogui.locateCenterOnScreen("student_email.png", confidence=0.7)
    if x8 and y8:
        pyautogui.moveTo(x8 / 2, y8 / 2)
        pyautogui.click()  
    
    x9, y9 = pyautogui.locateCenterOnScreen("student_email.png", confidence=0.7)
    if x9 and y9:
        pyautogui.moveTo(x9 / 2, y9 / 2)
        pyautogui.click()    
        pyautogui.write(user_info["student_email"]) 

    x10, y10 = pyautogui.locateCenterOnScreen("next.png", confidence=0.7)
    if x10 and y10:
        pyautogui.moveTo(x10 / 2, y10 / 2)
        pyautogui.click()   

    x11, y11 = pyautogui.locateCenterOnScreen("generalinq.png", confidence=0.7)
    if x11 and y11:
        pyautogui.moveTo(x11 / 2, y11 / 2)
        pyautogui.click() 

    x12, y12 = pyautogui.locateCenterOnScreen("next.png", confidence=0.7)
    if x12 and y12:
        pyautogui.moveTo(x12 / 2, y12 / 2)
        pyautogui.click()       
    time.sleep(5)

except Exception as e:
    print(f"An error occurred: {str(e)}")

finally:
    print("Browser closed.")
