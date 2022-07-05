from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)
model = pickle.load(open('random_forest_regression_model.pkl', 'rb'))
@app.route('/',methods=['POST','GET'])
def hello():
    return render_template('index.html')
@app.route("/about")
def about():
    return render_template('about.html')
@app.route("/predict_price")
def predict_price():
    return render_template('indexpredict1.html')
standard_to = StandardScaler()
@app.route("/indexfinal")
def final_price():
    return render_template('indexfinal.html')
@app.route("/predict", methods=['POST'])
def predict():
    Fuel_Type_Diesel=0
    if request.method == 'POST':
        Year = int(request.form['Year'])
        Car_name = str(request.form['car_name'])
        Maruti=0
        Skoda=0
        Honda=0
        Hyundai=0
        Toyota=0
        Ford=0
        Renault=0
        Mahindra=0
        Tata=0 
        Chevrolet=0
        Datsun=0
        Volkswagen=0
        Nissan=0
        Daewoo=0
        Kia=0
        Fiat=0
        Other=0
        Opel=0
        if(Car_name=='Ambassador'):
            Ambassador=1
        elif(Car_name=='Skoda'):
            Skoda=1
        elif(Car_name=='Honda'):
            Honda=1
        elif(Car_name=='Hyundai'):
            Hyundai=1
        elif(Car_name=='Toyota'):
            Toyota=1
        elif(Car_name=='Ford'):
            Ford=1
        elif(Car_name=='Renault'):
            Renault=1
        elif(Car_name=='Mahindra'):
            Mahindra=1
        elif(Car_name=='Tata'):
            Tata=1
        elif(Car_name=='Chevrolet'):
            Chevrolet=1
        elif(Car_name=='Datsun'):
            Datsun=1
        elif(Car_name=='Volkswagen'):
            Volkswagen=1
        elif(Car_name=='Nissan'):
            Nissan=1
        elif(Car_name=='Daewoo'):
            Daewoo=1
        elif(Car_name=='Kia'):
            Kia=1
        elif(Car_name=='Fiat'):
            Fiat=1
        elif(Car_name=='other'):
            Other=1
        else:
            Opel=1
        Kms_Driven=int(request.form['Kms_Driven'])
        Kms_Driven2=np.log(Kms_Driven)
        Mileage=float(request.form['Mileage'])
        Engine=int(request.form['Engine'])
        Max_power=float(request.form['Max_power'])
        Seats=int(request.form['Seats'])
        Fuel_Type=request.form['Fuel_Type']
        if(Fuel_Type=='CNG'):
            Fuel_Type_Cng=1
            Fuel_Type_Petrol=0
            Fuel_Type_Diesel=0
            Fuel_Type_Lpg=0
        elif(Fuel_Type=='Petrol'):
            Fuel_Type_Cng=0
            Fuel_Type_Petrol=1
            Fuel_Type_Diesel=0
            Fuel_Type_Lpg=0
        elif(Fuel_Type=='Diesel'):
            Fuel_Type_Cng=0
            Fuel_Type_Petrol=0
            Fuel_Type_Diesel=1
            Fuel_Type_Lpg=0
        else:
            Fuel_Type_Cng=0
            Fuel_Type_Petrol=0
            Fuel_Type_Diesel=0
            Fuel_Type_Lpg=1
        Year=2020-Year
        Seller_Type_Individual=request.form['Seller_Type_Individual']
        if(Seller_Type_Individual=='Individual'):
            Seller_Type_Individual=1
            Seller_Type_Dealer=0
            Seller_Type_Trustmark_Dealer=0
        elif(Seller_Type_Individual=='Dealer'):
            Seller_Type_Individual=0
            Seller_Type_Dealer=1
            Seller_Type_Trustmark_Dealer=0
        else:
            Seller_Type_Individual=0
            Seller_Type_Dealer=0
            Seller_Type_Trustmark_Dealer=1
        Transmission_Manual=request.form['Transmission_Manual']
        if(Transmission_Manual=='Manual'):
            Transmission_Manual=1
            Transmission_Automatic=0
        else:
            Transmission_Manual=0
            Transmission_Automatic=1
        Owner=request.form['Owner']
        if(Owner=='First Owner'):
            Owner_First_Owner=1
            Owner_Fourth_Above_Owner=0
            Owner_Second_Owner=0
            Owner_Third_Owner=0
        elif(Owner=='Second Owner'):
            Owner_First_Owner=0
            Owner_Fourth_Above_Owner=0
            Owner_Second_Owner=1
            Owner_Third_Owner=0
        elif(Owner=='Fourth and above'):
            Owner_First_Owner=0
            Owner_Fourth_Above_Owner=1
            Owner_Second_Owner=0
            Owner_Third_Owner=0
        else:
            Owner_First_Owner=0
            Owner_Fourth_Above_Owner=0
            Owner_Second_Owner=0
            Owner_Third_Owner=1
        X=[[Year,Kms_Driven2,Mileage,Engine,Max_power,Seats,Other,Chevrolet,Daewoo,Datsun,Fiat,Ford,Honda,Hyundai,Kia,Mahindra,Maruti,Nissan,Opel,Renault,Skoda,Tata,Toyota,Volkswagen,Fuel_Type_Cng,Fuel_Type_Diesel,Fuel_Type_Lpg,Fuel_Type_Petrol,Seller_Type_Dealer,Seller_Type_Individual,Seller_Type_Trustmark_Dealer,Transmission_Automatic,Transmission_Manual,Owner_First_Owner,Owner_Fourth_Above_Owner,Owner_Second_Owner,Owner_Third_Owner]]       
        prediction=model.predict(X)
        output=int(round(prediction[0],2))
        if output<0:
            return render_template('indexpredict1.html',prediction_texts="Sorry you cannot sell this car")
        else:
            return render_template('indexpredict1.html',prediction_text="You Can Buy/Sell The Car at Rs {}".format(output))
    else:
        return render_template('indexpredict1.html')

if __name__=="__main__":
    app.run(debug=True)