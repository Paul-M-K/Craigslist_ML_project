#### Project Goal
The goal of this project is to gain insight into vancouver's rental property market, this includes:

**Main objective**

* Use machine learning to accurately predict the price of rental property based on attributes that can be extracted from craigslist.

**Sub Objectives**

* Find a hosting site:
  * Scrape data from craigslist once per day to develop more robust algorithms
  * Follow rental property trends
  * Build interactive site for users
* find rental scams and report them (have self reporting of scams in order to develop a model for scams)

#### Data Source
The data is obtained from craigslist using the craigslist_scraper.py I wrote. I created my code following this tutorial. https://github.com/vprusso/youtube_tutorials/blob/master/web_scraping_and_automation/selenium/craigstlist_scraper.py
* I would like to improve craigslist_scraper.py in the following ways.
  * Make it possible to scrape all rental pricing automatically without manual manipulation.
  * Make the program scrape craigslist once a day to build the dataset.

#### Data Description
The dataset consists of rental property information in vancouver. The data is Latitude, longitude, accuracy(of location), number of beds, number of baths, square footage, price of property and name of listing.

#### Analysis

Here is a plot of the location of properties (latitude vs longitude) along with a colour representation of the price. There are some places to take note. UBC (lat: 49.26, long: -123.25), yaletown (lat: 49.275 -123.125), coal harbour (lat: 49.29, long: -123.125)
![housing_prices_scatterplot](https://user-images.githubusercontent.com/20325116/87889585-2eeaf580-c9e7-11ea-9ae2-f8350e439dd1.png)

![vancouver_housing_prices_plot](https://user-images.githubusercontent.com/20325116/88244264-26ddc080-cc48-11ea-8721-7a785b1eee75.png)

This plot shows the correlations between several attributes.

![corrolation_plot](https://user-images.githubusercontent.com/20325116/87895155-898d4d00-c9f9-11ea-918e-e5d82391304a.png)

there are not too many strong correlations, however, the correlations may not be linear. So further investigation is needed

![corr](https://user-images.githubusercontent.com/20325116/87895552-9a8a8e00-c9fa-11ea-9a83-dfce40526118.png)

The dataset is stratified to ensure there is no bias. The labels are removed from the data set for training. 

#### Results

Selecting the training model was done by comparing several different methods together by using cross validation using 10 folds for each model. The results were as followed:
* Linear regression: rmse 410.587 (mean) std: 16.506
* Decision TreeRegression: rmse 518.825 (mean), std: 31.828 
* RandomForestRegressor: rmse 392.983 (mean), std: 22.034

RandomForestRegressor seems to be the most promising model for this dataset. Therefore I am performing a GridSearchCV to help to determine the optimal hyperparameters. It is determined that the max_features hyperparameter to be 6 and the n_estimators hyperparameter to be 40. This yields a rmse of 392.710. 

Using RansomForestRegressor we can use the train and test data to show how well the model is able to predict the price of a rental property based on attributes alone.

![sqrt_vs_price](https://user-images.githubusercontent.com/20325116/88725702-5b86c780-d0e1-11ea-8590-57d35b1d57f3.png)

As you can see the model does a fairly good job at predicting the price of rental property with respect to square footage.

![beds_vs_price](https://user-images.githubusercontent.com/20325116/88725794-8244fe00-d0e1-11ea-8fe1-b59895b5ff52.png)

The model does a fairly good job at predicting the price with respect to the number of beds.

![Bath_vs_price](https://user-images.githubusercontent.com/20325116/88725864-9c7edc00-d0e1-11ea-9909-aa914934ef5e.png)

The model does a fairly good job at predicting the price with respect to the number of bathrooms. 

#### Conclusion

Modeling of rental property in Vancouver was done by using three techniques Linear Regression, Decision TreeRegression and RandomForestRegressor. Using cross validation it was shown that RandomForestRegressor was able to develop the best model for predicting the price of rental property in Vancouver. 

* Linear regression: rmse 410.587 (mean) std: 16.506
* Decision TreeRegression: rmse 518.825 (mean), std: 31.828
* RandomForestRegressor: rmse 392.983 (mean), std: 22.034

Fine turing the hyperparameters 'max_features': 6, 'n_estimators': 40 results in a rmse of 395.625 with a 95% condidence interval of [371.366, 418.482] which is very close to the cross validation technique. 

Using these hyperparameters we compare training data vs testing data and the three plots in the results section show that the model we are using is able to accurately predict the price of the rental properties in Vancouver.
 
#### Final remarks. 

From this point there are sub objectives that I have for this project. Such as determining scams, scraping data from craigslist periodically (online learning. I need to learn how to train models incrementally), and build an interactive site. At this moment I am not sure if I should build an interactive website or continue to learn different machine learning techniques. 

