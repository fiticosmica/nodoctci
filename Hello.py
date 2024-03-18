import streamlit as st
from PIL import Image
import pandas as pd
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)
img_ctci = Image.open("media/marca.png")

def run():
    st.set_page_config(
        page_title="Nodo CTCI",
        page_icon="🧬",
    )
    st.image(img_ctci, width=200)
    st.title("CTCI Nodo Centro Sur")
    st.write("El objetivo general es co-crear un modelo de Ciencia Abierta para fortalecer el desarrollo de la ciencia y tecnología en la Macrozona Centro Sur de Chile en concordancia con su territorio y sociedad.")
    st.write("---")

    #archivo_excel = pd.ExcelFile('datos.xlsx')
    #hoja_exel = 'Hoja1'
    
    #df = pd.read_excel(archivo_excel,sheet_name=hoja_exel,usecols='A:N',header=0)
    
    #df_iniciativas= df.groupby(['Macrotema'], as_index=False)
    
    #st.write(df_iniciativas)


if __name__ == "__main__":
    run()
