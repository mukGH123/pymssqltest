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
	
	query = "SELECT Employee_Name, Employee_Code, Employee_Gender, Employee_DOB, GrossSalary FROM EmployeeMater"
	df = pd.read_sql(query, conn)
	conn.close()
	return df

# Load the data from SQL Server
df = get_data_from_sql()
