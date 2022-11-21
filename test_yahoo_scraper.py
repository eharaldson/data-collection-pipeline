import unittest
from yahoo_scraper import Scraper
import os

class ScraperTestCase(unittest.TestCase):

    def test_ticker_to_link(self):
        self.scraper = Scraper()
        tickers = ['AAPL', 'AMZN', 'TSLA']
        expected_list = [('https://finance.yahoo.com/quote/AAPL/', 'AAPL'), ('https://finance.yahoo.com/quote/AMZN/', 'AMZN'), ('https://finance.yahoo.com/quote/TSLA/', 'TSLA')]
        actual_list = self.scraper.ticker_to_link(tickers)
        assert actual_list == expected_list

        self.scraper.end_session()

    def test_extract_all_data(self):
        self.scraper = Scraper()
        tickers = ['AAPL', 'AMZN', 'GOOG']
        data = self.scraper.extract_all_data(tickers)

        for key in data:
            assert len(data[key]) == 3
            if key != 'id' and key != 'ticker':
                for x in data[key]:
                    assert isinstance(x, float) or isinstance(x, int)
        
        assert len(data) == 13
        assert data['ticker'] == tickers

        self.scraper.end_session()

    def test_extract_logo(self):
        self.scraper = Scraper()
        self.scraper.look_at('https://finance.yahoo.com/quote/AAPL/')
        self.scraper.extract_logo()
        current_directory = os.getcwd()
        final_directory = os.path.join(current_directory, 'raw_data/images')
        list_files = os.listdir(final_directory)
        assert list_files[0][-3:] == 'png'

        self.scraper.end_session()

unittest.main(argv=[''], verbosity=2, exit=False)