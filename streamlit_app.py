import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Data Insights Pro", layout="wide")

st.title(" Data Analysis Dashboard")
st.write("Upload a CSV file to get started.")

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.success("File Uploaded Successfully!")

    st.sidebar.header("Filter Settings")
    all_columns = df.columns.tolist()
    selected_col = st.sidebar.selectbox("Select Column for Analysis", all_columns)

    col_left, col_right = st.columns(2)

    with col_left:
        st.subheader("Raw Data Preview")
        st.dataframe(df.head())

    with col_right:
        st.subheader("Statistical Summary")
        st.dataframe(df.describe().style.format("{:.2f}"))

    if df[selected_col].dtype in ['int64', 'float64']:
        st.divider() 
        st.subheader(f"Advanced Math on: {selected_col}")
        
        data_array = df[selected_col].to_numpy()
        mean_val = np.mean(data_array)
        std_val = np.std(data_array)
        
        m1, m2, m3 = st.columns(3)
        m1.metric("Average Value", f"{mean_val:.2f}")
        m2.metric("Standard Deviation", f"{std_val:.2f}")
        
        outliers = data_array[np.abs(data_array - mean_val) > 2 * std_val]
        m3.metric("Outliers Detected", len(outliers))
        
        if len(outliers) > 0:
            st.write(f"Note: Found {len(outliers)} values that are more than 2 standard deviations from the mean.")
    else:
        st.warning("Please select a numerical column in the sidebar for math analysis.")

else:
    st.info("Awaiting CSV file upload...")