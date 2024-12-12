import streamlit as st
import pandas as pd
import streamlit.components.v1 as components

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
    Explore financial instrument data, roles, and classifications all in a compact and modern layout. Navigate, view details, and perform actions directly from the table below.
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

# Add "Details" column with HTML button links without newline characters
df['Details'] = df['Link'].apply(
    lambda x: f'<a href="{x}" target="_blank"><button class="details-button">Details</button></a>'
)

# Add "Regenerate" column with button and info icon without newline characters
df['Regenerate'] = df['Link'].apply(
    lambda x: '<div class="regen-container"><button class="regen-button">Regenerate</button><span class="info-icon" title="The LLM with updated generated match">ℹ️</span></div>'
)

# Select columns to display, excluding 'Link'
display_df = df.drop(columns=["Link"])

# Function to generate styled HTML table
def generate_styled_table(dataframe):
    # Define CSS styles
    styles = """
    <style>
    /* Table Container */
    .table-container {
        overflow-x: auto;
    }
    
    /* Styled Table */
    table {
        width: 100%;
        border-collapse: collapse;
        font-family: Arial, sans-serif;
    }
    
    /* Table Header */
    th {
        position: sticky;
        top: 0;
        background-color: #4CAF50;
        color: white;
        padding: 12px 15px;
        text-align: left;
    }
    
    /* Table Rows */
    td {
        padding: 12px 15px;
        border-bottom: 1px solid #ddd;
        vertical-align: middle;
    }
    
    /* Striped Rows */
    tr:nth-child(even) {
        background-color: #f9f9f9;
    }
    
    /* Hover Effect */
    tr:hover {
        background-color: #f1f1f1;
    }
    
    /* Details Button Styling */
    .details-button {
        background-color: #008CBA; /* Blue */
        border: none;
        color: white;
        padding: 8px 16px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 14px;
        margin: 2px 0;
        cursor: pointer;
        border-radius: 4px;
        transition: background-color 0.3s ease;
    }
    
    .details-button:hover {
        background-color: #005f6a;
    }
    
    /* Regenerate Button Styling */
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
    
    /* Info Icon Styling */
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
    
    /* Responsive Design */
    @media screen and (max-width: 768px) {
        th, td {
            padding: 8px 10px;
        }
        .details-button, .regen-button {
            padding: 6px 10px;
            font-size: 12px;
        }
        .info-icon {
            font-size: 12px;
        }
    }
    </style>
    """
    
    # Generate HTML table
    table_html = dataframe.to_html(escape=False, index=False, classes='styled-table')
    
    # Wrap the table in a div for horizontal scrolling on small screens
    final_html = f"""
    {styles}
    <div class="table-container">
        {table_html}
    </div>
    """
    return final_html

# Generate the styled table HTML
styled_table = generate_styled_table(display_df)

# Display the styled table using components.html
components.html(
    styled_table,
    height=700,  # Adjust height as needed
    scrolling=True
)
