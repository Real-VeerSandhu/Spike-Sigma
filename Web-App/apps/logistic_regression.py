from numpy.core.numeric import full
import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import random
from sklearn.linear_model import LinearRegression

# To be changed
def gen_points(input):
    x = []
    y = []
    for i in range(input):
        x.append(i+1)
    slope = random.randint(1,4)
    for i in x:
        val = i*slope
        rand = random.randint(1,3)
        if rand == 1:
            y.append(val+1)
        elif rand == 2:
            y.append(val-1)
        else:
            y.append(val+2)
    data = pd.DataFrame({'X': x, 'Y': y})
    return data

def train_model(data):
    reg = LinearRegression().fit(np.array(data['X']).reshape(-1,1), np.array(data['Y']).reshape(-1,1))
    preds = reg.predict(np.array(data['X']).reshape(-1,1))
    new_data = pd.DataFrame({'X': data['X'], 'Y': data['Y'], 'Model': preds.reshape(-1)})
    return reg, new_data

def app():
    
    st.title('Linear Regression')

    st.write("Linear Regression is the most fundamental algorithm in Machine Learning and Artificial Intelligence, it's applicable in several scenrios \
        and is straighforward to emulate")
    slide_input = st.slider('Select the number of data points', 10, 20)

    data = gen_points(slide_input)
    model, full_data = train_model(data)

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=full_data['X'], y=full_data['Y'], mode='markers', name='Original Data'))
    fig.add_trace(go.Scatter(x=full_data['X'], y=full_data['Model'], mode='lines', name='Linear Regression Model'))
    st.plotly_chart(fig)

    st.write('## Use the trained model to make predictions')
    x_val = st.number_input('Enter an X value', 0, 99999999999999)
    if st.button('Run Model'):
        st.write('Prediction (Y Value): ', int(model.predict([[x_val]])[0][0]))