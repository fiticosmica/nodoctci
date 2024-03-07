import streamlit as st
from PIL import Image
import pandas as pd
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)
img_ctci = Image.open("/media/marca.png")

def run():
    st.set_page_config(
        page_title="Nodo CTCI",
        page_icon="🧬",
    )
    st.image(img_ctci, width=200)
    st.title("CTCI Nodo Centro Sur")
    st.write("El objetivo general es co-crear un modelo de Ciencia Abierta para fortalecer el desarrollo de la ciencia y tecnología en la Macrozona Centro Sur de Chile en concordancia con su territorio y sociedad.")
    st.write("---")

    st.markdown(
        """
        Streamlit is an open-source app framework built specifically for
        Machine Learning and Data Science projects.
        **👈 Select a demo from the sidebar** to see some examples
        of what Streamlit can do!
        ### Want to learn more?
        - Check out [streamlit.io](https://streamlit.io)
        - Jump into our [documentation](https://docs.streamlit.io)
        - Ask a question in our [community
          forums](https://discuss.streamlit.io)
        ### See more complex demos
        - Use a neural net to [analyze the Udacity Self-driving Car Image
          Dataset](https://github.com/streamlit/demo-self-driving)
        - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
    """
    )


if __name__ == "__main__":
    run()
