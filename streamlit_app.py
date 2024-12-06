import streamlit as st
from streamlit_modal import Modal

# Set the page configuration
st.set_page_config(page_title="Abstract Instrument Role", layout="wide")

# Page title
st.title("Abstract Instrument Role")

# Define the URL to embed in the iframe
iframe_url = "https://bird.ecb.europa.eu/view/Framework/1544692898369?published=true"

# Define the table data
data = [
    {
        "Name": "Abstract Instrument Role",
        "Code": "BIRD_ABSTRCT_INSTRMNT_RL_EIL",
        "Description": "An Abstract instrument role is a role an Instrument may act in.",
        "Maintenance Agency": "SDD team (ECB)",
        "Type of Cube": "EIL - Enriched Input Layer",
        "Version": "1 (01.07.2023 - 31.12.9999)",
    }
]

# Create a modal object
modal = Modal(key="iframe_modal", title="Detailed View", max_width=1000)

# Render the table
st.subheader("Role Details")
for row in data:
    col1, col2, col3, col4, col5, col6, col7 = st.columns(
        [2, 3, 4, 3, 2, 3, 1]
    )  # Define column widths for layout
    with col1:
        st.write(row["Name"])
    with col2:
        st.write(row["Code"])
    with col3:
        st.write(row["Description"])
    with col4:
        st.write(row["Maintenance Agency"])
    with col5:
        st.write(row["Type of Cube"])
    with col6:
        st.write(row["Version"])
    with col7:
        # Add a button to open the modal
        if st.button("View Details", key=f"button_{row['Code']}"):
            modal.open()

# Define the content of the modal
if modal.is_open():
    with modal.container():
        st.markdown("### Abstract Instrument Role - Detailed View")
        st.components.v1.html(
            f"""
            <iframe src="{iframe_url}" width="100%" height="600px" frameborder="0"></iframe>
            """,
            height=600,
        )
        if st.button("Close Modal"):
            modal.close()
