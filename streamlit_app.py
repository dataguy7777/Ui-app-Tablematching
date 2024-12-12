import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder, GridUpdateMode
from st_aggrid.shared import JsCode

# Set page configuration
st.set_page_config(
    page_title="Financial Data Dashboard",
    page_icon="📊",
    layout="wide"
)

# App title
st.title("📊 Financial Data Dashboard")

st.markdown(
    """
    Explore financial instrument data, roles, and classifications all in a compact and modern layout. Navigate, view details, and analyze data trends below.
    """
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

# Define a JavaScript function to handle the "Regenerate" button clicks
button_renderer = JsCode("""
function(params) {
    return `
        <button class="regen-button">Regenerate</button>
        <span class="info-icon" title="The LLM with updated generated match">ℹ️</span>
    `;
};
""")

# Configure AgGrid options
gb = GridOptionsBuilder.from_dataframe(df.drop(columns=["Link"]))
gb.configure_column("Details", header_name="Details", cellRenderer=JsCode("""
function(params) {
    return `<a href="${params.value}" target="_blank"><button class="details-button">Details</button></a>`;
};
"""), width=120)
gb.configure_column("Regenerate", header_name="Regenerate", cellRenderer=button_renderer, width=150)
gb.configure_pagination(paginationAutoPageSize=True)
gb.configure_side_bar()

gridOptions = gb.build()

# Define CSS for buttons and info icons
st.markdown("""
<style>
.regen-button {
    background-color: #f0ad4e; /* Orange */
    border: none;
    color: white;
    padding: 6px 12px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 13px;
    margin-right: 5px;
    cursor: pointer;
    border-radius: 4px;
    transition: background-color 0.3s ease;
}

.regen-button:hover {
    background-color: #ec971f;
}

.info-icon {
    font-size: 14px;
    cursor: pointer;
    color: #555;
    position: relative;
}

/* Tooltip Styling */
.info-icon:hover::after {
    content: attr(title);
    position: absolute;
    bottom: 125%; /* Position above the icon */
    left: 50%;
    transform: translateX(-50%);
    background-color: #333;
    color: #fff;
    padding: 5px 8px;
    border-radius: 4px;
    white-space: nowrap;
    font-size: 12px;
    z-index: 1;
    opacity: 1;
    transition: opacity 0.3s;
}

/* Tooltip Arrow */
.info-icon:hover::before {
    content: "";
    position: absolute;
    bottom: 115%; /* Slightly below the tooltip */
    left: 50%;
    transform: translateX(-50%);
    border-width: 5px;
    border-style: solid;
    border-color: #333 transparent transparent transparent;
    z-index: 1;
    opacity: 1;
    transition: opacity 0.3s;
}

/* Hide tooltip by default */
.info-icon::after,
.info-icon::before {
    opacity: 0;
    pointer-events: none;
}
</style>
""", unsafe_allow_html=True)

# Display the AgGrid table
grid_response = AgGrid(
    df.drop(columns=["Link"]),
    gridOptions=gridOptions,
    enable_enterprise_modules=False,
    update_mode=GridUpdateMode.NO_UPDATE,
    allow_unsafe_jscode=True  # Required to render the buttons and tooltips
)

# Capture button clicks (Advanced Implementation)
# This requires more complex integration and is beyond the current scope.
# You can explore Streamlit's Custom Components for deeper interactivity.
