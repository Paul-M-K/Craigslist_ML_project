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

To gain a general understanding of the data we can plot the location of each rental property based on latitude vs longitude. The colour gradient on the right represents the price of each rental property. From this plot we can make out the shape of Vancouver with this plot alone. There are some places to take note. UBC (lat: 49.26, long: -123.25), yaletown (lat: 49.275 -123.125), coal harbour (lat: 49.29, long: -123.125) 

![housing_prices_scatterplot](https://user-images.githubusercontent.com/20325116/87889585-2eeaf580-c9e7-11ea-9ae2-f8350e439dd1.png)

Here I have superimposed a map of Vancouver under the location data. We can see that the data and the map are very similar. Unfortunately it is very hard to align the map perfectly, so please bear with me.

![vancouver_housing_prices_plot](https://user-images.githubusercontent.com/20325116/88244264-26ddc080-cc48-11ea-8721-7a785b1eee75.png)


Determining the correlation of each attribute shows a fairly interesting picture. There are no strong correlations, however, there are trends in the positive direction for multiple attributes. However, not all correlations may be linear, therefore more investigation is needed.

![corrolation_plot](https://user-images.githubusercontent.com/20325116/87895155-898d4d00-c9f9-11ea-918e-e5d82391304a.png)

Here we can see at the numeric level how strongly each attributes corrolates to one another.

![corr](https://user-images.githubusercontent.com/20325116/87895552-9a8a8e00-c9fa-11ea-9a83-dfce40526118.png)

#### Results

The multivariable data was separated stratified first to ensure there is no bias. The data was then split into training data and test data. When training started the label (price) was removed from the training set and the data was standardized. 

The training data was passed through three different modelling techniques, Linear Regression, Decision TreeRegression, and RandomForestRegressor. To determine the optimal model for the training data I used cross validation with 10 folds to find the mean Root Mean Square Error (RMSE) for each technique.

![rmse](https://user-images.githubusercontent.com/20325116/88749591-79b3ee00-d108-11ea-94c9-ac454495389a.png)

The resulting cross validation Mean RMSE are as follows:

* Linear regression: RMSE 410.587 (mean) std: 16.506
* Decision TreeRegression: RMSE 518.825 (mean), std: 31.828 
* RandomForestRegressor: RMSE 392.983 (mean), std: 22.034

The lowest Mean RMSE was determined to be RandomForestRegressor. To fine tune the hyperparameters a GridSearchCV was performed. The optimal hyperparameters were determined to 'max_features': 8, 'n_estimators': 30 resulting in a rmse of 392.195.

Using the RandomForestRegressor model with hyperparameters we can pass the test dataset through this model and determine the predicted price for rental property in Vancouver. By comparing the predicted price (red circles) with the actual price (blue squares), we can see visually that the predicted values mimic the actual values very well. We can also determine the RMSE for the test data and this is 395.756 with a 95% confidence interval of [371.290, 418.796].

![sqrt_vs_price](https://user-images.githubusercontent.com/20325116/88725702-5b86c780-d0e1-11ea-8590-57d35b1d57f3.png)

This plot shows the square footage vs price for both the training data (Blue squares) and the test data (red circles). The test data prices are all predicted values that are created using the RandomForestRegressor model we have developed. 

![beds_vs_price](https://user-images.githubusercontent.com/20325116/88725794-8244fe00-d0e1-11ea-8fe1-b59895b5ff52.png)

This plot shows the number of beds vs price for both the training data (Blue squares) and the test data (red circles). The test data prices are all predicted values that are created using the RandomForestRegressor model we have developed. 

![Bath_vs_price](https://user-images.githubusercontent.com/20325116/88725864-9c7edc00-d0e1-11ea-9909-aa914934ef5e.png)

This plot shows the number of baths vs price for both the training data (Blue squares) and the test data (red circles). The test data prices are all predicted values that are created using the RandomForestRegressor model we have developed. 

#### Conclusion

Modeling of rental property in Vancouver was done by using three techniques Linear Regression, Decision TreeRegression and RandomForestRegressor. Using cross validation it was shown that RandomForestRegressor was able to develop the best model for predicting the price of rental property in Vancouver. 

* Linear regression: rmse 410.587 (mean) std: 16.506
* Decision TreeRegression: rmse 518.825 (mean), std: 31.828
* RandomForestRegressor: rmse 392.983 (mean), std: 22.034

Fine tuning the hyperparameters 'max_features': 8, 'n_estimators': 30 results in a rmse of 392.195. Using the test data with the RandomForestRegressor model and the above hyperparameters the rmse with the test data is 395.756 with a 95% condidence interval of [371.290, 418.796]. 

Using these hyperparameters we compare training data vs testing data and the three plots in the results section show that the model we are using is able to accurately predict the price of the rental properties in Vancouver.
 
#### Final remarks. 

From this point there are sub objectives that I have for this project. Such as determining scams, scraping data from craigslist periodically (online learning. I need to learn how to train models incrementally), and build an interactive 

site. At this moment I am not sure if I should build an interactive website or continue to learn different machine learning techniques. 

Thank you for taking the time to read through my project. Stay safe out there during these unusual times. -Paul

\pmb y = X \beta + \epsilon
