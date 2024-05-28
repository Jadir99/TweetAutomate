from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.edge.service import Service
from pynput.keyboard import Key, Controller



from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from time import sleep

class TwitterBot:
    def __init__(self, driver_path):
        self.driver_path = driver_path
        self.service = Service(self.driver_path)
        self.driver = None  # Declare the driver variable

    def initialize_driver(self):
        self.driver = webdriver.Edge(service=self.service)

    def login(self, username, password):
        self.driver.get('https://x.com/i/flow/login')
        sleep(3)
        username_field = self.driver.find_element(By.XPATH, "//input[@name='text']")
        username_field.send_keys(username)
        next_button = self.driver.find_element(By.XPATH, "//span[contains(text(),'Next')]")
        next_button.click()
        sleep(3)
        password_field = self.driver.find_element(By.XPATH, "//input[@name='password']")
        password_field.send_keys(password)
        login_button = self.driver.find_element(By.XPATH, "//span[contains(text(),'Log in')]")
        login_button.click()

    def follow(self, name):
        url = f"https://twitter.com/{name}"
        self.driver.get(url)
        sleep(3)
        follow_button = self.driver.find_element(By.XPATH, "//span[contains(text(),'Follow')]")
        follow_button.click()

    def unfollow(self, name):
        url = f"https://twitter.com/{name}"
        self.driver.get(url)
        sleep(3)
        following_button = self.driver.find_element(By.XPATH, "//span[contains(text(),'Following')]")
        following_button.click()
        unfollow_button = self.driver.find_element(By.XPATH, "//span[text()='Unfollow']")
        unfollow_button.click()

    def add_post(self, text):
        self.driver.get("https://twitter.com/home")
        sleep(3)
        post_button = self.driver.find_element(By.XPATH, "//span[contains(text(),'Post')]")
        post_button.click()
        sleep(2)
        post_area = self.driver.find_element(By.XPATH, "//span[@data-text='true']")
        post_area.send_keys(str(text))
        tweet_button = self.driver.find_element(By.XPATH, "//span[contains(text(),'Post')]")
        tweet_button.click()

    def add_pic(self, image_path):
        self.driver.get("https://twitter.com/home")
        sleep(3)
        add_photo_button = self.driver.find_element(By.XPATH, "//input[@data-testid='fileInput']")
        add_photo_button.send_keys(image_path)
        sleep(2)
        tweet_button = self.driver.find_element(By.XPATH, "//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button/div/span/span")
        tweet_button.click()

    def add_video(self, video_path):
        self.driver.get("https://twitter.com/home")
        sleep(3)
        add_photo_button = self.driver.find_element(By.XPATH, "//input[@data-testid='fileInput']")
        add_photo_button.send_keys(video_path)
        sleep(160)
        tweet_button = self.driver.find_element(By.XPATH, "//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button/div/span/span")
        tweet_button.click()

    def like_tweet(self, username, tweet_id):
        url = f"https://twitter.com/{str(username)}/status/{str(tweet_id)}"
        self.driver.get(url)
        sleep(3)
        like_button = self.driver.find_element(By.XPATH, "//button[contains(@aria-label, 'Likes. Like') and @data-testid='like']")
        like_button.click()

    def share_tweet(self, username, tweet_id):
        url = f"https://twitter.com/{str(username)}/status/{str(tweet_id)}"
        self.driver.get(url)
        sleep(3)
        share_button = self.driver.find_element(By.XPATH, "//button[contains(@aria-label, 'reposts. Repost')]")
        share_button.click()
        sleep(1)
        repost_button = self.driver.find_element(By.XPATH, "//span[contains(text(),'Repost')]")
        repost_button.click()

    def chat(self,username,message):
        message_butt = self.driver.find_element(By.XPATH, "//a[@href='/messages']")
        message_butt.click()
        sleep(2)
        user = self.driver.find_element(By.XPATH, "//span[text()='"+str(username)+"']")
        user.click()
        sleep(3)
        username_field = self.driver.find_element(By.XPATH, "//span[@data-text='true']")
        username_field.send_keys(str(message))
        send_button = self.driver.find_element(By.XPATH, "//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[2]/div/div/aside/div[2]/button/div")
        send_button.click()


        

