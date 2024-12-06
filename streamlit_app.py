import streamlit as st
import streamlit.components.v1 as components

# Set the page configuration to maximize window size
st.set_page_config(page_title="Large Webpage Embed", layout="wide")

st.title("Large Webpage Embed Example")

# Define the URL to embed
url = "https://bird.ecb.europa.eu/bycode/cube/ECB/BIRD_ABSTRCT_INSTRMNT_RL_EIL?published=true"

# Add the iframe to the page with adjusted width and height
components.html(
    f"""
    <iframe src="{url}" width="100%" height="800px" frameborder="0"></iframe>
    """,
    height=800,  # Set the height of the iframe
)
