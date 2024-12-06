import streamlit as st
import streamlit.components.v1 as components

# Set the page configuration
st.set_page_config(page_title="Abstract Instrument Role", layout="wide")

# Page title
st.title("Abstract Instrument Role Information")

# Define the table data
table_data = {
    "Attribute": [
        "Name", 
        "Code", 
        "Description", 
        "Maintenance agency", 
        "Type of cube", 
        "Version"
    ],
    "Value": [
        "Abstract instrument role", 
        "BIRD_ABSTRCT_INSTRMNT_RL_EIL", 
        "An Abstract instrument role is a role an Instrument may act in.", 
        "SDD team (ECB)", 
        "EIL - Enriched Input Layer", 
        "1 (01.07.2023 - 31.12.9999)"
    ]
}

# Display the table
st.subheader("Details Table")
st.table(table_data)

# Define the URL to embed
url = "https://bird.ecb.europa.eu/view/Framework/1544692898369?published=true"

# Add a button to show the iframe
if st.button("Open Detailed View"):
    # Show iframe when button is clicked
    st.subheader("Detailed View")
    components.html(
        f"""
        <iframe src="{url}" width="100%" height="800px" frameborder="0"></iframe>
        """,
        height=800,
    )
