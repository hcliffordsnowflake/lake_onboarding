import streamlit
from PIL import Image
streamlit.title('CoDE On-Boarding Form')

image = Image.open('Data_Center_Logo.png')
streamlit.image(image, caption='Center of Data Excellence')
