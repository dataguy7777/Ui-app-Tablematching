import streamlit as st
from streamlit_modal import Modal

# Set the page configuration
st.set_page_config(page_title="Abstract Instrument Role", layout="wide")

# Page title
st.title("Abstract Instrument Role")

# Define a modal object
modal = Modal(key="iframe_modal", title="Detailed View", max_width=1000)

# Define the URL to embed
iframe_url = "https://bird.ecb.europa.eu/view/Framework/1544692898369?published=true"

# Create a table with a link to open the modal
table_html = f"""
<table style="width:100%; border: 1px solid black; border-collapse: collapse;">
    <tr style="border: 1px solid black; text-align: left; padding: 8px;">
        <th style="border: 1px solid black; padding: 8px;">Name</th>
        <th style="border: 1px solid black; padding: 8px;">Code</th>
        <th style="border: 1px solid black; padding: 8px;">Description</th>
        <th style="border: 1px solid black; padding: 8px;">Maintenance Agency</th>
        <th style="border: 1px solid black; padding: 8px;">Type of Cube</th>
        <th style="border: 1px solid black; padding: 8px;">Version</th>
        <th style="border: 1px solid black; padding: 8px;">Link</th>
    </tr>
    <tr style="border: 1px solid black; text-align: left; padding: 8px;">
        <td style="border: 1px solid black; padding: 8px;">Abstract Instrument Role</td>
        <td style="border: 1px solid black; padding: 8px;">BIRD_ABSTRCT_INSTRMNT_RL_EIL</td>
        <td style="border: 1px solid black; padding: 8px;">An Abstract instrument role is a role an Instrument may act in.</td>
        <td style="border: 1px solid black; padding: 8px;">SDD team (ECB)</td>
        <td style="border: 1px solid black; padding: 8px;">EIL - Enriched Input Layer</td>
        <td style="border: 1px solid black; padding: 8px;">1 (01.07.2023 - 31.12.9999)</td>
        <td style="border: 1px solid black; padding: 8px;">
            <button onclick="document.getElementById('modal-trigger').click()" style="background-color: #4CAF50; color: white; border: none; padding: 6px 12px; cursor: pointer;">Open View</button>
        </td>
    </tr>
</table>
"""

# Display the table
st.markdown(table_html, unsafe_allow_html=True)

# Create a button to open the modal
if st.button("Open Detailed View", key="modal-trigger"):
    modal.is_open = True

# Define the content of the modal
with modal.container():
    st.subheader("Detailed View")
    st.components.v1.html(
        f"""
        <iframe src="{iframe_url}" width="100%" height="600px" frameborder="0"></iframe>
        """,
        height=600,
    )

# Render the modal
modal.render()
