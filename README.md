# Data Collection Pipeline
## Milestone 3
- For this project, I decided to do the website scraping on yahoo finance. I thought this would be a good website for this as it is free to use and holds a lot of specific information for several different companies which can then be accessed with the same code. In addition I thought it would be interesting to extend the project by creating a stock screener that would scrape yahoo finance for the relevant data. This aspect would have an interesting use case and I believe is doable in the time frame of the porject.

- In this milestone of the project, I created a scraper class that contains methods to: visit a link, access the search bar, scroll through the page, and convert a list of stock tickers into the specific urls that contain the data for that specifc ticker. The latter method will be useful when extending the project to be a stock screener.

## Milestone 4
- Methods to extract the data that is wanted have been added at this point. These look at the summary page of each company and the statistics page, clicking to get from the former to the latter as this is faster than following the link to the statistics url as the cookies banner will slow down the driver. 

- A raw data folder holds data for each stock in a json file and contains an image file which now holds the downloaded logo for the yahoo finance website which can be found there now with the file name indicating the the date and time downloaded.

- Abstraction has been used to hide some functions in a separate file that contains a function that will convert numbered data in string form from the webscraping. As these functions are similar and could be used in other situations, I decided to put it in a separate file to clean up the yahoo_scraper.py file.

## Milestone 5
- Worked more on creating a general stock screener. The problem is that web scraping using selenium is very slow and to have a screener for all the stocks in the nasdaq (~80,000 stocks) would take several days to complete. Therefore instead I will download data for some stocks I am interested in and performing the screening on these instead.

- Created test files using unittest to ensure proper working order for all the public methods.

## Milestone 6
- The process of creating a stock screener has been slow and therefore to speed up the project I have decided instead to configure the scraper to ask for a letter input. The scraper will then return data on all tickers that start with that letter.

- In this milestone, docker was used to create an image of the scraper program which was then pushed to my docker hub. 