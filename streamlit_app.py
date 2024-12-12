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

# Add "Details" column with HTML button links
df['Details'] = df['Link'].apply(
    lambda x: f'''
        <a href="{x}" target="_blank">
            <button class="details-button">Details</button>
        </a>
    '''
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
    
    /* Responsive Design */
    @media screen and (max-width: 768px) {
        th, td {
            padding: 8px 10px;
        }
        .details-button {
            padding: 6px 12px;
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
    height=600,  # Adjust height as needed
    scrolling=True
)
