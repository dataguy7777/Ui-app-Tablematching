import streamlit as st
import streamlit.components.v1 as components

# Set the page configuration
st.set_page_config(page_title="Abstract Instrument Role", layout="wide")

# Page title
st.title("Abstract Instrument Role")

# Define the table data
table_html = """
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
        <td style="border: 1px solid black; padding: 8px;"><a href="#iframe-popup" style="text-decoration: none;">Open View</a></td>
    </tr>
</table>
"""

# Display the table
st.markdown(table_html, unsafe_allow_html=True)

# Define the URL to embed
url = "https://bird.ecb.europa.eu/view/Framework/1544692898369?published=true"

# Add a header for the iframe section
st.markdown("<a name='iframe-popup'></a>", unsafe_allow_html=True)
st.subheader("Detailed View")

# Display the iframe
components.html(
    f"""
    <iframe src="{url}" width="100%" height="800px" frameborder="0"></iframe>
    """,
    height=800,
)
