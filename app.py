import streamlit as st
import pandas as pd

# Load Honda prefix data (the cleaned data)
prefix_data = pd.DataFrame({
    'Prefix': ['B', 'M', '2', 'C', 'C', 'N', '3', 'D', '4', 'E', 'F', 'R', 'S', '6'],
    'Year': [1981, 1991, 2002, 2012, 1982, 1992, 2003, 2013, 2004, 2014, 2015, 1994, 1995, 2006]
})

# Web app title
st.title("Honda Vehicle Manufacture Year Finder")

# Input field for 車台番号 (Vehicle Code)
vin_code = st.text_input("Enter 車台番号 (e.g., AA01-102345):")

# Function to extract prefix and find year
def get_year_from_vin(vin):
    vin = vin.upper().replace("-", "")  # Remove hyphens and make uppercase
    prefix = vin[:4]  # First 4 characters to match prefix
    result = prefix_data[prefix_data['Prefix'].str.contains(prefix)].iloc[0]
    return result['Year']

# Check for valid VIN and show result
if vin_code:
    try:
        year = get_year_from_vin(vin_code)
        st.write(f"Estimated Year: {year}")
    except:
        st.error("No matching year found. Please check the VIN or prefix.")
