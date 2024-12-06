import streamlit as st

# Set the page configuration
st.set_page_config(page_title="Abstract Instrument Role", layout="wide")

# Page title
st.title("Abstract Instrument Role")

# Define the URL to embed in the iframe
iframe_url = "https://bird.ecb.europa.eu/view/Framework/1544692898369?published=true"

# Define the table data
data = {
    "Name": ["Abstract Instrument Role"],
    "Code": ["BIRD_ABSTRCT_INSTRMNT_RL_EIL"],
    "Description": ["An Abstract instrument role is a role an Instrument may act in."],
    "Maintenance Agency": ["SDD team (ECB)"],
    "Type of Cube": ["EIL - Enriched Input Layer"],
    "Version": ["1 (01.07.2023 - 31.12.9999)"],
    "Link": ["Click to View Details"],  # Placeholder for clickable link
}

# Render the table
st.subheader("Role Details")
clicked_row = None

for i in range(len(data["Name"])):
    col1, col2, col3, col4, col5, col6, col7 = st.columns(
        [2, 3, 4, 3, 2, 3, 1]
    )  # Define column widths

    with col1:
        st.write(data["Name"][i])
    with col2:
        st.write(data["Code"][i])
    with col3:
        st.write(data["Description"][i])
    with col4:
        st.write(data["Maintenance Agency"][i])
    with col5:
        st.write(data["Type of Cube"][i])
    with col6:
        st.write(data["Version"][i])
    with col7:
        if st.button("View Details", key=f"button_{i}"):
            clicked_row = i  # Track which row's button was clicked

# If a row's button is clicked, display the iframe in a modal-like behavior
if clicked_row is not None:
    st.subheader("Detailed View")
    st.components.v1.html(
        f"""
        <iframe src="{iframe_url}" width="100%" height="600px" frameborder="0"></iframe>
        """,
        height=600,
    )
