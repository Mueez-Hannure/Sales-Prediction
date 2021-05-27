from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
import pandas as pd
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        Item_Weight = float(request.form['Item_Weight'])
        Item_Visibility=float(request.form['Item_Visibility'])
        Item_MRP=float(request.form['Item_MRP'])
        Outlet_Years=int(request.form['Outlet_Years'])
        Outlet=int(request.form['Outlet'])
        
        
        
        
        
        Item_Type=request.form['Item_Type']
        if(Item_Type=='Dairy'):
            Item_Type=0
        if(Item_Type=='SoftDrinks'):
            Item_Type=1
        if(Item_Type=='Meat'):
            Item_Type=2
        if(Item_Type=='FruitsandVegetables'):
            Item_Type=3
        if(Item_Type=='Household'):
            Item_Type=4
        if(Item_Type=='BakingGoods'):
            Item_Type=5
        if(Item_Type=='SnackFoods'):
            Item_Type=6
        if(Item_Type=='FrozenFoods'):
            Item_Type=7
        if(Item_Type=='Breakfast'):
            Item_Type=8
        if(Item_Type=='HealthandHygiene'):
            Item_Type=9
        if(Item_Type=='HardDrinks'):
            Item_Type=10
        if(Item_Type=='Canned'):
            Item_Type=11
        if(Item_Type=='Breads'):
            Item_Type=12
        if(Item_Type=='StarchyFoods'):
            Item_Type=13
        if(Item_Type=='Others'):
            Item_Type=14
        if(Item_Type=='Seafood'):
            Item_Type=15
  
        
            
        
        
        Item_Fat_Content=request.form['Item_Fat_Content']
        if(Item_Fat_Content=='LowFat'):
            Item_Fat_Content_0=1
            Item_Fat_Content_1=0
            Item_Fat_Content_2=0
        elif(Item_Fat_Content=='Regular'):                  
            Item_Fat_Content_0=0
            Item_Fat_Content_1=1
            Item_Fat_Content_2=0
        else:
            Item_Fat_Content_0=0
            Item_Fat_Content_1=0
            Item_Fat_Content_2=1
        
        Outlet_Size=request.form['Outlet_Size']
        if(Outlet_Size=='Low'):
            Outlet_Size_0=1
            Outlet_Size_1=0
            Outlet_Size_2=0
        elif(Outlet_Size=='Medium'):                  
            Outlet_Size_0=0
            Outlet_Size_1=1
            Outlet_Size_2=0
        else:
            Outlet_Size_0=0
            Outlet_Size_1=0
            Outlet_Size_2=1
            
        Outlet_Location_Type=request.form['Outlet_Location_Type']
        if(Outlet_Location_Type=='Tier1'):
            Outlet_Location_Type_0=1
            Outlet_Location_Type_1=0
            Outlet_Location_Type_2=0
        elif(Outlet_Location_Type=='Tier2'):                  
            Outlet_Location_Type_0=0
            Outlet_Location_Type_1=1
            Outlet_Location_Type_2=0
        else:
            Outlet_Location_Type_0=0
            Outlet_Location_Type_1=0
            Outlet_Location_Type_2=1
            
        Outlet_Type=request.form['Outlet_Type']
        
        if(Outlet_Type=='Grocery_Store'):
            Outlet_Type_0=1
            Outlet_Type_1=0
            Outlet_Type_2=0
            Outlet_Type_3=0
        elif(Outlet_Type=='Supermarket_Type1'):
            Outlet_Type_0=0
            Outlet_Type_1=1
            Outlet_Type_2=0
            Outlet_Type_3=0   
        elif(Outlet_Type=='Supermarket_Type2'):                  
            Outlet_Type_0=0
            Outlet_Type_1=0
            Outlet_Type_2=1
            Outlet_Type_3=0
        else:
            Outlet_Type_0=0
            Outlet_Type_1=0
            Outlet_Type_2=0
            Outlet_Type_3=1
            
        New_Item_Type=request.form['New_Item_Type']
        if(Outlet_Size=='Food'):
            New_Item_Type_0=1
            New_Item_Type_1=0
            New_Item_Type_2=0
            
        elif(Outlet_Size=='Non_Consumable'):                  
            New_Item_Type_0=0
            New_Item_Type_1=1
            New_Item_Type_2=0
            
        else:
            New_Item_Type_0=0
            New_Item_Type_1=0
            New_Item_Type_2=1
            
        
        prediction=model.predict([[Item_Weight,Item_Visibility,Item_Type,Item_MRP,Outlet_Years,Outlet,Item_Fat_Content_0,Item_Fat_Content_1,Item_Fat_Content_2,Outlet_Size_0,Outlet_Size_1,Outlet_Size_2,Outlet_Location_Type_0,Outlet_Location_Type_1,Outlet_Location_Type_2,Outlet_Type_0,Outlet_Type_1,Outlet_Type_2,Outlet_Type_3,New_Item_Type_0,New_Item_Type_1,New_Item_Type_2]])
        output=(round(prediction[0],2))
        return render_template('index.html',prediction_text="Prediction output is {}".format(np.exp(output)))
    else:
        return render_template('index.html')
        



if __name__=="__main__":
    app.run(debug=True)
