import pandas as pd 
import streamlit as st

def main():
    st.title("CSV Data Display")

    csv_file_path = "insurance.csv"

    df = pd.read_csv(csv_file_path)

    st.write(df)

if __name__ == "__main__":
    main()
