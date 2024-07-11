import pandas as pd 
import streamlit as st
def main():
    st.title("CSV Data Display")

    # Upload CSV file
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

    if uploaded_file is not None:
        # Read CSV file
        df = pd.read_csv('insurance.csv')

        # Display CSV file
        st.write(df)

if __name__ == "__main__":
    main()