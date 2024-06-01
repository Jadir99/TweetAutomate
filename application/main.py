from automate import TwitterBot
from time import sleep
# Usage
if __name__ == "__main__":
    driver_path = 'edge_driver\\msedgedriver.exe'
    bot = TwitterBot(driver_path)
    
    # Initialize WebDriver
    bot.initialize_driver()
    
    # Login to Twitter
    bot.login('username', 'password')
    sleep(5)
    # Follow a user
    bot.follow('username')
    sleep(4)
    # Unfollow a user
    bot.unfollow('username')
    
    sleep(4)
    # Post a tweet
    bot.add_post('hello from JADIR  team ')
    
    sleep(4)
    # Add a picture to a tweet
    bot.add_pic('path of picture!!')
    
    sleep(4)
    # Add a video to a tweet
    bot.add_video('path of video!!!!')
    
    sleep(4)
    # # Like a tweet
    bot.like_tweet('username', 'id of poste')
    
    sleep(4)
    # Share a tweet
    bot.share_tweet('username', 'id of poste')

    
    # sleep(40)
    sleep(5)
    #  chat 
    bot.chat("username","the message")
    sleep(40)
    # Quit the driver
    bot.quit()
