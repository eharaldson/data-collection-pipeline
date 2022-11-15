from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

from convert_data import convert

def wait(func):                 # Wait wrapper: sleeps for 2 seconds after a function is completed to make sure website does not think I am a bot
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
    def look_at(self, url):                     # Look at webpage given by url and bypass cookies
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
    def search(self, string):                   # Enter a string into the search bar
        search_bar = self.driver.find_element(by=By.XPATH, value='//*[@id="yfin-usr-qry"]')
        search_bar.click()
        search_bar.send_keys(string)
        search_bar.send_keys(Keys.RETURN)
        self.landing_page = False

    def end_session(self):                      # End the session by quitting the driver
        self.driver.quit()

    @wait
    def scroll_bottom(self):                    # Scroll to the bottom of the page
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    @wait
    def scroll(self, pixels):                   # Scroll to down by pixels
        self.driver.execute_script(f"window.scrollBy(0,{pixels});")

    def ticker_to_link(self, tickers):          # Takes in a list of tickers and returns a list of the links to each tickers statistics and analysis page
        links = []
        for ticker in tickers:
            links.append((f'https://finance.yahoo.com/quote/{ticker}/', ticker))
        return links

    def extract_statistics_page(self):          # Extract data from the statistics page of a ticker

        # Whole table
        table_section = self.driver.find_element(by=By.XPATH, value='//section[@data-test="qsp-statistics"]')
        table_element = table_section.find_elements(by=By.XPATH, value='./div')[-1]
        sub_table_elements = table_element.find_elements(by=By.XPATH, value='./div')

        valuation_measures = sub_table_elements[0]
        valuation_measure_rows = valuation_measures.find_elements(by=By.XPATH, value='.//tr')
        trading_information = sub_table_elements[1]
        trading_information_rows = trading_information.find_elements(by=By.XPATH, value='.//tr')
        financial_highlights = sub_table_elements[2]
        financial_highlight_rows = financial_highlights.find_elements(by=By.XPATH, value='.//tr')

        # Valuation measures
        market_cap = valuation_measure_rows[0].find_elements(by=By.XPATH, value='.//td')[1].text
        market_cap = convert(market_cap)
        trailing_pe = valuation_measure_rows[2].find_elements(by=By.XPATH, value='.//td')[1].text
        trailing_pe = convert(trailing_pe)
        forward_pe = valuation_measure_rows[3].find_elements(by=By.XPATH, value='.//td')[1].text
        forward_pe = convert(forward_pe)
        trailing_ps = valuation_measure_rows[5].find_elements(by=By.XPATH, value='.//td')[1].text
        trailing_ps = convert(trailing_ps)

        # Financial highlights
        profit_margin = financial_highlight_rows[2].find_elements(by=By.XPATH, value='.//td')[1].text
        profit_margin = convert(profit_margin)
        return_on_assets = financial_highlight_rows[4].find_elements(by=By.XPATH, value='.//td')[1].text
        return_on_assets = convert(return_on_assets)
        ebitda = financial_highlight_rows[10].find_elements(by=By.XPATH, value='.//td')[1].text
        ebitda = convert(ebitda)
        current_ratio = financial_highlight_rows[-4].find_elements(by=By.XPATH, value='.//td')[1].text
        current_ratio = convert(current_ratio)

        # Trading information
        short_ratio = trading_information_rows[15].find_elements(by=By.XPATH, value='.//td')[1].text
        short_ratio = convert(short_ratio)
        
        # Collate data into dictionary
        data_dict = {'market_cap': market_cap, 
                    'trailing_pe': trailing_pe, 
                    'forward_pe': forward_pe,
                    'trailing_ps': trailing_ps,
                    'profit_margin': profit_margin,
                    'return_on_assets': return_on_assets,
                    'ebitda': ebitda,
                    'current_ratio': current_ratio,
                    'short_ratio': short_ratio}

        return data_dict

    def extract_summary_page(self):             # Extract data from summary page
        target_estimate = self.driver.find_element(by=By.XPATH, value='//td[@data-test="ONE_YEAR_TARGET_PRICE-value"]').text
        previous_close = self.driver.find_element(by=By.XPATH, value='//td[@data-test="PREV_CLOSE-value"]').text
        data_dict = {'previous_close': float(previous_close), 'target_estimate': float(target_estimate)}

        return data_dict

    def extract_data_ticker(self, link):        # Extract data for one ticker with link inputted into method
        
        # Increment id to ensure each ticker has its own unique id
        self.id += 1

        # Initialise a data dictionary with the specific idea for this ticker
        data = {'id': self.id, 'ticker': link[1]}

        # Visit the tickers yahoo finance page 
        self.look_at(link[0])

        # Extract data from the summary page
        data_summary = self.extract_summary_page()
        data = data | data_summary

        # Move to the statistics page by clicking on the button
        self.driver.find_element(by=By.XPATH, value='//li[@data-test="STATISTICS"]').click()

        # Wait 1 seconds so that the website does not suspect a bot
        time.sleep(1)

        # Extract data from the statistics page
        data_statistics = self.extract_statistics_page()
        data = data | data_statistics

        return data

    def extract_all_data(self, tickers):        # Extract data for each ticker inputted into method

        # Collect a list of links to the tickers to visit
        list_of_links = self.ticker_to_link(tickers)

        # Initialise the ids of the data rows which will then be returned
        self.id = 0

        # Loop through the list of links and extract the data needed
        for link in list_of_links:
            data = self.extract_data_ticker(link)
            print(data)

if __name__ == "__main__":
    
    ticker_list = ['AAPL']
    yahoo_finance = Scraper()

    yahoo_finance.extract_all_data(ticker_list)

    yahoo_finance.end_session()