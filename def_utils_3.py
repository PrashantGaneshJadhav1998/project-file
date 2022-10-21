import pandas as pd
import numpy as np
import pickle
import json
import config_3

class MedicalPremium():
    def __init__(self,Age,Diabetes,BloodPressureProblems,AnyTransplants,AnyChronicDiseases,
               Height,Weight,KnownAllergies,HistoryOfCancerInFamily,NumberOfMajorSurgeries):
               self.Age=Age
               self.Diabetes=Diabetes
               self.BloodPressureProblems=BloodPressureProblems
               self.AnyTransplants=AnyTransplants
               self.AnyChronicDiseases=AnyChronicDiseases
               self.Height=Height
               self.Weight=Weight
               self.KnownAllergies=KnownAllergies
               self.HistoryOfCancerInFamily=HistoryOfCancerInFamily
               self.NumberOfMajorSurgeries=NumberOfMajorSurgeries

    def load_model(self):
        with open (config_3.LINEAR_MODEL_PATH,'rb') as f:
            self.linear_model=pickle.load(f)

        with open (config_3.PROJECT_DATA_PATH,'r') as f:
            self.project_data=json.load(f)

    def get_premium_charge(self):
        self.load_model()

        test_array=np.zeros(len(self.project_data['columns']))
        test_array[0]=self.Age
        test_array[1]=self.Diabetes
        test_array[2]=self.BloodPressureProblems
        test_array[3]=self.AnyTransplants
        test_array[4]=self.AnyChronicDiseases
        test_array[5]=self.Height
        test_array[6]=self.Weight
        test_array[7]=self.KnownAllergies
        test_array[8]=self.HistoryOfCancerInFamily
        test_array[9]=self.NumberOfMajorSurgeries

        print('test_array :',test_array)
        predicted_charge=self.linear_model.predict([test_array])
        # print(predicted_charge)
        return(predicted_charge)

if __name__ == '__main__' :
    Age=45
    Diabetes=3
    BloodPressureProblems=2
    AnyTransplants=1
    AnyChronicDiseases=1
    Height=155
    Weight=57
    KnownAllergies=1
    HistoryOfCancerInFamily=1
    NumberOfMajorSurgeries=2

    med_ins=MedicalPremium(Age,Diabetes,BloodPressureProblems,AnyTransplants,AnyChronicDiseases,
                       Height,Weight,KnownAllergies,HistoryOfCancerInFamily,NumberOfMajorSurgeries)
    print('premium_charge :',med_ins.get_premium_charge()[0].round(2))
