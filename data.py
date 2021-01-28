import streamlit as st
import numpy as np
import pandas as pd
from sklearn import datasets

def app():
    st.title('Data')

    st.write("This is the `Data` page of the multi-page app.")

    st.write("The following is the DataFrame of the `iris` dataset.")

    iris = datasets.load_iris()
    X = pd.DataFrame(iris.data, columns = iris.feature_names)
    Y = pd.Series(iris.target, name = 'class')
    df = pd.concat([X,Y], axis=1)
    df['class'] = df['class'].map({0:"setosa", 1:"versicolor", 2:"virginica"})

    st.write(df)
