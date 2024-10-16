import streamlit as st

def inject_custom_css():
    st.markdown("""
        <style>
        body {
            color: white !important;
            background-color: black;
        }
        .stApp {
            background-color: black;
            padding-top: 0px;
        }
        .stMarkdown, .stText, .stCode, .stTextInput, .stSelectbox, .stMultiSelect {
            color: white !important;
        }
        .stSelectbox > div > div, 
        .stMultiSelect > div > div,
        .stTextInput > div > div,
        .stNumberInput > div > div {
            background-color: #333 !important;
            color: white !important;
            border: 1px solid #555 !important;
        }
        .stSelectbox > div > div > div[data-baseweb="select"] > div,
        .stMultiSelect > div > div > div[data-baseweb="select"] > div {
            color: white !important;
        }
        .stSelectbox > div > div > div[data-baseweb="select"] > div:last-child {
            color: white !important;
        }
        h1 {
            font-size: 50px;
            font-weight: 700;
            color: #4db8ff !important;
            text-align: center;
        }
        h2, h3 {
            color: white !important;
        }
        .stButton > button {
            background-color: #004080;
            color: white !important;
            border-radius: 8px;
            transition: all 0.3s ease;
            padding: 8px 0; /* Adjust padding to make the buttons more compact */
            border: 1px solid #004080;
            margin: 0 !important; /* Remove all margins */
            border-right: none !important; /* Remove right border between buttons */
            display: inline-block; /* Make sure all buttons are inline */
            width: 150px; /* Set a fixed width for equal button sizes */
        }
        .stButton > button:last-child {
            border-right: 1px solid #004080 !important; /* Ensure the last button has a right border */
        }
        .stButton > button:hover {
            background-color: white;
            color: black !important;
        }
        .element-container, .stDataFrame {
            color: white !important;
        }
        .css-1d391kg, .css-1d391kg .stMarkdown {
            background-color: #1a1a1a;
            color: white !important;
            padding-top: 0px;
        }
        .stFileUploader > div > div {
            background-color: #333 !important;
            color: white !important;
        }
        .js-plotly-plot .plotly {
            background-color: #1a1a1a !important;
        }
        .stApp h1 {
            text-align: center;
        }
        .stApp p.description {
            text-align: center;
            font-size: 18px;
            color: white;
            background-color: #004080;
            padding: 10px;
            border-radius: 5px;
        }
        .stApp hr {
            border: 1px solid #004080;
        }
        .element-container .stAlert {
            background-color: #004080;
            color: white;
            border: none;
            border-radius: 5px;
        }
        .element-container .stAlert.success {
            background-color: #0f5132;
        }
        .element-container .stAlert.error {
            background-color: #842029;
        }
        .element-container .stAlert.info {
            background-color: #087990;
        }
        .stRadio > div {
            color: white !important;
        }
        .stRadio > div > label {
            color: white !important;
        }
        .stDownloadButton > button {
            background-color: #004080;
            color: white !important;
            border-radius: 8px;
            transition: all 0.3s ease;
            margin: 0 !important;
            border-right: none !important; /* Remove right border between buttons */
            display: inline-block; /* Make sure all buttons are inline */
            width: 150px; /* Set a fixed width for equal button sizes */
        }
        .stDownloadButton > button:last-child {
            border-right: 1px solid #004080 !important; /* Ensure the last button has a right border */
        }
        .stDownloadButton > button:hover {
            background-color: white;
            color: black !important;
        }
        .stExpander {
            background-color: #1a1a1a;
            border: 1px solid #004080;
            border-radius: 8px;
            margin-bottom: 20px;
            padding: 10px;
        }
        .stExpander > div:first-child {
            border-bottom: 1px solid #004080;
            padding-bottom: 10px;
            margin-bottom: 10px;
        }
        .stButton {
            margin: 0 !important;
        }
        .stButton > button {
            margin-right: 0 !important; /* Remove margin between buttons */
        }
        .element-container {
            margin-bottom: 20px;
            margin-top: 0px;
        }
        .stRadio > div {
            margin-top: 10px;
            margin-bottom: 10px;
        }

        /* New sidebar styles */
        .sidebar .sidebar-content {
            background-color: #1e2936;
            color: white;
            padding: 0 !important;
        }
        .sidebar .sidebar-content > div:not(:last-child) {
            border-bottom: none;
            padding-bottom: 0 !important;
            margin-bottom: 0 !important;
        }
        .sidebar .sidebar-content .element-container {
            margin: 0 !important;
            padding: 5px 10px !important;
        }
        .sidebar .sidebar-content .element-container:hover {
            background-color: #2c3e50;
        }
        .sidebar .sidebar-content .element-container button {
            background: none !important;
            border: none !important;
            color: white !important;
            font-size: 16px !important;
            text-align: left !important;
            width: 100% !important;
            padding: 3px 0 !important;
        }
        .sidebar .sidebar-content .element-container button:hover {
            background: none;
            color: white !important;
        }
        .sidebar .sidebar-content .element-container button svg,
        .sidebar .sidebar-content .element-container button img {
            margin-right: 10px !important;
            vertical-align: middle !important;
        }
        .main .block-container {
            padding-left: 14rem !important;
        }
        .sidebar .sidebar-content .element-container.active {
            background-color: #34495e !important;
        }
        </style>
    """, unsafe_allow_html=True)

