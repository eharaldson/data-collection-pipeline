# Data Collection Pipeline

In this project I will use the selenium module with python to scrape a website for both image and tabular data.

I decided on the yahoo finance website as it holds a lot of data points in a structured format and I am very interested in investing in general so I though it would be interesting.

I will create an app that asks a user for a letter and will then save a csv file of important data points (e.g. price/earnings, 1 year target estimate, profit margin ...) for each stock for which the ticker starts with the letter inputted.

The application will be containerised in a Docker image so that it is easily deployable by anyone who accesses my Docker account.

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

- During the containerisation of the scraper image I ran into errors where the Selenium webdriver would crash and so none of my code which originally worked would run. To fix this I implemented the following options to apply to the webdriver...

```
options = Options()
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')     
options.headless = True
self.driver = webdriver.Chrome(options=options)
```

- The `--no-sandbox` option is added to work around the issue of chrome being run as the root user. The `--disable-dev-shm-usage` option is added as the dev/shm partition is too small. Further info on these options can be found here https://rstudio.github.io/chromote/reference/default_chrome_args.html.

## Milestone 7
- I have now created a yaml file in the workflows folder in the .github folder of this directory. Github actions are basically processes defined by you that are carried out on a GitHub server (runner) upon an event happening; such as a push onto the main branch which is what I have implemented. This feature is useful in the continuous integration and continuous deployment are practices used in software development which reference the incremental updating of your software so as to improve performance and user experience. For example I could create a github action that runs a test file when a new push is made and if this is successful the deployment of the new code can be done. 

- The workflow of the action is configured in a yaml file: docker-image.yml in this project. My GitHub action checks out my repository using a `actions/checkout@v3` command which is pre built so that I do not have to write all the code to do this myself. It then builds an image from the directory and logs in to my docker hub to then push this image to my hub. The full `docker-image.yml` script is shown below:

```
name: Docker Image CI

on:
  push:
    branches: [ "main" ]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3

    - name: Build the Docker image locally
      run: docker build . --file Dockerfile --tag erikhara/yahoo_scraper:latest

    - name: Login to Docker Hub
      uses: docker/login-action@v2
      with:
        username: ${{ secrets.DOCKER_HUB_USERNAME }}
        password: ${{ secrets.DOCKER_HUB_ACCESS_TOKEN }}

    - name: Push Docker image to hub
      run: docker push erikhara/yahoo_scraper:latest
```
