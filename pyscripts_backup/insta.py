from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Coordinates of the points to click
points_to_click = [(294.5, 249.58), (149.5, 50)]  # Replace x1, y1, x2, y2 with the coordinates

# Setup Chrome driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Get a list of window handles for all open tabs
window_handles = driver.window_handles

for window_handle in window_handles:
    # Switch to the tab
    driver.switch_to.window(window_handle)

    for point in points_to_click:
        action = ActionChains(driver)
        action.move_to_element_with_offset(driver.find_element(By.TAG_NAME, 'body'), point[0], point[1]).click().perform()
        time.sleep(1)  # Delay between actions, adjust as needed

    driver.close()  # Close the current tab

