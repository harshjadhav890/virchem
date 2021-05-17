import streamlit as st
import pandas as pd
import numpy as np
from multiapp import MultiApp


def app():
    st.header("""pH-metry""")
    aim_bar = st.beta_expander("About")
    aim_bar.markdown("""
    * **Aim:** To determine dissociation constant of Weak acid (Acetic acid) using pH-meter.
    * **Prior Concept:** Concentration of H+ and OH-, pH, pOH, pKa, pKb. Concept of strong and
    weak acids and bases, Buffers: acidic and basic, dissociation constant (Ka)
    * **Chemicals:** Sodium hydroxide, Acetic acid, buffer solution.
    * **Apparatus:** pH meter, pH meter electrode, burette, pipette, beaker etc.
    """)

    col1 = st.sidebar
    col2, colsep, col3 = st.beta_columns((1, 0.1, 1.3))

    # dataframe pH
    data = {'Volume of NaOH': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            'pH': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}
    df = pd.DataFrame(data)

    # dataframe d(pH)/d(NaOH)
    data1 = {'Volume of NaOH': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             'pH': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}
    df1 = pd.DataFrame(data1)

    # selecting iterating value of NaOH
    col2.subheader("Volume of NaOH added")
    added = col2.slider("Amount of NaOH(ml) added at every step", min_value=0.0, max_value=8.0, value=2.0, step=2.0, format=None, key=None)
    naoh = 0.0
    naoh1 = 0.0
    for index in df.index:
        df.loc[index, 'Volume of NaOH'] = naoh
        naoh += added
    for index in df1.index:
        df1.loc[index, 'Volume of NaOH'] = naoh1
        naoh1 += added

    # df.loc[index, 'Conductivity'] = user_input
    col2.subheader("Values of pH")
    sequence = col2.text_area("Input your values of pH here")
    sequence1 = sequence.splitlines()

    if sequence != '':
        for index in df.index:
            df.loc[index, 'pH'] = float(sequence1[index])
    seq_data = df.values.tolist()
    print(seq_data)
    x = []
    y = []
    for i in range(0, 20):
        x.append(seq_data[i][0])
        y.append(seq_data[i][1])
    sequenced = np.diff(y) / np.diff(x)
    if sequence != '':
        for index1 in df1.index:
            df1.loc[index1, 'pH'] = float(sequenced[index1])

    # printing dataframe
    col2.subheader("Table of Values")
    col2.dataframe(df)

    colsep.write(" ")

    # plotting the graph
    col3.subheader("Plot of NaOH added v/s Conductivity")
    col3.line_chart(df.rename(columns={'Volume of NaOH':'index'}).set_index('index'))

    # plotting the graph dy/dx
    col3.subheader("Differential Plot of NaOH added v/s Conductivity")
    col3.line_chart(df1.rename(columns={'Volume of NaOH':'index'}).set_index('index'))


