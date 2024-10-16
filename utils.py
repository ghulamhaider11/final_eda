import pandas as pd
import streamlit as st

def load_data(uploaded_file):
    try:
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
        elif uploaded_file.name.endswith('.xlsx'):
            df = pd.read_excel(uploaded_file)
        return df
    except Exception as e:
        st.error(f"Error: {e}")
        return None

def display_preview_option(dataframe):
    st.subheader("Dataset Preview")
    
    col1, col2 = st.columns([3, 1])
    
    with col1:
        preview_option = st.radio("Select an option:", ("Hide Data Preview", "Show Data Preview"))
    
    with col2:
        if preview_option == "Show Data Preview":
            num_rows = st.number_input("Rows to preview", min_value=1, max_value=len(dataframe), value=5)
    
    if preview_option == "Show Data Preview":
        st.dataframe(dataframe.head(num_rows), use_container_width=True)
        
        col3, col4 = st.columns(2)
        with col3:
            st.info(f"Total rows: {len(dataframe)}")
        with col4:
            st.info(f"Total columns: {len(dataframe.columns)}")
    else:
        st.info("Data preview is hidden. Select 'Show Data Preview' to view the data.")
    
    return preview_option

def get_column_types(dataframe):
    numeric_columns = dataframe.select_dtypes(include=['int64', 'float64']).columns.tolist()
    categorical_columns = dataframe.select_dtypes(include=['object', 'category']).columns.tolist()
    return numeric_columns, categorical_columns

def get_column_stats(dataframe, column):
    stats = dataframe[column].describe()
    return stats