from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

def wait(func):     # Wait wrapper: sleeps for 2 seconds after a function is completed to make sure website does not think I am a bot
    def wrapper(*args, **kwargs):
        output = func(*args, **kwargs)
        time.sleep(2)
        return output
    return wrapper

class Scraper:      # Class with methods to scrape websites

    # Constructor
    def __init__(self):
        self.driver = webdriver.Chrome() 
        self.landing_page = True

    # Methods
    @wait
    def look_at(self, url):         # Look at webpage given by url and bypass cookies
        self.driver.get(url)
        time.sleep(2)
        delay = 10
        try:
            WebDriverWait(self.driver, delay).until(EC.presence_of_element_located((By.XPATH, '//div[@class="con-wizard"]')))
            accept_cookies_button = WebDriverWait(self.driver, delay).until(EC.presence_of_element_located((By.XPATH, '//button[@class="btn primary"]')))
            accept_cookies_button.click()
        except TimeoutException:
            print("Loading took too much time!")

    @wait
    def search(self, string):       # Enter a string into the search bar
        search_bar = self.driver.find_element(by=By.XPATH, value='//*[@id="yfin-usr-qry"]')
        search_bar.click()
        search_bar.send_keys(string)
        search_bar.send_keys(Keys.RETURN)

    def end_session(self):          # End the session by quitting the driver
        self.driver.quit()

    @wait
    def scroll_bottom(self):        # Scroll to the bottom of the page
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    @wait
    def scroll(self, pixels):       # Scroll to down by pixels
        self.driver.execute_script(f"window.scrollBy(0,{pixels});")

    def ticker_to_link(tickers):    # Takes in a list of tickers and returns a list of the links to each tickers page
        links = []
        for ticker in tickers:
            links.append(f'https://finance.yahoo.com/quote/{ticker}/')
        return links

yahoo_finance = Scraper()

yahoo_finance.look_at('https://uk.finance.yahoo.com/')
yahoo_finance.search('AAPL')

yahoo_finance.scroll_bottom()

yahoo_finance.end_session()