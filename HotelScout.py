import os, time, random, importlib
dependancies = ["selenium", "pushbullet.py"]
for i in dependancies:
    try:
        if i == "pushbullet.py": i = "pushbullet"
        importlib.import_module(i)
        print(f"{i} installed")
    except ImportError:
        if i == "pushbullet": i = "pushbullet.py"
        print("installing missing dependancy")
        os.system(f"pip install {i}")
from selenium import webdriver 
from selenium.webdriver.common.by import By
from pushbullet import Pushbullet


driver = webdriver.Firefox()
driver.get("https://www.furryweekend.com/hotels/")
pb_key = os.environ.get("pb_key")
pb = Pushbullet(pb_key)


run = True
while run:
    try:
        driver.refresh()
        driver.implicitly_wait(4)
        booking_link = driver.find_element(By.XPATH, "//p/strong[text()='Booking link']")
        actual_link = driver.execute_script("return arguments[0].nextSibling.textContent.trim();", booking_link)
        if "TBA" not in actual_link: pb.push_note("FWA ROOM BLOCK", actual_link)
        print(f"Current Status{actual_link.strip()}")
        time.sleep(random.uniform(2,4))
    except: 
        pb.push_note("Error Occured", "Page refresh failed. Will re-attempt in 10 seconds")
        time.sleep(10)
driver.close()

    
