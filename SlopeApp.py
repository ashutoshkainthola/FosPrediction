import pandas as pd
import numpy as np
import pickle
import streamlit as st
from PIL import Image
import typing_extensions 
  
# loading in the model to predict on the data
pickle_in = open('slr.pkl', 'rb')
slr = pickle.load(pickle_in)
  
def welcome():
    return 'welcome all'
  
# defining the function which will make the prediction using 
# the data which the user inputs
def prediction(Height, SlopeAngle, Cohesion, FrictionAngle):  
   
    prediction = slr.predict(
        [[Height, SlopeAngle, Cohesion, FrictionAngle]])
    print(prediction)
    return np.array(prediction, dtype= float)
      
  
# this is the main function in which we define our webpage 
def main():
      # giving the webpage a title
    st.title("Geo-Engineering & Soft Computing Laboratory, BHU")
      
    # here we define some of the front end elements of the web page like 
    # the font and background color, the padding and the text to be displayed
    html_temp = """
    <div style ="background-color:skyblue;padding:10px">
    <h2 style ="color:black;text-align:center;">Slope FOS Prediction App </h2>
    <i style ="font-family:hack;font-size:18px"> Machine Learning Enabled FOS Prediction </i>
    </div>
    """
    from typing_extensions import Final


    # this line allows us to display the front end aspects we have 
    # defined in the above code
    st.markdown(html_temp, unsafe_allow_html = True)
      
    # the following lines create text boxes in which the user can enter 
    # the data required to make the prediction
    Height = st.text_input("Height (m)", "")
    #Height= np.array(Height, dtype= float)
    SlopeAngle = st.text_input("Slope Angle (o)", "")
    #SlopeAngle = np.array(SlopeAngle, dtype= float)
    Cohesion = st.text_input("Cohesion (KPa)", "")
    #Cohesion= np.array(Cohesion, dtype= float)
    FrictionAngle = st.text_input("Friction Angle (o)", "")
    #FrictionAngle = np.array(FrictionAngle, dtype= float)
    result =""
      
    # the below line ensures that when the button called 'Predict' is clicked, 
    # the prediction function defined above is called to make the prediction 
    # and store it in the variable result
    if st.button("Predict"):
        result = prediction(float(Height), float(SlopeAngle), float(Cohesion), float(FrictionAngle))
        result = np.array(result, dtype= float) 
    st.success('The Factor of Safety of the slope is: {}'.format(result))
     
if __name__=='__main__':
    main()
