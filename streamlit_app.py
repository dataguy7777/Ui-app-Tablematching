import streamlit as st
import pandas as pd
import numpy as np

# Set page configuration
st.set_page_config(
    page_title="Financial Data Dashboard",
    page_icon="📊",
    layout="wide"
)

# App title
st.title("📊 Financial Data Dashboard")

st.markdown(
    """Explore financial instrument data, roles, and classifications all in a compact and modern layout. Navigate, view details, and analyze data trends below."""
)

# Data for tables
data = [
    {
        "Name": "Abstract Instrument Role",
        "Code": "BIRD_ABSTRCT_INSTRMNT_RL_EIL",
        "Description": "An Abstract instrument role is a role an Instrument may act in.",
        "Agency": "SDD team (ECB)",
        "Type": "EIL",
        "Version": "1 (01.07.2023 - 31.12.9999)",
        "Link": "https://bird.ecb.europa.eu/view/Framework/1544692898369?published=true",
    },
    {
        "Name": "Asset Pool Security Position Assignment",
        "Code": "BIRD_ASST_PL_DBT_SCRTY_PSTN_ASSGNMNT_EIL",
        "Description": (
            "An Asset pool Debt security position assignment indicates which (part of a) Debt security position is included in which Asset pool."
        ),
        "Agency": "SDD team (ECB)",
        "Type": "EIL",
        "Version": "1 (01.07.2023 - 31.12.9999)",
        "Link": "https://bird.ecb.europa.eu/bycode/cube/ECB/BIRD_ASST_PL_DBT_SCRTY_PSTN_ASSGNMNT_EIL?published=true",
    },
    {
        "Name": "Credit Risk Instrument",
        "Code": "BIRD_CRD_RSK_INSTRMNT_EIL",
        "Description": "A Credit Risk Instrument is used to quantify the probability of default.",
        "Agency": "SDD team (ECB)",
        "Type": "EIL",
        "Version": "1 (01.08.2023 - 31.12.9999)",
        "Link": "https://bird.ecb.europa.eu/example2.html",
    },
    {
        "Name": "Liquidity Buffer Instrument",
        "Code": "BIRD_LQD_BFFR_INSTRMNT_EIL",
        "Description": "A Liquidity Buffer Instrument ensures the institution has sufficient liquid assets.",
        "Agency": "SDD team (ECB)",
        "Type": "EIL",
        "Version": "1 (01.08.2023 - 31.12.9999)",
        "Link": "https://bird.ecb.europa.eu/example3.html",
    },
    {
        "Name": "Market Value Position",
        "Code": "BIRD_MRKT_VAL_PSTN_EIL",
        "Description": "Represents the current market valuation of an instrument.",
        "Agency": "SDD team (ECB)",
        "Type": "EIL",
        "Version": "1 (01.09.2023 - 31.12.9999)",
        "Link": "https://bird.ecb.europa.eu/example4.html",
    },
    {
        "Name": "Collateral Instrument Role",
        "Code": "BIRD_CLLTRL_INSTRMNT_RL_EIL",
        "Description": "Indicates the role of an instrument as collateral in secured transactions.",
        "Agency": "SDD team (ECB)",
        "Type": "EIL",
        "Version": "1 (01.09.2023 - 31.12.9999)",
        "Link": "https://bird.ecb.europa.eu/example5.html",
    }
]

# Convert data to DataFrame for better display
df = pd.DataFrame(data)

# Display data as a table
st.markdown("### 📋 Financial Instrument Overview")

# Style the table for compact view
st.dataframe(
    df.drop(columns=["Link"]),  # Exclude the link column for clarity in the table
    use_container_width=True,
    height=400
)

# Add detailed links in a single row for better visual appeal
st.markdown("### 🔗 Explore Details")
for index, row in df.iterrows():
    st.markdown(f"- [**{row['Name']}**]({row['Link']})")

# Add a sample graph visualization
st.markdown("### 📊 Data Trends")
st.write("Visualize trends with sample data below:")

# Sample data for graph
graph_data = pd.DataFrame({
    "Time": range(1, 11),
    "Value": np.random.rand(10)
})

# Display line chart
st.line_chart(graph_data.set_index("Time"))
