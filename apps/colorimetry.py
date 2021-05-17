import streamlit as st
import pandas as pd
from multiapp import MultiApp
import numpy as np
from sklearn.preprocessing import MinMaxScaler


def app():
    st.header("""Colorimetry""")
    aim_bar = st.beta_expander("About")
    aim_bar.markdown("""
        * **Aim:** To determine maximum wavelength of absorption of CuSO4, verify Beer’s law 
        and find unknown concentration in given sample.
        * **Concepts:**  Electromagnetic radiation, particle and wave like nature of radiation, 
        absorption and transmission of radiation by substance, frequency and wavelength of light. 
        * **Chemicals:** CuSO4, NH3 (Liquor ammonia), distilled water.
        * **Apparatus:** Colorimeter.
        """)

    col1 = st.sidebar
    col2, colsep, col3 = st.beta_columns((1, 0.1, 1.3))

# A_max dataframe
    data = {'Wavelength': [0, 0, 0, 0, 0, 0, 0, 0],
            'Absorbance': [0, 0, 0, 0, 0, 0, 0, 0]}
    df = pd.DataFrame(data)

# Input values in dataframe
    col2.subheader("Values of wavelength(nm)")
    wavelength0 = col2.text_area("Input your values of Wavelength")
    wavelength = wavelength0.splitlines()

    col2.subheader("Values of Absorbance")
    absorbance0 = col2.text_area("Input your values of Absorbance")
    absorbance = absorbance0.splitlines()

    if wavelength0 != '':
        for index in df.index:
            df.loc[index, 'Wavelength'] = float(wavelength[index])

    if absorbance0 != '':
        for index in df.index:
            df.loc[index, 'Absorbance'] = float(absorbance[index])

# print dataframe
    col2.subheader('Table of values')
    col2.dataframe(df)

# finding A_max and W_max
    listofdf = df.values.tolist()
    x = []
    y = []
    a_max = 0
    w_max = 0
    for i in range(0, 8):
        x.append(listofdf[i][0])
        y.append(listofdf[i][1])
        if y[i] > a_max:
            a_max = y[i]
    for j in range(0, 8):
        if y[j] == a_max:
            w_max = x[j]

# print the graph
    col3.subheader("Plot of λ max")
    col3.line_chart(df.rename(columns={'Wavelength': 'index'}).set_index('index'))

# printing A_max and W_max
    col3.subheader("λ max of Solution")
    a_max_print = float(col3.text_input("λ max:", a_max))
    col3.subheader("Wavelength at which λ max is obtained")
    w_max_print = float(col3.text_input("Wavelength:", w_max))

    st.markdown("---")
    st.header("""Predicting Concentration""")
    cola, colsp, colb = st.beta_columns((1, 0.1, 1.3))

# ML segment
# Predicting the unknown concentration

    data_pred = {'Concentration': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                 'Absorbance': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                 'Transmission': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]}
    df_pred = pd.DataFrame(data_pred)

# Input values in dataframe
    cola.subheader("Values of Concentration")
    concentration0 = cola.text_area("Input values of Concentration")
    concentration = concentration0.splitlines()

    cola.subheader("Values of Absorbance")
    abs0 = cola.text_area("Input values of Absorbance")
    abs = abs0.splitlines()

    cola.subheader("Values of Transmission")
    transmission0 = cola.text_area("Input values of Transmission")
    transmission = transmission0.splitlines()

    if concentration0 != '':
        for index in df_pred.index:
            df_pred.loc[index, 'Concentration'] = float(concentration[index])

    if abs0 != '':
        for index in df_pred.index:
            df_pred.loc[index, 'Absorbance'] = float(abs[index])

    if transmission0 != '':
        for index in df_pred.index:
            df_pred.loc[index, 'Transmission'] = float(transmission[index])

# print dataframe
    colb.subheader('Table of values')
    colb.dataframe(df_pred)

# Input values of unknown
    colb.subheader("Values for unknown Concentration")
    abs1 = float(colb.text_input("Input the value of Absorbance", 0.0))
    transmission1 = float(colb.text_input("Input the value of Transmission", 0.0))
    x_test = [[abs1, transmission1]]

# predicting value
    x1 = df_pred.iloc[:, [1,  2]].values
    x1 = np.append(x1, x_test, 0)
    y1 = df_pred.iloc[:, 0].values

    # normalization
    scale = MinMaxScaler()
    x1 = scale.fit_transform(x1)

    # normalized input
    x_test1 = [x1[5]]

    # Regression
    from sklearn.linear_model import LinearRegression
    model = LinearRegression()
    x1 = np.delete(x1, 5, 0)
    model.fit(x1, y1)

    y_pred = model.predict(x_test1)

# printing predicted value
    colb.subheader("Value of unknown Concentration")
    colb.text_input(" ", y_pred[0])

# result
    st.markdown("---")
    col7, col8, col9 = st.beta_columns((1, 0.1, 1.3))
    col7.header("""Result""")
    col7.subheader("λ max was obtained to be")
    col7.text_input(" a_max val ", a_max)
    col7.subheader("Wavelength at which λ max was obtained is:")
    col7.text_input(" w_max val ", w_max)
    col7.subheader("Concentration of unknown solution was predicted to be:")
    col7.text_input(" y_pred val ", y_pred[0])































