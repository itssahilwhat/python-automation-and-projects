import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

PROMISED_DOWN = 80
PROMISED_UP = 10
TWITTER_EMAIL = ''
TWITTER_PASSWORD = ''




class InternetSpeedTwitterBot:
    def __init__(self):
        edge_options = webdriver.EdgeOptions()
        edge_options.add_experimental_option("detach", True)
        self.driver = webdriver.Edge(options=edge_options)

        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get('https://www.speedtest.net/')

        time.sleep(3)
        continue_btn = self.driver.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]')
        continue_btn.click()

        time.sleep(3)
        go = self.driver.find_element(By.ID, '/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
        go.click()

        time.sleep(60)
        self.down = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        self.up = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text

        print(f'Down: {self.down} \nUp: {self.up}')

    def tweet_at_provider(self):
        self.driver.get('https://x.com/')
        time.sleep(3)

        sign_in = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div/div/div[3]/div[4]/a')
        sign_in.click()
        time.sleep(3)

        email = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div/div[4]/label/div/div[2]/div/input')
        email.send_keys(TWITTER_EMAIL, Keys.ENTER)
        time.sleep(3)

        password = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div[1]/div/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        password.send_keys(TWITTER_PASSWORD, Keys.ENTER)

        tweet = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div/div/div/div/div/span')
        tweet.send_keys(f'Hey Internet Provider, why is my internet speed\n{self.down}down/{self.up}up when i pay for 150down/10up?')

        post = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button')
        post.click()


obj = InternetSpeedTwitterBot()
obj.get_internet_speed()
obj.tweet_at_provider()


