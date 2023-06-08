import streamlit
from PIL import Image
streamlit.title('Center of Data Excellence On-Boarding Form')

image = Image.open('Data_Center_Logo.png')
streamlit.image(image, caption='Center of Data Excellence')
