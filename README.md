# Mod20_Segment_3
During this segment, all of the individual pieces we've been building will come together. Once we have assembled these pieces, then we can start putting the final touches on the repository. Does the README.md fully describe the project and its purpose? Is the repository ready to be added to your portfolio? Details like these are part of "plugging it in" because each piece is vital to the final presentation.

# Purpose

Third Segment: Plug It In: Connect your final database to your model, continue to train your model, and create your dashboard and presentation.

## [Link to Topic Segment Details](https://github.com/ALIYA2Group)

# Presentation 

## Selected topic

We want to see if we could predict the melting of Arctic Sea Ice using the time series predictive model SARIMAX using Python.

![Header](https://github.com/ALIYA2Group/Mod20_Segment_3/blob/main/Pictures/Header.jpg)

## Reason topic was selected

We selected this topic because we wanted to predict at what point in time would the sea ice shrink. It is a topic that all the team members felt passionate about and wanted to explore. 

## Description of the source of data

We reviewed data from the following resources and identified the most useful features to be used in our analysis: 

1. [National Snow and Ice Data Center (NSIDC)](http://nsidc.org/data/google_earth)
2. [Climate Data Store](https://cds.climate.copernicus.eu/user/119111)
3. [Visualize Arctic and Antarctic Sea Ice](https://livingatlas.arcgis.com/sea-ice/)

## Here is the Question the team hopes to answer with the data

> Based on past features of science exploration and calculation on melting and atmosphere changes, we extract, transform and load the selected trends to show the sea-ice diminishing from 2003-2020 to try and predict at what point in time in the future these factors would impact the melting of the Arctic sea ice.

## Description of the data exploration phase of the project

* Extract

Through data exploration, we determined that we wanted to use Arctic data only as it is melting faster than Antarctic. 

![P5](https://github.com/ALIYA2Group/Mod20_Segment_3/blob/main/Pictures/P5.PNG)

![D3](https://github.com/ALIYA2Group/Mod20_Segment_3/blob/main/Pictures/D3.PNG)

## Description of the analysis phase of the project and data processing

* Transform
 
We had to understand the significance of the science behind the data, to understand which features of the data set we needed to use. When we transformed the features of the data set that were applicable, we reviewed the trends.

![M2](https://github.com/ALIYA2Group/Mod20_Segment_3/blob/main/Pictures/M2.PNG)

* Technologies, languages, tools, and algorithms used throughout the project

![technology](https://github.com/ALIYA2Group/Mod20_Segment_3/blob/main/Pictures/technology.jpg)

# Google Slides

## [Link to Google Slides Presentation](https://docs.google.com/presentation/d/e/2PACX-1vTcX9jJk6ygnS3amtgkJ-ByMINvXs98Os4At5uzAr8ARsh10iMweahxc6NGSYjBHSQ_T0KmloQUrV55/pub?start=true&loop=true&delayms=3000)

# Github 
Main Branch
All code in the main branch is production-ready.

![G1](https://github.com/ALIYA2Group/Mod20_Segment_3/blob/main/Pictures/G1.PNG)

* All code necessary to perform exploratory analysis
* All code necessary to complete the machine learning portion of the project

*Commits per Segment

1. [Segment 1 - Commits](https://github.com/ALIYA2Group/Mod20_Segment_1/branches)
2. [Segment 2 - Commits](https://github.com/ALIYA2Group/Mod20_Segment_2/branches)
3. [Segment 3 - Commits](https://github.com/ALIYA2Group/Mod20_Segment_3/branches)

# Machine Learning Model

Data pre-processing included importing the dataset using SQLAlchemy from AWS, dropping unwanted columns and setting the date as index.  

## Description of feature engineering and the feature selection, including the decision-making process

The selected features were visualized as time series and against the target (extent) to understand the correlation. 

![CORR](https://github.com/ALIYA2Group/Mod20_Segment_3/blob/main/Pictures/CORR.jpg)

## Description of how data was split into training and testing sets

Data was split into training and testing sets using a 70-30 ratio and using the scikit library. 

![traintest](https://github.com/ALIYA2Group/Mod20_Segment_3/blob/main/Pictures/traintest.PNG)

## Description of how we have trained the model thus far, and any additional training that will take place

The model was trained using SARIMAX. After splitting the data into training and testing sets:

1-	 Decomposed Time Series into several components-Trend, Seasonality, and Random noise

![seasonal](https://github.com/ALIYA2Group/Mod20_Segment_3/blob/main/Pictures/seasonal.png)

2- Checked for Data Stationarity using Augmented Dickey-Fuller(ADF) test. If we make the data stationary, then the model can make predictions based on the fact that mean and variance will remain the same in the future. A stationarized series is easier to predict. For data points that were not stationary, data was differenced to make it stationary. 

3- An ACF and PACF bar chart was plotted. ACF is a plot of the coefficients of correlation between a time series and its lag and helps determine the value of p or the AR term while PACF is a plot of the partial correlation coefficients between the series and lags of itself and helps determine the value of q or the MA term. Both p and q are required input parameters for the SARIMAX Model. 

![ACF](https://github.com/ALIYA2Group/Mod20_Segment_3/blob/main/Pictures/ACF.png)

3- Ran the SARIMAX model to forecast the extent based on the order obtained using ARIMA  model and using the traing set as the exogenous variables

4- Fitted the model and trained and tested data was put into a dataframe (converted back to scale)

![F9](https://github.com/ALIYA2Group/Mod20_Segment_3/blob/main/Pictures/F9.PNG)

## Description of current accuracy score

The Accuracy Score : 0.08529 (root square mean error)

We resulted in a very good accuracy score.

![F10](https://github.com/ALIYA2Group/Mod20_Segment_3/blob/main/Pictures/F10.PNG)

## Future Prediction:

We successfully completed prediction model to predict the features of the Artic Sea Ice melt:

1) A univariate time-series model was applied to each of the features to estimate their future value, which are put into a dataframe

![XFORE](https://github.com/ALIYA2Group/Mod20_Segment_3/blob/main/Pictures/XFORE.jpg)

2) using the predicted values of the features, we used the model to predict the values of Y (Extent):

![F10c](https://github.com/ALIYA2Group/Mod20_Segment_3/blob/main/Pictures/F10c.PNG)

## Explanation of model choice, including limitations and benefits

Given the nature of the data and the question we are trying to answer, we used a Timer-Series prediction model SARIMAX (Seasonal Auto-Regressive Integrated Moving Average with eXogenous factors). It helps to predict future values using auto-regression and moving average along with adding in the seasonality factor. 

[ARIMA Model](https://www.machinelearningplus.com/time-series/arima-model-time-series-forecasting-python/) - using Using ARIMA model, we can forecast a time series using the series past values. We built optimal ARIMA model from scratch and extend it to Seasonal ARIMA (SARIMA) and SARIMAX models. 

[SARIMAX](https://www.statsmodels.org/dev/examples/notebooks/generated/statespace_sarimax_faq.html) is seasonal updated version of the ARIMA model family.

## Explanation of changes in model choice 

There were a number of different models tried and tested, which were the changes that occurred between the Segment 2 and Segment 3 as follows: 

1. Method using vector autoregression (VAR) 
![M1](https://github.com/ALIYA2Group/Mod20_Segment_3/blob/main/Pictures/M1.PNG)

2. Method Time-series forecasting using tensor flow, including convolutional and recurrent neural networks (CNN and RNN)
![M1a](https://github.com/ALIYA2Group/Mod20_Segment_3/blob/main/Pictures/M1a.PNG)

# Database Integration 

There are no deliverables for the database integration section of the project for this segment.

# Dashboard

## [Link to Dashboard](https://aliya2group.github.io/Mod20_Segment_3/)

The dashboard plan includes the following:

* Using" beautiful soup" and "splinter" to scrap the news from idc website. (interactive element)
* We put the scraping script in the "Google app engine Cron task" and it will automatically do the scraping everyday. (interactive element)
* Store the data into MongoDB.
* Deploy the web page to "Google app engine".
* The website is using "Flask" and "pymongo" to show and read the data from MongoDB.
* Images & Databases available to view and download
 
![W2](https://github.com/ALIYA2Group/Mod20_Segment_3/blob/main/Pictures/W2.PNG)

# Preview of Final Project Website:

# [Final Preview](https://seaiceanalysis.appspot.com/)


