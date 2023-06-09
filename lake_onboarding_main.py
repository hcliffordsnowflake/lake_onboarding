import streamlit
import snowflake.connector
from PIL import Image
streamlit.title('CoDE On-Boarding Form Test')

image = Image.open('Data_Center_Logo.png')
streamlit.image(image, caption='Center of DATA Excellence')

# Connect to Snowflake and retreive the business units
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT BUSINESS_UNIT_DESCRIPTION FROM BUSINESS_UNIT")
my_data_rows = my_cur.fetchall()
streamlit.text("Please select a business unit:")
streamlit.dataframe(my_data_rows)
