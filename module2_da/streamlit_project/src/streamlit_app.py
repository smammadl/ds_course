import numpy as np
import pandas as pd
import streamlit as st
from pathlib import Path
import plotly.express as px
from utils import get_map, get_scatter_plot, get_histogram, get_correlation_matrix

st.set_page_config(page_title="California Housing Prices", page_icon=":house:", layout="wide")

st.title("My Streamlit App")

tab1, tab2 = st.tabs(["Exploration", "Prediction"])

FILE_DIR = Path(__file__).parent
DATA_DIR = FILE_DIR / "data"

CSV_FILE_PATH = DATA_DIR / "housing.csv"

@st.cache_data
def get_housing_df():
    return pd.read_csv(CSV_FILE_PATH)

housing_df = get_housing_df()

with tab1:
    # -------------------------------------------------------------
    st.header("Data")
    # st.subheader("Table")

    if st.checkbox("Show All Data", value=False):
        st.dataframe(housing_df)
    else:
        st.dataframe(housing_df.head(5))

    if st.checkbox("Show Statistics", value=False):
        st.dataframe(housing_df.describe())

    # -------------------------------------------------------------
    st.header("Map")

    fig = get_map(housing_df)
    st.plotly_chart(fig, width='stretch')
    st.markdown("Colored by Median House Value and Size by Population")

    # -------------------------------------------------------------
    st.markdown("---")
    st.header("Plots")

    numeric_columns = housing_df.select_dtypes(include=['number']).columns.tolist()
    categorical_columns = housing_df.select_dtypes(include=['object']).columns.tolist()

    plot_type = st.radio("Select Plot Type", ["Scatter", "Histogram"], horizontal=True)

    st.markdown("Plot Configuration")
    if plot_type == "Scatter":

        col1, col2, col3, col4, col5 = st.columns(5)

        with col1:
            x_val = st.selectbox("X-Axis", numeric_columns, index=numeric_columns.index("median_income"))
        with col2:
            y_val = st.selectbox("Y-Axis", numeric_columns, index=numeric_columns.index("median_house_value"))
        with col3:
            color_val = st.selectbox("Color", [None] + list(housing_df.columns), index=0)
        with col4:
            size_val = st.selectbox("Size", [None] + list(housing_df.columns), index=0)
        with col5:
            margin_val = st.selectbox("Margin Plot", [None, "box", "histogram"], index=0)

        fig_scatter = get_scatter_plot(housing_df, x_val, y_val, color_val, size_val, margin_val)
        st.plotly_chart(fig_scatter, width='stretch')

    elif plot_type == "Histogram":
        col1, col2 = st.columns(2)
        with col1:
            x_val = st.selectbox("X-Axis", numeric_columns)
        with col2:
            nbins_val = st.slider("Number of Bins", min_value=10, max_value=1000, value=100, step=10)
        
        margin_val = st.checkbox("Margin Plot", value=False)
        fig_histogram = get_histogram(housing_df, x_val, nbins_val, margin_val)
        st.plotly_chart(fig_histogram, width='stretch')

    st.markdown("---")
    st.header("Correlation")
    fig_correlation = get_correlation_matrix(housing_df)
    st.plotly_chart(fig_correlation, width='stretch')
with tab2:
    st.header("PLANNED")