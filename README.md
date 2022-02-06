# Mod20_Segment_3
During this segment, all of the individual pieces we've been building will come together. Once we have assembled these pieces, then we can start putting the final touches on the repository. Does the README.md fully describe the project and its purpose? Is the repository ready to be added to your portfolio? Details like these are part of "plugging it in" because each piece is vital to the final presentation.

# Purpose

Third Segment: Plug It In: Connect your final database to your model, continue to train your model, and create your dashboard and presentation.

# Presentation 

## [Link to Topic Segment Details](https://github.com/ALIYA2Group)

## Selected topic

We want to see if we could predict the mealting of Artic Sea Ice using time series predictive model SARIMAX for Time series prediction using Python.

![Header](https://github.com/ALIYA2Group/Mod20_Segment_3/blob/main/Pictures/Header.jpg)
![P1](https://github.com/ALIYA2Group/Mod20_Segment_3/blob/main/Pictures/P1.PNG)

## Reason topic was selected

We selected this topic becuase we wanted to predict at what point in time would the sea ice shrink.

## Description of the source of data

After reviewing the source data from the following resources; 

1. [National Snow and Ice Data Center (NSIDC)](http://nsidc.org/data/google_earth)
2. [Climate Data Store](https://cds.climate.copernicus.eu/user/119111)
3. [Visualize Arctic and Antarctic Sea Ice](https://livingatlas.arcgis.com/sea-ice/)

## Here is the Question the team hopes to answer with the data

> Based on past features of science exploration and calculation on melting and atmosphere changes, we extract, transform and load the selected trends to show the sea-ice diminishing from 2003-2020 to try and predict at what point in time in the future these factors would impact the melting of the arctic sea ice extent.

## Description of the data exploration phase of the project

* Extract

Thru data exploration we determined that we wanted to use Artic data only, because it will melt faster than Antartica. 

![P5](https://github.com/ALIYA2Group/Mod20_Segment_3/blob/main/Pictures/P5.PNG)

## Description of the analysis phase of the project and data processing

* Transform
 
We had to understand the significance of the science behind the data, to understand which features of the data set we needed to use. When we transformed the features of the data set that were applicable, we reviewed the trends.
![M2](https://github.com/ALIYA2Group/Mod20_Segment_3/blob/main/Pictures/M2.PNG)
![D3](https://github.com/ALIYA2Group/Mod20_Segment_3/blob/main/Pictures/D3.PNG)

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

Working code for our machine learning model is as follows;

# Description of feature engineering and the feature selection, including the decision-making process


![F2](https://github.com/ALIYA2Group/Mod20_Segment_3/blob/main/Pictures/F1.PNG)

# Description of how data was split into training and testing sets
![F1](https://github.com/ALIYA2Group/Mod20_Segment_3/blob/main/Pictures/F1.PNG)
![F3](https://github.com/ALIYA2Group/Mod20_Segment_3/blob/main/Pictures/F1.PNG)
# Explanation of model choice, including limitations and benefits

[ARIMA Model](https://www.machinelearningplus.com/time-series/arima-model-time-series-forecasting-python/) - using Using ARIMA model, we can forecast a time series using the series past values. We built optimal ARIMA model from scratch and extend it to Seasonal ARIMA (SARIMA) and SARIMAX models. 
[SARIMAX](https://www.statsmodels.org/dev/examples/notebooks/generated/statespace_sarimax_faq.html) is seasonal updated version of the ARIMA model family.

# Explanation of changes in model choice 

There were a number of different models tried and tested, which were the changes that occurred between the Segment 2 and Segment 3 as follows: 

1. Method using vector autoregression (VAR)
![M1](https://github.com/ALIYA2Group/Mod20_Segment_3/blob/main/Pictures/M1.PNG)
2. Method Time-series forecasting using tensor flow, including convolutional and recurrent neural networks (CNN and RNN)
![M1a](https://github.com/ALIYA2Group/Mod20_Segment_3/blob/main/Pictures/M1a.PNG)

# Description of how we have trained the model thus far, and any additional training that will take place

The model was trained using SARIMAX. 

# Description of current accuracy score

The Accuracy Score : 0.08529

We resulted in a very good accuracy score.

![F7](https://github.com/ALIYA2Group/Mod20_Segment_3/blob/main/Pictures/F7.PNG)

# Future Prediction:

We successfully completed prediction model to predicte the features of the Artic Sea Ice melt as follows;

![F10](https://github.com/ALIYA2Group/Mod20_Segment_3/blob/main/Pictures/F10.PNG)
![F10a](https://github.com/ALIYA2Group/Mod20_Segment_3/blob/main/Pictures/F10a.PNG)
![F10b](https://github.com/ALIYA2Group/Mod20_Segment_3/blob/main/Pictures/F10b.PNG)
![F10c](https://github.com/ALIYA2Group/Mod20_Segment_3/blob/main/Pictures/F10c.PNG)

# Database Integration 

There are no deliverables for the database integration section of the project for this segment.

# Dashboard

## [Link to Dashboard](https://aliya2group.github.io/Mod20_Segment_3/)

The dashboard plan include the following:

1. The iteractive element 
2. Images & Databases
 
![W1](https://github.com/ALIYA2Group/Mod20_Segment_3/blob/main/Pictures/W1.PNG)

# Preview of Final Project Website:

# [Final Preview](https://seaiceanalysis.appspot.com/)


