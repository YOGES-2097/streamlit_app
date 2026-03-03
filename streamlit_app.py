import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Data Insights Pro", layout="wide")
st.subheader("Statistical Summary")
st.dataframe(df.describe().style.format("{:.2f}"))
st.title("Data Analysis Dashboard")
st.write("Upload a CSV file to get started.")

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.success("File Uploaded Successfully!")
    st.sidebar.header("Filter Settings")
    all_columns = df.columns.tolist()
    selected_col = st.sidebar.selectbox("Select Column for Analysis", all_columns)
    st.subheader("Raw Data Preview")
    st.dataframe(df.head())
    st.subheader("Statistical Summary")
    st.write(df.describe())
    if df[selected_col].dtype in ['int64', 'float64']:
        st.subheader(f"Advanced Math on {selected_col}")
        
        data_array = df[selected_col].to_numpy()
        mean_val = np.mean(data_array)
        std_val = np.std(data_array)
        
        col1, col2 = st.columns(2)
        col1.metric("Average Value", f"{mean_val:.2f}")
        col2.metric("Standard Deviation", f"{std_val:.2f}")

        outliers = data_array[np.abs(data_array - mean_val) > 2 * std_val]
        st.write(f"Detected {len(outliers)} statistical outliers.")
    else:
        st.warning("Select a numerical column for math analysis.")

else:
    st.info("Awaiting CSV file upload...")