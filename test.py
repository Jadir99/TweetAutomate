

from selenium import webdriver
from selenium.webdriver.edge.service import Service

# Path to the newly downloaded WebDriver
edge_driver_path = 'C:\\Users\\hp\\Downloads\\edge_driver\\msedgedriver.exe'
service = Service(edge_driver_path)

# Initialize the WebDriver with the Service object
driver = webdriver.Edge(service=service)

# Your test code here
driver.get('https://www.example.com')

# Always remember to close the driver at the end
# driver.quit()


# # Setup the log in
# sleep(3)
# username = driver.find_element(By.XPATH,"//input[@name='text']")
# username.send_keys("jadir99")
# next_button = driver.find_element(By.XPATH,"//span[contains(text(),'Next')]")
# next_button.click()

# sleep(3)
# password = driver.find_element(By.XPATH,"//input[@name='password']")
# password.send_keys('jadir99jadir99')
# log_in = driver.find_element(By.XPATH,"//span[contains(text(),'Log in')]")
# log_in.click()