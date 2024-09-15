import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import pyodbc

# Function to connect to SQL Server and fetch data
def get_data_from_sql():
	conn = pyodbc.connect(
		'DRIVER={ODBC Driver 17 for SQL Server};'
		'SERVER=202.66.174.120,1232;'
		'DATABASE=vaagmndb;'
		'UID=vaagdadbusr;'
		'PWD=MefrAyu!Uw8they9ru;'
	)
	
	query = "SELECT Employee_Name as name, Employee_Code as code, Employee_Gender as gender, Employee_DOB as dob, GrossSalary as salary FROM EmployeeMater"
	df = pd.read_sql(query, conn)
	conn.close()
	return df

# Load the data from SQL Server
df = get_data_from_sql()

st.sidebar.header('Select Employee Name')
store_name = st.sidebar.selectbox('Employee Name', df['name'].unique())

# Filter data for the selected store
store_data = df[df['name'] == store_name].iloc[0]

# Display store attributes
st.header(f'Employee: {store_name}')
st.write('### Employee Details')
st.write(f"Code: {store_data['code']}")
st.write(f"Gender: {store_data['gender']}")
st.write(f"DOB: {store_data['dob']}")
st.write(f"Salary: {store_data['salary']}")
