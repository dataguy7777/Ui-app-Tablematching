import streamlit as st

# Set the page configuration
st.set_page_config(page_title="Abstract Instrument Role", layout="wide")

# Page title
st.title("Abstract Instrument Role")

# Define the URL to embed in the iframe
iframe_url = "https://bird.ecb.europa.eu/view/Framework/1544692898369?published=true"

# Define the table data
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
            <button id="dialog-trigger" style="background-color: #4CAF50; color: white; border: none; padding: 6px 12px; cursor: pointer;">Open View</button>
        </td>
    </tr>
</table>
"""

# Display the table
st.markdown(table_html, unsafe_allow_html=True)

# Trigger for dialog
if st.button("Open Detailed View"):
    # Create and display the dialog
    with st.dialog("Detailed View"):
        st.markdown(f"### Detailed View")
        st.components.v1.html(
            f"""
            <iframe src="{iframe_url}" width="100%" height="600px" frameborder="0"></iframe>
            """,
            height=600,
        )
