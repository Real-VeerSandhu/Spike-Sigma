import streamlit as st
from multiapp import MultiApp
from apps import home, linear_regression

app = MultiApp()

st.set_page_config(page_title="Spike Sigma App", page_icon="➕", layout='centered', initial_sidebar_state="expanded")

st.markdown("""
# Spike Sigma
""")

# Add all your application here
app.add_app("Home", home.app)
app.add_app("Linear Regression", linear_regression.app)

# The main app
app.run()