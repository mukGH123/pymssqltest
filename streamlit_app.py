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
# Format Store IDs (name in your case) to avoid comma separation
df['name'] = df['name'].astype(str)


# Define pages
def store_details():
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
	
	# Pie chart for Male/Female Population
	st.write('### Employee Gender Salary')
	labels = ['Gender', 'Salary']
	sizes = [store_data['gender'], store_data['salary']]
	colors = ['#ff9999', '#66b3ff']
	explode = (0.1, 0)  # explode the 1st slice
	
	fig1, ax1 = plt.subplots()
	ax1.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%',
	shadow=True, startangle=90)
	ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
	
	st.pyplot(fig1)


# Create a navigation menu
st.sidebar.title('Navigation')
page = st.sidebar.radio('Go to', ['Employee Details', 'Employee Statistics', 'Employee Comparison'])

st.markdown(
    """
    <style>
    [data-testid="stElementToolbar"] {
        display: none;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Render the selected page
if page == 'Employee Details':
    store_details()
elif page == 'Employee Statistics':
    store_details()
elif page == 'Employee Comparison':
    store_details()
