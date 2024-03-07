import streamlit as st
from PIL import Image
import pandas as pd
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)
img_ctci = Image.open("media/marca.png")
#df = pd.read_csv('data.csv')

def run():
    st.set_page_config(
        page_title="Nodo CTCI",
        page_icon="🧬",
    )
    st.image(img_ctci, width=200)
    st.title("CTCI Nodo Centro Sur")
    st.write("El objetivo general es co-crear un modelo de Ciencia Abierta para fortalecer el desarrollo de la ciencia y tecnología en la Macrozona Centro Sur de Chile en concordancia con su territorio y sociedad.")
    st.write("---")

if __name__ == "__main__":
    run()
