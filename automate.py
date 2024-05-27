from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.edge.service import Service
from pynput.keyboard import Key, Controller

# login to twitter account 
def login():
    # Path to the newly downloaded WebDriver
    edge_driver_path = 'C:\\Users\\hp\\Downloads\\edge_driver\\msedgedriver.exe'
    service = Service(edge_driver_path)

    # Initialize the WebDriver with the Service object
    driver = webdriver.Edge(service=service)

    # Your test code here
    driver.get('https://x.com/i/flow/login')
    # Setup the log in
    sleep(3)
    username = driver.find_element(By.XPATH,"//input[@name='text']")
    username.send_keys("jadir99")
    next_button = driver.find_element(By.XPATH,"//span[contains(text(),'Next')]")
    next_button.click()

    sleep(3)
    password = driver.find_element(By.XPATH,"//input[@name='password']")
    password.send_keys('jadir99jadir99')
    log_in = driver.find_element(By.XPATH,"//span[contains(text(),'Log in')]")
    log_in.click()

# follow
def add_freind():
    name="Cristiano"
    url="https://twitter.com/"+name
    driver.get(url)
    sleep(3)
    follow=driver.find_element(By.XPATH,"//span[contains(text(),'Follow')]")
    follow.click()

# unfollow
def Unfollow():
    name="Cristiano"
    url="https://twitter.com/"+name
    driver.get(url)
    sleep(3)
    if driver.find_element(By.XPATH,"//span[contains(text(),'Following')]"):
        follow=driver.find_element(By.XPATH,"//span[contains(text(),'Following')]")
        follow.click()
        follow=driver.find_element(By.XPATH,"//span[@class='css-1jxf684 r-bcqeeo r-1ttztb7 r-qvutc0 r-poiln3' and text()='Unfollow']")
        follow.click()



# add post 
def add_post():
    url="https://twitter.com/home"
    driver.get(url)
    sleep(3)
    follow=driver.find_element(By.XPATH,"//span[contains(text(),'Post')]")
    follow.click()
    sleep(2)
    publicite=driver.find_element(By.XPATH,"//span[@data-text='true']") 
    publicite.send_keys('hello world from python and jadir mohammed')
    follow=driver.find_element(By.XPATH,"//span[contains(text(),'Post')]")
    follow.click()
    
# add picture 
def add_pic():
    image_path="C:/Users/hp/OneDrive/Bureau/advanced_python_project/le projet/imgs/hackathon.jpg"
    # Find the add photo button and click it to open the file upload dialog
    add_photo_button = driver.find_element(By.XPATH,"//input[@data-testid='fileInput']")
    add_photo_button.send_keys(image_path)

    # Wait for the image to be uploaded
    sleep(2)  # Adjust this time as needed

    # Find the tweet button and submit the tweet
    post=driver.find_element(By.XPATH,"//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button/div/span/span")
    post.click()

# add video 
def add_video():
    image_path="C:/Users/hp/OneDrive/Bureau/advanced_python_project/le projet/videos/hackathon.mp4"
    # Find the add photo button and click it to open the file upload dialog
    add_photo_button = driver.find_element(By.XPATH,"//input[@data-testid='fileInput']")
    add_photo_button.send_keys(image_path)

    # Wait for the image to be uploaded
    sleep(20)  # Adjust this time as needed

    # Find the tweet button and submit the tweet
    post=driver.find_element(By.XPATH,"//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button/div/span/span")
    post.click()

# like for tweet 
# // function of like and ommen
def like_tweet():
    id_post='1794605275850371199'
    username="elonmusk"
    url="https://twitter.com/"+username+"/status/"+id_post
    driver.get(url)
    sleep(3)
   
    like_button=driver.find_element(By.XPATH,"//button[contains(@aria-label, 'Likes. Like') and @data-testid='like']") 
    # Click the like button
    like_button.click()

# # // function of share
def share_tweet():
    id_post='1794605275850371199'
    username="elonmusk"
    url="https://twitter.com/"+username+"/status/"+id_post
    driver.get(url)
    sleep(3)
   
    like_button=driver.find_element(By.XPATH,"//button[contains(@aria-label, 'reposts. Repost')]") 
    # Click the like button
    like_button.click()
    sleep(1)
    if driver.find_element(By.XPATH,"//span[contains(text(),'Repost')]"):
        repost=driver.find_element(By.XPATH,"//span[contains(text(),'Repost')]")
        repost.click()
    return "deja reposted"


# message between 2 users 
def message():
    pass