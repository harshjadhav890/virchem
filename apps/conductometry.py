import streamlit as st
import pandas as pd
from multiapp import MultiApp


def app():
    st.header("""Conductometry""")
    aim_bar = st.beta_expander("About")
    aim_bar.markdown("""
    * **Aim:** Titration of mixture of weak acid and strong acid with strong base using conductometer.
    * **Concepts:** The principle of conductometric titration is based on the fact that during
    titration, one of the ion is replaced by other and invariably these two ions differ in the
    ionic conductance with the result that conductivity of solution varies during the
    titration.
    The equivalence point is located graphically by plotting change in
    conductance as function of the volume of titrant added.
    * **Chemicals:** 0.01 N HCl, 0.01 N CH 3 COOH, 0.1 N NaOH.
    * **Apparatus:** Conductivity meter, Burette, Pipette, Beakers, Electrodes, Micro-burette.
    """)

    col1 = st.sidebar
    col2, colsep, col3 = st.beta_columns((1, 0.1, 1.3))

    # dummy dataframe
    data = {'Volume of NaOH': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            'Conductivity': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}
    df = pd.DataFrame(data)

    # selecting iterating value of NaOH
    col2.subheader("Volume of NaOH added")
    added = col2.slider("Amount of NaOH(ml) added at every step", min_value=0.0, max_value=1.0, value=0.2, step=0.2, format=None, key=None)
    naoh = 0.0
    for index in df.index:
        df.loc[index, 'Volume of NaOH'] = naoh
        naoh += added

    # df.loc[index, 'Conductivity'] = user_input
    col2.subheader("Values of conductivity")
    sequence = col2.text_area("Input your values here")
    sequence1 = sequence.splitlines()

    if sequence != '':
        for index in df.index:
            df.loc[index, 'Conductivity'] = float(sequence1[index])

    col2.subheader("Table of Values")
    col2.dataframe(df)

    colsep.write(" ")

    # plotting the graph
    col3.subheader("Plot of NaOH added v/s Conductivity")
    col3.line_chart(df.rename(columns={'Volume of NaOH':'index'}).set_index('index'))

    # v1 and v2

    col3.subheader("V1")
    v1 = float(col3.text_input("ml of NaOH required for neutralization of HCl:", 0.0))
    col3.subheader("V2")
    v2 = float(col3.text_input("ml of NaOH required for neutralization of HCL + CH3COOH:", 0.0))
    col3.subheader("V2 - V1")
    v3 = float(col3.text_input("ml of NaOH required for neutralization of CH3COOH:", v2 - v1))

    st.markdown("---")
    st.header("""Result""")
    st.subheader("Ml of NaOH required for neutralization of CH3COOH is:")
    st.text_input("ml of NaOH", v2 - v1)


