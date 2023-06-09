import streamlit
import snowflake.connector
from PIL import Image
streamlit.title('CoDE On-Boarding Form Test')

image = Image.open('Data_Center_Logo.png')
streamlit.image(image, caption='Center of DATA Excellence')

# Connect to Snowflake
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)
