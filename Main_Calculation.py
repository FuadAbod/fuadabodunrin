import pandas as pd
import json

def bmi_calculator(data_file):
    
    open_data=open(data_file)
    
    data = json.load(open_data)
    Number_Of_Overweight=0

    for i in data:
        height=i['HeightCm']
        weight=i['WeightKg']
        bmi = round(weight / ((height/100)**2),2)

        if bmi <= 18.4:
            i.update({'BMI_Index': bmi,'BMI_Category':'Underwieght', 'Health_Risk':'Malnutrition risk'})
        elif 18.5 <= bmi <=24.9:
            i.update({'BMI_Index': bmi,'BMI_Category':'Normal weight ', 'Health_Risk':'Low risk'})
        elif  25 <= bmi <= 29.9:
            i.update({'BMI_Index': bmi,'BMI_Category':'Overweight  ', 'Health_Risk':'Enhanced risk'})
        elif 30 <= bmi <= 34.9:
            i.update({'BMI_Index': bmi,'BMI_Category':'Moderately obese', 'Health_Risk':'Medium risk'})
        elif 35 <= bmi <=  39.9:
            i.update({'BMI_Index': bmi,'BMI_Category':'Severely obese', 'Health_Risk':'High risk'})
        else:
            i.update({'BMI_Index': bmi,'BMI_Category':'Very severely obese', 'Health_Risk':'Very high risk'})

    open_data.close()
    for person in data:
        if person['BMI_Index'] >= 25:
            Number_Of_Overweight+=1
    

    return data, Number_Of_Overweight

