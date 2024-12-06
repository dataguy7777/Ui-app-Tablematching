import streamlit as st
from streamlit_modal import Modal

# Set the page configuration
st.set_page_config(page_title="Abstract Instrument Role", layout="wide")

# Page title
st.title("Role Details Table")

# Define the table data
data = [
    {
        "Name": "Abstract Instrument Role",
        "Code": "BIRD_ABSTRCT_INSTRMNT_RL_EIL",
        "Description": "An Abstract instrument role is a role an Instrument may act in.",
        "Maintenance Agency": "SDD team (ECB)",
        "Type of Cube": "EIL - Enriched Input Layer",
        "Version": "1 (01.07.2023 - 31.12.9999)",
        "Iframe URL": "https://bird.ecb.europa.eu/view/Cube/3000124535161",
    },
    {
        "Name": "Asset Pool Security Position Assignment",
        "Code": "BIRD_ASST_PL_DBT_SCRTY_PSTN_ASSGNMNT_EIL",
        "Description": (
            "An Asset pool Debt security position assignment is the combination of an "
            "Asset pool and a Debt security position that indicates which (part of a) Debt "
            "security position is comprised in which Asset pool."
        ),
        "Maintenance Agency": "SDD team (ECB)",
        "Type of Cube": "EIL - Enriched Input Layer",
        "Version": "1 (01.07.2023 - 31.12.9999)",
        "Iframe URL": "https://bird.ecb.europa.eu/view/Cube/3000124535210",
    },
]

# Create a modal object
modals = {row["Code"]: Modal(key=f"modal_{row['Code']}", title="Detailed View", max_width=1000) for row in data}

# Render the table
st.subheader("Role Details")
for row in data:
    col1, col2, col3, col4, col5, col6, col7 = st.columns([2, 3, 4, 3, 2, 3, 1])  # Define column widths
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
        # Add a button to open the corresponding modal
        if st.button("View Details", key=f"button_{row['Code']}"):
            modals[row["Code"]].open()

# Define the content of the modals
for row in data:
    modal = modals[row["Code"]]
    if modal.is_open():
        with modal.container():
            st.markdown(f"### {row['Name']} - Detailed View")
            st.components.v1.html(
                f"""
                <iframe src="{row['Iframe URL']}" width="100%" height="600px" frameborder="0"></iframe>
                """,
                height=600,
            )
            if st.button(f"Close Modal {row['Code']}"):
                modal.close()
