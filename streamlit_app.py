import streamlit as st
import pandas as pd
import numpy as np

# Set page configuration
st.set_page_config(
    page_title="Data Dashboard",
    page_icon="📊",
    layout="wide"
)

# App title
st.title("📊 Data Dashboard for Financial Instruments")

# Sidebar for navigation
st.sidebar.title("Navigation")
selected_tab = st.sidebar.radio("Go to", ["Home", "Instrument Roles", "Risk & Liquidity Instruments", "Market & Collateral Instruments", "Graphs"])

# Data preparation
data1 = [
    {
        "Name": "Abstract Instrument Role",
        "Code": "BIRD_ABSTRCT_INSTRMNT_RL_EIL",
        "Description": "An Abstract instrument role is a role an Instrument may act in.",
        "Maintenance Agency": "SDD team (ECB)",
        "Type of Cube": "EIL - Enriched Input Layer",
        "Version": "1 (01.07.2023 - 31.12.9999)",
        "Link": "https://bird.ecb.europa.eu/view/Framework/1544692898369?published=true",
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
        "Link": "https://bird.ecb.europa.eu/bycode/cube/ECB/BIRD_ASST_PL_DBT_SCRTY_PSTN_ASSGNMNT_EIL?published=true",
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
        "Link": "https://bird.ecb.europa.eu/example2.html",
    },
    {
        "Name": "Liquidity Buffer Instrument",
        "Code": "BIRD_LQD_BFFR_INSTRMNT_EIL",
        "Description": "A Liquidity Buffer Instrument ensures the institution has sufficient liquid assets.",
        "Maintenance Agency": "SDD team (ECB)",
        "Type of Cube": "EIL - Enriched Input Layer",
        "Version": "1 (01.08.2023 - 31.12.9999)",
        "Link": "https://bird.ecb.europa.eu/example3.html",
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
        "Link": "https://bird.ecb.europa.eu/example4.html",
    },
    {
        "Name": "Collateral Instrument Role",
        "Code": "BIRD_CLLTRL_INSTRMNT_RL_EIL",
        "Description": "Indicates the role of an instrument as collateral in secured transactions.",
        "Maintenance Agency": "SDD team (ECB)",
        "Type of Cube": "EIL - Enriched Input Layer",
        "Version": "1 (01.09.2023 - 31.12.9999)",
        "Link": "https://bird.ecb.europa.eu/example5.html",
    }
]

# Function to display data tables
def display_table(data, title):
    st.subheader(f"📋 {title}")
    df = pd.DataFrame(data)
    df = df.drop(columns=["Link"])  # Exclude links from the table for better readability
    st.dataframe(df, use_container_width=True)
    for row in data:
        st.markdown(f"[🔗 More Info for {row['Name']}]({row['Link']})", unsafe_allow_html=True)

# Function to display graphs
def display_graphs():
    st.subheader("📈 Data Graphs")
    st.markdown("Visualize data trends over time.")

    # Sample data for graphs
    df = pd.DataFrame({
        "Time": range(1, 11),
        "Value": np.random.rand(10)
    })

    # Line chart
    st.line_chart(df.set_index("Time"))

    # Area chart
    st.area_chart(df.set_index("Time"))

# Tabs content
if selected_tab == "Home":
    st.subheader("🏠 Welcome to the Data Dashboard")
    st.markdown("""
    This dashboard provides a detailed overview of financial instruments, including their roles, risk, liquidity, market value, 
    and collateral instruments. Explore the sections using the sidebar.
    """)
    st.image("https://www.ecb.europa.eu/home/images/ecb_photo_default.jpg", use_column_width=True)

elif selected_tab == "Instrument Roles":
    display_table(data1, "Instrument Roles")

elif selected_tab == "Risk & Liquidity Instruments":
    display_table(data2, "Risk & Liquidity Instruments")

elif selected_tab == "Market & Collateral Instruments":
    display_table(data3, "Market & Collateral Instruments")

elif selected_tab == "Graphs":
    display_graphs()
