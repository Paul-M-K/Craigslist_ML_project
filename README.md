#### Project Goal
The goal of this project is to gain insight into vancouver's rental property market, this includes:
* follow rental property trends based on craiglist listings
* help renters gain an understanding of what areas, are within their budget
* *with future goals*
* find rental scams and report them

#### Data Source
The data is obtained from craigslist using the craigslist_scraper.py I wrote. I created my code following this tutorial. https://github.com/vprusso/youtube_tutorials/blob/master/web_scraping_and_automation/selenium/craigstlist_scraper.py
* I would like to improve craigslist_scraper.py in the following ways.
  * Make it possible to scrape all rental pricing automatically without manual manipulation.
  * Make the program scrape craigslist once a day to build the dataset.

#### Data Description
The dataset consists of rental property information in vancouver. The data is Latitude, longitude, accuracy(of location), number of beds, number of baths, square footage, price of property and name of listing.

#### Plots

Here is a plot of the location of properties (latitude vs longitude) along with a colour representation of the price. There are some places to take note. UBC (lat: 49.26, long: -123.25), yaletown (lat: 49.275 -123.125), coal harbour (lat: 49.29, long: -123.125)
* improvement: I want to have an overlay of the vancouver map in the plot. I have done it, but i’ve messed up the scaling.

![housing_prices_scatterplot](https://user-images.githubusercontent.com/20325116/87889585-2eeaf580-c9e7-11ea-9ae2-f8350e439dd1.png)

*issue with scaling*
![vancouver_housing_prices_plot](https://user-images.githubusercontent.com/20325116/87895104-66fb3400-c9f9-11ea-8a0e-ef1cbad2cd5f.png)

This plot shows the correlations between several attributes.

![corrolation_plot](https://user-images.githubusercontent.com/20325116/87895155-898d4d00-c9f9-11ea-918e-e5d82391304a.png)

there are not too many strong correlations, however, the correlations may not be linear. So further investigation is needed
![corr](https://user-images.githubusercontent.com/20325116/87895552-9a8a8e00-c9fa-11ea-9a83-dfce40526118.png)


more things to come! I just need to think more about what I am doing, and how I should present the data.
