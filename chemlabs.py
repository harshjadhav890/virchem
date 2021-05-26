import streamlit as st
import pandas as pd
from PIL import Image
from multiapp import MultiApp
from apps import conductometry, ph_metry, colorimetry

st.set_page_config(layout="wide")


st.image("virchem-logos_transparent.png", width=200)
st.title("Welcome to Virchem")
st.markdown("""A simple **Data-App** for performing Chemistry experiments
""")
st.markdown("---")
# #e79215
# #2e2929

app = MultiApp()

# Add all your application here
app.add_app("Conductometry", conductometry.app)
app.add_app("pH metry", ph_metry.app)
app.add_app("Colorimetry", colorimetry.app)
# The main app
app.run()

help_bar = st.sidebar.beta_expander("Help")
help_bar.markdown("""**Virchem** is a data app that allows you to perform experiments involving graphical calculations
 with ease. The app accepts values for different readings depending on the 
 experiment, saves them in the form of a python dataframe and plots the graphs required. """)






