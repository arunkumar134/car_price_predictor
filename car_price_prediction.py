import pandas as pd
import numpy as np
import datetime
import xgboost as xgb
import streamlit as st

def main():
    html_temp="""<h1>CAR PRice PRedicTion</h1>"""

    model=xgb.XGBRegressor()
    model.load_model("xgb_model.json")

    st.markdown(html_temp,unsafe_allow_html=True)
    st.markdown("this app will help you to predict your car selling price")

    p1=st.number_input("please enter ex_showroom price in lakhs",2.5,25.0,step=1.0)
    p2=st.number_input("please enter car driven in km",100,500000,step=100)

    s1=st.selectbox("select the fuel type",("petrol","diesel","cng"))
    if s1=='petrol':
        p3=0
    elif s1=='diesel':
        p3=1
    elif s1=='cng':
        p3=2
    
    s2=st.selectbox("select the seller type",("dealer","individual"))
    if s2=='dealer':
        p4=0
    elif s2=='individual':
        p4=1
    
    s3=st.selectbox("select the transmission ",("manual","automatic"))
    if s3=='manual':
        p5=0
    elif s3=='automatic':
        p5=1

    p6=st.slider("how many owners",0,3)

    date_time=datetime.datetime.now()
    years=st.number_input("car purchased year",1990,date_time.year,step=1)
    p7=date_time.year - years

    data_new=pd.DataFrame({})
    data_new=pd.DataFrame([[p1,p2,p3,p4,p5,p6,p7]],columns=["Present_Price","Kms_Driven","Fuel_Type","Seller_Type","Transmission","Owner","Age"],index=[0])

    if st.button("Predict"):
        pred=model.predict(data_new)
        st.success("you can sell you car at {:.2f} lakhs".format(pred[0]))
    
    
if __name__=='__main__':
    main()

