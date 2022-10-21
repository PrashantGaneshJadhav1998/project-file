from flask import Flask,jsonify
import config_3
from def_utils_3 import MedicalPremium 

app=Flask(__name__)
@app.route('/')
def home():
    print('Hello')
    return('Good Afternoon')

@app.route('/prediction')
def get_prediction():
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

     charge=MedicalPremium(Age,Diabetes,BloodPressureProblems,AnyTransplants,AnyChronicDiseases,
               Height,Weight,KnownAllergies,HistoryOfCancerInFamily,NumberOfMajorSurgeries)
     charge_2=charge.get_premium_charge()
     return jsonify({'MSG':f'predictional Medical_Premium available at charges {charge_2.round(1)[0]}'})

if __name__ == '__main__' :
    app.run(host='0.0.0.0',port=config_3.PORT_NUMBER,debug=False)