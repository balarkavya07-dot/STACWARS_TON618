# Part D (Bonus) - Solar Radiation Prediction

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

#the same things which we did earlier but now we are using hour only as using complete things which complicate
df = pd.read_csv("SolarPrediction.csv")
only_date = df["Data"].str.split(" ").str[0]
full_text = only_date + " " + df["Time"]
df["Datetime"] = pd.to_datetime(full_text)
df["Hour"]=df["Datetime"].dt.hour

#Step1: Selected all important features.
#Note that i have used humidity which have very less change because coefficient will be less so it will not affect much in this
#Note that wind direction is also which practically do not seem to have much affect but the type of winds can affect in moving clouds.
All=["Temperature","Humidity","Pressure","Speed","WindDirection(Degrees)","Hour"]
#X and Y parameters
X=df[All]
Y=df["Radiation"]

print("Parameters used in this model are:")
i=1
for x in All:
    print(f"{i}.   {x}")
    i+=1

#Step2: splitting in training an two test sessions
#note that when i was not using random_state the value of R2 and RMSE were changing 
X_train,X_first,Y_train,Y_first = train_test_split(X, Y,test_size=0.2,random_state=4)
X_second,X_test,Y_second,Y_test = train_test_split(X_first, Y_first, test_size=0.5,random_state=2)

#Step3: Linear regression is the main model making module and .fit train the module
imodel=LinearRegression()
imodel.fit(X_train,Y_train)

prediction1= imodel.predict(X_second)

#Step4: using RMSE and R2 to evaluate the the model in both cases
mse1=mean_squared_error(Y_second, prediction1)
RMSE1 = np.sqrt(mse1)
R2_1 = r2_score(Y_second, prediction1)   

print("first_RMSE:",RMSE1)
print("First_ R2:",R2_1)

X_final=pd.concat([X_train,X_second])
Y_final=pd.concat([Y_train,Y_second])

imodel.fit(X_final,Y_final)

prediction2= imodel.predict(X_test)

mse2=mean_squared_error(Y_test,prediction2)
RMSE2 = np.sqrt(mse2)
R2_2 = r2_score(Y_test,prediction2)

print("final_RMSE:",RMSE2)
print("final_ R2:",R2_2)

X_final2=pd.concat([X_final,X_test])
Y_final2=pd.concat([Y_final,Y_test])
imodel.fit(X_final2,Y_final2)

#Step5: finding which feature matter the most by using coefficient of linear expression in the model
print("constant to be added to the data: ", round(imodel.intercept_,2))
for i in range(len(All)):
    print(f"{All[i]}.  X  {round(imodel.coef_[i],2)}\n")

#printing the data
print(f"order of importance is:\n1. Pressure\n2. Temperature\n3. Speed\n4. Hour\n5. Wind Direction\n6. Humidity")

t= input("Do you want to use this model (YES/NO): ")
if t=="YES":
    Temperature = float(input("Enter temperature: "))
    Humidity = float(input("Enter humidity: "))
    Pressure = float(input("Enter pressure: "))
    Speed = float(input("Enter wind speed: "))
    WindDirection = float(input("Enter wind direction (0-360): "))
    Hour = int(input("Enter hour (0-23): "))

    my_values = [[Temperature, Humidity, Pressure, Speed, WindDirection, Hour]]
    my_data = pd.DataFrame(my_values, columns=All)

    my_prediction = imodel.predict(my_data)
    no_negative = max(my_prediction[0],0)
    print("Predicted radiation:", no_negative)
    try:
        if no_negative > 800:
            raise Exception("Radiation is greater than 800W/m². DANGER ")
    except Exception as e:
        print("***************************************************************\n*    WARNING:" +str(e)+"       *\n***************************************************************")

