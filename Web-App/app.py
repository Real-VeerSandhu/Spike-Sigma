import streamlit as st
from multiapp import MultiApp
from apps import home, data, linear_regression # import your app modules here

app = MultiApp()

st.markdown("""
# Spike Sigma
This  app allows users to experiment and play with mathematical models to allow for an interactive educational experience
""")

# Add all your application here
app.add_app("Home", home.app)
app.add_app("Data", data.app)
app.add_app("Linear Regression", linear_regression.app)
# The main app
app.run()