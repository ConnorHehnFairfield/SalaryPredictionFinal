# Salary Prediction
## By Connor Hehn and John Minogue

### Table of Contents
-[Introduction](#introduction)

-[Data](#data)

-[Methods/Models](#methods/models)

-[Evaluation](#evaluation)

-[Conclusion](#conclusion)

-[References](#references)

### Introduction
This project uses machine learning and artificial intelligence methods in order to predict the estimated salary based on various factors.

### Data
The data used for this project is titled Salary by Job Title and Country from Kaggle. The link to this dataset is referenced below.
The data uses various features as follows: <br>
-Age <br>
-Gender <br>
-Education Level <br>
-Job Title <br>
-Years of Experience <br>
-Country <br>
-Race <br>
-Senior (yes/no) <br>

### Method/Models
This project was initially tested using two models: Linear Regression and Random Forest Regression.
#### Linear Regression
The linear regression model had the following results: <br>
Mean Error (ME) : -175.0845 <br>
Root Mean Squared Error (RMSE) : 27969.9491 <br>
Mean Absolute Error (MAE) : 21965.9850 <br>
Mean Percentage Error (MPE) : -21.3839 <br>
Mean Absolute Percentage Error (MAPE) : 35.2633 <br>
#### Random Forest Regression
The random forest regression model had the following results: <br>
Mean Error (ME) : -597.8250 <br>
Root Mean Squared Error (RMSE) : 7945.2258 <br>
Mean Absolute Error (MAE) : 3554.2483 <br>
Mean Percentage Error (MPE) : -8.9728 <br>
Mean Absolute Percentage Error (MAPE) : 11.3125 <br>

### Evaluation
After evaluation of the two models chosen for this project, we have decided to choose Random Forest Regression as the model to use for the main prediction.
Random forest regression hsa a lower Mean Absolute Error (MAE) and a lower Mean Percent Error (MPE) which we have decided were more important in model choice.
### Conclusion
In conclusion, the model choosen to predict salary based on the fields from the dataset was the Random Forest Regression model. The model also provides feature importance
information. The feature importance for this model are as follows: <br>
Age: 5.97 % <br>
Education Level: 02.75 % <br>
Years of Experience: 74.97 <br>
Senior: 00.61 <br>
Gender: 00.63 <br>
Job Title: 14.29 <br>
Country: 00.35 <br>
Race: 00.44 <br>
### References
reference link to dataset: https://www.kaggle.com/datasets/amirmahdiabbootalebi/salary-by-job-title-and-country
