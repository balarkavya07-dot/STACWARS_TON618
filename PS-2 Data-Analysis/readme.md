##PS2 SOLAR RADIATION ANALYSIS AND PREDICTION ##

**INTRODUCTION**
The Solar Radiation Analysis and Prediction project focuses on analyzing solar observation data to understand how solar radiation varies with time and how it relates to environmental parameters such as temperature and humidity.
Using Python, Pandas, Matplotlib,numPy and scikit-learn we processed the dataset and created visualizations to identify trends,patterns in solar radiation and machine learning regression model to predict solar radiations using the available environmental and temporal features.

--------------------------------------------------------------------------------------------

**part--1 Data Visualizations and inferences**
OVERVIEW:
In part A i used python Matplot, pandas and numpy . i have made graphs and plots for analyzing such large data using matplot and pandas mainly.I used the data which is given in PS (SolarPrediction.csv file) to visualize and analyze data.

INSTALLATION AND PACKAGES I INSTALLED IN PYTHON:
python -m pip install pandas
python -m pip install matplotlib (matplot library)


********************************************************************************************
**PART A(DATA VISUALIZATIONS)**
1) Purpose of drawing Solar Radiation vs Time graph:
  -identifying the changes happening throughout the day, where the peaks and dips  occurs and the trend it is following.
2) Purpose of drawing Solar Radiation vs Temperatue graph:
  -Temperature is strongly related to solar radiation among all other environmental factors it shows the positive correlation.When solar radiation increases , temperature also increases that shows the direct relation between them.
3) Purpose of drawing Solar Radiation vs Humidity graph:
  -After temperature humidity has the major correlation with solar radiation.It shows the negative correlation with solar radiation.When solar radiation increases , humidity generally seen to decrease.

I also added average radiation vs hour of a day graph helps to understand how average solar radiation changes throughout the day.By calculating this it reduces the effect of individual fluctuations and makes the overall daily pattern easier to observe.It helps identify the hours with the highest and lowest average radiation and shows the general trend of solar radiation over time.
********************************************************************************************
**PART B(DRAWING INFERENCES)**
1) When is solar radiation highest?
Solar radiation is generally highest around midday or early afternoon, when sunlight is more brighter and decreases towards the evening.

2) Which parameter has the strongest relationship with radiation?
Temperature appears to have a positive relationship with solar radiation, while humidity  shows a negative relationship.In humidity and temperature relation humidity increases, showing a negative relationship .It is observed that average humidity generally decreases as temperature increases.

3) What patterns exist between radiation, temperature, and humidity?
Higher radiation often occurs with higher temperatures. Humidity may decrease as temperature increases, but this pattern is not always consistent.Humidity generally seen to decrease when temperature increases.
********************************************************************************************

------------------------------------------------------------------------------------------

**part--3  Solar Day Analysis**
REQUIREMENTS
To analyse it we have to use pandas library. 
pip install pandas
This analysis is in SolarDayAnalysis.py file.

i have added the following columns to SolarPrediction.csv:
1. DateTime : complete date and time is required format using .to_datetime
2. SunRise and SunSet : time in .to_datetime format
1) we need daily report of radiations so date is later seperated by **.dt.date**. and then the daily mean and max are calculated for each day by .max() and .mean() after grouping them in seperate days and then a seperate data frame in created in panda  
then in this data frame daily_max and daily_avg is added along with date daily_report.txt is later generated in the .py only.

2) to identify the location of highest radiation firstly all radiations are loacated to a list, max function used then location of maxed value is found by .loc() and complete row is is then named peak. later required parameters of that time are printed by peak. 
to calculate timeinterval between sunrise , sunset with peak[time] difference is used as all these times are in .to_datetime

3) Now we have to find dates of top5 highest solar radiation so as i have the daily_avg data already i simply sorted it and found the top five values using .tail(5) but as they still are not in decreasing order we will reverse them 

4) also to make a seperate file with date daily_avg and daily_max i have used file handling

--------------------------------------------------------------------------------------------

**part--4  Solar Radiation Prediction**
REQUIREMENTS:
the following should be installed:
pip install pandas
pip install numpy
pip install scikit-learn

1) Almost all the parameters are used to make the model more reliable like:
["Temperature","Humidity","Pressure","Speed","WindDirection(Degrees)","Hour"]
other parameters like UNIXTime,Date,Sunrise and Sunset are not used as input cause they do not affect any difference in SolarRadiation

2) train_test_split is used to split the data into train(80%) , validation_part(10%) and test_part(10%) 

3) .fit is used to train the LinearRegression model {i.e. imodel}with train part
then validation part is used to evaluate the data and named as RMSE1 and R2_1
1. RMSE1= 198.8806
2. R2_1= 0.6037
4) then the data used for validation is also added in the imodel 
and later the final test data is used to evaluate the model 
1. RMSE2= 205.9964
2. R2_2= 0.5808
5) Also note that after final evaluation i have added the remaining data to model too
to find useful features in the prediction of Solar Radiation i have reached for the coefficients in the model 
i)   Temperature.  X  39.95
ii)  Humidity.  X  -0.01
iii) Pressure.  X  -704.29
iv)  Speed.  X   7.69
v)   WindDirection(Degrees).   X  -0.27
vi)  Hour.  X  -6.4
6) By this we can say that Pressure is the most major role in Predicting the Solar radiation followed by Temperature cause on small changes in Pressure large change in Radiation can be observed
7) order of importance is:
1. Pressure
2. Temperature
3. Speed
4. Hour
5. Wind Direction
6. Humidity
8) i have also added a system to take input from user to predict the SolarRadiation on given parameters.
9) also a warning signal has been added so that if Radiations are very high, authorities can be alerted 

--------------------------------------------------------------------------------------------









