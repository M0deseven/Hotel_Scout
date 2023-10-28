import os, time, random
from selenium import webdriver 
from selenium.webdriver.common.by import By
from pushbullet import Pushbullet


driver = webdriver.Firefox()
driver.get("https://www.furryweekend.com/hotels/")
pb_key = os.environ.get("pb_key")
pb = Pushbullet(pb_key)

run = True
while run:
    driver.refresh()
    driver.implicitly_wait(4)
    booking_link = driver.find_element(By.XPATH, "//p/strong[text()='Booking link']")
    actual_link = driver.execute_script("return arguments[0].nextSibling.textContent.trim();", booking_link)
    if "TBA" not in actual_link:
        pb.push_note("FWA ROOM BLOCK", actual_link)
    print(actual_link.strip())
    time.sleep(random.uniform(2,4))
driver.close()

    
