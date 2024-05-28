from automate import TwitterBot
from time import sleep
# Usage
if __name__ == "__main__":
    driver_path = 'C:\\Users\\hp\\Downloads\\edge_driver\\msedgedriver.exe'
    bot = TwitterBot(driver_path)
    
    # Initialize WebDriver
    bot.initialize_driver()
    
    # Login to Twitter
    bot.login('jadir99', 'jadir99jadir99')
    sleep(5)
    # Follow a user
    bot.follow('Cristiano')
    sleep(4)
    # Unfollow a user
    bot.unfollow('Cristiano')
    
    sleep(4)
    # Post a tweet
    bot.add_post('hellofrom medpy team ')
    
    sleep(4)
    # Add a picture to a tweet
    bot.add_pic('C:\\Users\\hp\\OneDrive\\Bureau\\advanced_python_project\\le projet\\application\\static\\imgs\\hackathon.jpg')
    
    sleep(4)
    # Add a video to a tweet
    bot.add_video('C:\\Users\\hp\\OneDrive\\Bureau\\advanced_python_project\\le projet\\application\\static\\videos\\hackathon.mp4')
    
    sleep(4)
    # # Like a tweet
    bot.like_tweet('AIDRIVR', '1794887169162850588')
    
    sleep(4)
    # Share a tweet
    bot.share_tweet('AIDRIVR', '1794887169162850588')

    
    # sleep(40)
    sleep(5)
    #  chat 
    bot.chat("jadir999","salam si jadir cv hanya malin dar kchi mzn  ???")
    sleep(40)
    # Quit the driver
    # bot.quit()
