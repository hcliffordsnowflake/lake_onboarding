import streamlit
import snowflake.connector
from PIL import Image
streamlit.title('CoDE On-Boarding Forms')

image = Image.open('Data_Center_Logo.png')
streamlit.image(image, caption='Center of Data Excellence')
