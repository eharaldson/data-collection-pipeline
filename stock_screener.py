from yahoo_scraper import Scraper
from yahoo_scraper import wait, create_folder, save_json, download_img
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QFormLayout, QLabel, QLineEdit, QMainWindow, QDialogButtonBox, QVBoxLayout, QGroupBox

import pandas as pd
import sys

class StockScreener:

    # Constructor
    def __init__(self, ticker_data) :
        self.ticker_data = ticker_data
        self.start_up()

    # Methods
    def getInfo(self):                      # Method called when OK pressed: Take in user input and then show correct data
        
        mkt_cap_minimum = self.mkt_cap_line_edit_minimum.text()
        mkt_cap_maximum = self.mkt_cap_line_edit_maximum.text()

        trailing_pe_minimum = self.trailing_pe_line_edit_minimum.text()
        trailing_pe_maximum = self.trailing_pe_line_edit_maximum.text()

        forward_pe_minimum = self.forward_pe_line_edit_minimum.text()
        forward_pe_maximum = self.forward_pe_line_edit_maximum.text()

        price_sales_minimum = self.price_sales_line_edit_minimum.text()
        price_sales_maximum = self.price_sales_line_edit_maximum.text()

        profit_margin_minimum = self.profit_margin_line_edit_minimum.text()
        profit_margin_maximum = self.profit_margin_line_edit_maximum.text()

        return_on_assets_minimum = self.return_on_assets_line_edit_minimum.text()
        return_on_assets_maximum = self.return_on_assets_line_edit_maximum.text()

        ebitda_minimum = self.ebitda_line_edit_minimum.text()
        ebitda_maximum = self.ebitda_line_edit_maximum.text()

        current_ratio_minimum = self.current_ratio_line_edit_minimum.text()
        current_ratio_maximum = self.current_ratio_line_edit_maximum.text()

        short_ratio_minimum = self.short_line_edit_minimum.text()
        short_ratio_maximum = self.short_line_edit_maximum.text()

        self.window.close()

    def cancel(self):                       # Method called when CANCEL pressed: Exit the window
        self.window.close()

    def mkt_cap_row(self):                  # Creates market cap row
        self.mkt_cap_layout = QHBoxLayout()
        self.mkt_cap_layout.addWidget(QLabel('Market Cap ($USD Millions):'))
        self.mkt_cap_line_edit_minimum = QLineEdit()
        self.mkt_cap_line_edit_minimum.setPlaceholderText("Min")
        self.mkt_cap_layout.addWidget(self.mkt_cap_line_edit_minimum)
        self.mkt_cap_line_edit_maximum = QLineEdit()
        self.mkt_cap_line_edit_maximum.setPlaceholderText("Max")
        self.mkt_cap_layout.addWidget(self.mkt_cap_line_edit_maximum)

        self.form_layout.addRow(self.mkt_cap_layout)

    def trailing_pe_row(self):              # Creates trailing p/e row
        self.trailing_pe_layout = QHBoxLayout()
        self.trailing_pe_layout.addWidget(QLabel('Trailing Price/Earnings:'))
        self.trailing_pe_line_edit_minimum = QLineEdit()
        self.trailing_pe_line_edit_minimum.setPlaceholderText("Min")
        self.trailing_pe_layout.addWidget(self.trailing_pe_line_edit_minimum)
        self.trailing_pe_line_edit_maximum = QLineEdit()
        self.trailing_pe_line_edit_maximum.setPlaceholderText("Max")
        self.trailing_pe_layout.addWidget(self.trailing_pe_line_edit_maximum)

        self.form_layout.addRow(self.trailing_pe_layout)

    def forward_pe_row(self):               # Creates forward p/e row
        self.forward_pe_layout = QHBoxLayout()
        self.forward_pe_layout.addWidget(QLabel('Forward Price/Earnings:'))
        self.forward_pe_line_edit_minimum = QLineEdit()
        self.forward_pe_line_edit_minimum.setPlaceholderText("Min")
        self.forward_pe_layout.addWidget(self.forward_pe_line_edit_minimum)
        self.forward_pe_line_edit_maximum = QLineEdit()
        self.forward_pe_line_edit_maximum.setPlaceholderText("Max")
        self.forward_pe_layout.addWidget(self.forward_pe_line_edit_maximum)

        self.form_layout.addRow(self.forward_pe_layout)

    def price_sales_row(self):               # Creates p/s row
        self.price_sales_layout = QHBoxLayout()
        self.price_sales_layout.addWidget(QLabel('Sales/Earnings:'))
        self.price_sales_line_edit_minimum = QLineEdit()
        self.price_sales_line_edit_minimum.setPlaceholderText("Min")
        self.price_sales_layout.addWidget(self.price_sales_line_edit_minimum)
        self.price_sales_line_edit_maximum = QLineEdit()
        self.price_sales_line_edit_maximum.setPlaceholderText("Max")
        self.price_sales_layout.addWidget(self.price_sales_line_edit_maximum)

        self.form_layout.addRow(self.price_sales_layout)

    def profit_margin_row(self):                # Creates profit margin row
        self.profit_margin_layout = QHBoxLayout()
        self.profit_margin_layout.addWidget(QLabel('Profit margin (%):'))
        self.profit_margin_line_edit_minimum = QLineEdit()
        self.profit_margin_line_edit_minimum.setPlaceholderText("Min")
        self.profit_margin_layout.addWidget(self.profit_margin_line_edit_minimum)
        self.profit_margin_line_edit_maximum = QLineEdit()
        self.profit_margin_line_edit_maximum.setPlaceholderText("Max")
        self.profit_margin_layout.addWidget(self.profit_margin_line_edit_maximum)

        self.form_layout.addRow(self.profit_margin_layout)

    def return_on_assets_row(self):                # Creates Return on assets row
        self.return_on_assets_layout = QHBoxLayout()
        self.return_on_assets_layout.addWidget(QLabel('Return on assets (%):'))
        self.return_on_assets_line_edit_minimum = QLineEdit()
        self.return_on_assets_line_edit_minimum.setPlaceholderText("Min")
        self.return_on_assets_layout.addWidget(self.return_on_assets_line_edit_minimum)
        self.return_on_assets_line_edit_maximum = QLineEdit()
        self.return_on_assets_line_edit_maximum.setPlaceholderText("Max")
        self.return_on_assets_layout.addWidget(self.return_on_assets_line_edit_maximum)

        self.form_layout.addRow(self.return_on_assets_layout)

    def ebitda_row(self):                           # Creates EBITDA row
        self.ebitda_layout = QHBoxLayout()
        self.ebitda_layout.addWidget(QLabel('EBITDA ($USD millions):'))
        self.ebitda_line_edit_minimum = QLineEdit()
        self.ebitda_line_edit_minimum.setPlaceholderText("Min")
        self.ebitda_layout.addWidget(self.ebitda_line_edit_minimum)
        self.ebitda_line_edit_maximum = QLineEdit()
        self.ebitda_line_edit_maximum.setPlaceholderText("Max")
        self.ebitda_layout.addWidget(self.ebitda_line_edit_maximum)

        self.form_layout.addRow(self.ebitda_layout)

    def current_ratio_row(self):                    # Creates current ratio row
        self.current_ratio_layout = QHBoxLayout()
        self.current_ratio_layout.addWidget(QLabel('Current ratio:'))
        self.current_ratio_line_edit_minimum = QLineEdit()
        self.current_ratio_line_edit_minimum.setPlaceholderText("Min")
        self.current_ratio_layout.addWidget(self.current_ratio_line_edit_minimum)
        self.current_ratio_line_edit_maximum = QLineEdit()
        self.current_ratio_line_edit_maximum.setPlaceholderText("Max")
        self.current_ratio_layout.addWidget(self.current_ratio_line_edit_maximum)

        self.form_layout.addRow(self.current_ratio_layout)

    def short_row(self):                    # Creates short ratio row
        self.short_layout = QHBoxLayout()
        self.short_layout.addWidget(QLabel('Short ratio:'))
        self.short_line_edit_minimum = QLineEdit()
        self.short_line_edit_minimum.setPlaceholderText("Min")
        self.short_layout.addWidget(self.current_ratio_line_edit_minimum)
        self.short_line_edit_maximum = QLineEdit()
        self.short_line_edit_maximum.setPlaceholderText("Max")
        self.short_layout.addWidget(self.short_line_edit_maximum)

        self.form_layout.addRow(self.short_layout)

    def start_up(self):                     # Method that is called to start up the interface to get the filters for the screener
        
        self.app = QApplication([])
        self.app.setStyle('Macintosh')
        self.window = QWidget()
        self.window.setWindowTitle('Stock Screener')

        # Create layout form
        self.form_layout = QFormLayout()

        # Create all the rows for the form
        self.formGroupBox = QGroupBox("Please enter a minimum or maximum value. Leave blank to remove filter")
        self.mkt_cap_row()
        self.trailing_pe_row()
        self.forward_pe_row()
        self.price_sales_row()
        self.profit_margin_row()
        self.return_on_assets_row()
        self.ebitda_row()
        self.current_ratio_row()
        self.short_row()

        self.formGroupBox.setLayout(self.form_layout)

        # creating a dialog button for ok and cancel
        self.buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
  
        # adding action when form is accepted
        self.buttonBox.accepted.connect(self.getInfo)
  
        # adding action when form is rejected
        self.buttonBox.rejected.connect(self.cancel)
  
        # Creating main layout
        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(self.formGroupBox)
        self.main_layout.addWidget(self.buttonBox)
  
        # setting lay out
        self.window.setLayout(self.main_layout)

        self.window.show()
        self.app.exec()

def main():
    ticker_list = ['AAPL']
    data = pd.read_csv('nasdaq_tickers.csv', index_col=False)
    stock_screener = StockScreener(data)

if __name__ == "__main__":
    main()