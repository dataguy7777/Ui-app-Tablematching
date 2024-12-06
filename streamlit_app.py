import streamlit as st
from streamlit_modal import Modal
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Configure page
st.set_page_config(page_title="Data and Graph Navigation", layout="wide")

st.title("Data Navigation Example")

# Sample data for three tables
data1 = [
    {
        "Name": "Abstract Instrument Role",
        "Code": "BIRD_ABSTRCT_INSTRMNT_RL_EIL",
        "Description": "An Abstract instrument role is a role an Instrument may act in.",
        "Maintenance Agency": "SDD team (ECB)",
        "Type of Cube": "EIL - Enriched Input Layer",
        "Version": "1 (01.07.2023 - 31.12.9999)",
        "Iframe URL": "https://bird.ecb.europa.eu/view/Framework/1544692898369?published=true",
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
        "Iframe URL": "https://bird.ecb.europa.eu/bycode/cube/ECB/BIRD_ASST_PL_DBT_SCRTY_PSTN_ASSGNMNT_EIL?published=true",
    }
]

data2 = [
    {
        "Name": "Credit Risk Instrument",
        "Code": "BIRD_CRD_RSK_INSTRMNT_EIL",
        "Description": "A Credit Risk Instrument is used to quantify the probability of default.",
        "Maintenance Agency": "SDD team (ECB)",
        "Type of Cube": "EIL - Enriched Input Layer",
        "Version": "1 (01.08.2023 - 31.12.9999)",
        "Iframe URL": "https://bird.ecb.europa.eu/example2.html",
    },
    {
        "Name": "Liquidity Buffer Instrument",
        "Code": "BIRD_LQD_BFFR_INSTRMNT_EIL",
        "Description": "A Liquidity Buffer Instrument ensures the institution has sufficient liquid assets.",
        "Maintenance Agency": "SDD team (ECB)",
        "Type of Cube": "EIL - Enriched Input Layer",
        "Version": "1 (01.08.2023 - 31.12.9999)",
        "Iframe URL": "https://bird.ecb.europa.eu/example3.html",
    }
]

data3 = [
    {
        "Name": "Market Value Position",
        "Code": "BIRD_MRKT_VAL_PSTN_EIL",
        "Description": "Represents the current market valuation of an instrument.",
        "Maintenance Agency": "SDD team (ECB)",
        "Type of Cube": "EIL - Enriched Input Layer",
        "Version": "1 (01.09.2023 - 31.12.9999)",
        "Iframe URL": "https://bird.ecb.europa.eu/example4.html",
    },
    {
        "Name": "Collateral Instrument Role",
        "Code": "BIRD_CLLTRL_INSTRMNT_RL_EIL",
        "Description": "Indicates the role of an instrument as collateral in secured transactions.",
        "Maintenance Agency": "SDD team (ECB)",
        "Type of Cube": "EIL - Enriched Input Layer",
        "Version": "1 (01.09.2023 - 31.12.9999)",
        "Iframe URL": "https://bird.ecb.europa.eu/example5.html",
    }
]

# Create dictionaries to store modals for each data row keyed by Code
modals = {}
for row in data1 + data2 + data3:
    key = f"modal_{row['Code']}"
    modals[key] = Modal(key=key, title="Detailed View", max_width=1000)

# Function to display a table with modals
def display_table_with_modals(data, table_name):
    # Display fields as a list (excluding "Iframe URL")
    st.write("**Fields:**")
    fields = [f for f in data[0].keys() if f != "Iframe URL"]
    for field in fields:
        st.write(f"- {field}")

    # Display table rows
    for row in data:
        col1, col2, col3, col4, col5, col6, col7 = st.columns([2, 3, 4, 3, 2, 3, 1])
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
            modal_key = f"modal_{row['Code']}"
            if st.button("View Details", key=f"button_{row['Code']}_{table_name}"):
                modals[modal_key].open()

    # Define the content of the modals if opened
    for row in data:
        modal_key = f"modal_{row['Code']}"
        modal = modals[modal_key]
        if modal.is_open():
            with modal.container():
                st.markdown(f"### {row['Name']} - Detailed View")
                st.components.v1.html(
                    f"""
                    <iframe src="{row['Iframe URL']}" width="100%" height="600px" frameborder="0"></iframe>
                    """,
                    height=600,
                )
                if st.button(f"Close Modal {row['Code']}", key=f"close_{row['Code']}_{table_name}"):
                    modal.close()

# Create tabs for navigation
tabs = st.tabs(["Table 1", "Table 2", "Table 3", "Graph"])

with tabs[0]:
    st.subheader("Table 1: Instrument Roles")
    display_table_with_modals(data1, "table1")

with tabs[1]:
    st.subheader("Table 2: Risk & Liquidity Instruments")
    display_table_with_modals(data2, "table2")

with tabs[2]:
    st.subheader("Table 3: Market & Collateral Instruments")
    display_table_with_modals(data3, "table3")

with tabs[3]:
    st.subheader("Graph & Related Information")
    # Display fields for the graph
    st.write("**Fields (for the displayed data set):**")
    st.write("- Time")
    st.write("- Value")

    # Provide a link (example link)
    st.write("[Visit ECB Bird Framework](https://bird.ecb.europa.eu/)")

    # Create some sample data for the chart
    df = pd.DataFrame({"Time": range(1, 11), "Value": np.random.rand(10)})
    df = df.set_index("Time")

    # Display a simple line chart
    st.line_chart(df["Value"])
