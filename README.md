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
![housing_prices_scatterplot](https://user-images.githubusercontent.com/20325116/87889585-2eeaf580-c9e7-11ea-9ae2-f8350e439dd1.png)

![vancouver_housing_prices_plot](https://user-images.githubusercontent.com/20325116/88244264-26ddc080-cc48-11ea-8721-7a785b1eee75.png)

This plot shows the correlations between several attributes.

![corrolation_plot](https://user-images.githubusercontent.com/20325116/87895155-898d4d00-c9f9-11ea-918e-e5d82391304a.png)

there are not too many strong correlations, however, the correlations may not be linear. So further investigation is needed
![corr](https://user-images.githubusercontent.com/20325116/87895552-9a8a8e00-c9fa-11ea-9a83-dfce40526118.png)

The dataset is stratified to ensure there is no bias. The labels are removed from the data set for training. 

Selecting the training model was done by comparing several different methods together by using cross validation using 10 folds for each model. The results were as followed:
Linear regression: rmse 410.297 (mean) std: 15.974
Decision TreeRegression: rmse 526.377 (mean), std: 25.397 
RandomForestRegressor: rmse 389.414 (mean), std: 21.371

RandomForestRegressor seems to be the most promising model for this dataset. Therefore I am performing a GridSearchCV to help to determine the optimal hyperparameters. It is determined that the max_features hyperparameter to be 4 and the n_estimators hyperparameter to be 30. This yields a rmse of 390.996. 

I messed up the dataset. I should not be using the accuracy attribute because it is completly independant of all other attributes. I left it in there because eventually I want to use it as a weight factor for each listing.

