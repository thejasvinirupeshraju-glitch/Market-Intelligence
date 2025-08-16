import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Market Intelligence",
    page_icon="📊",
    layout="centered", 
    initial_sidebar_state="collapsed"
)

# --- COLORS ---
primary_color = "#4CAF50"  # soft green
secondary_color = "#2196F3"  # soft blue
button_style = f"""
    <style>
    .stButton>button {{
        background-color: {secondary_color};
        color: white;
        border-radius: 10px;
        padding: 10px 25px;
        font-size: 18px;
        margin: 5px;
    }}
    .stButton>button:hover {{
        background-color: {primary_color};
        color: white;
    }}
    </style>
"""
st.markdown(button_style, unsafe_allow_html=True)

# --- SESSION STATE FOR NAVIGATION ---
if "page" not in st.session_state:
    st.session_state.page = "home"
if "company" not in st.session_state:
    st.session_state.company = None

# --- FUNCTION TO RESET PAGE ---
def go_to_home():
    st.session_state.page = "home"
    st.session_state.company = None

# --- HOMEPAGE ---
if st.session_state.page == "home":
    st.markdown("<h1 style='text-align: center; color: #2196F3;'>Market Intelligence</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size:18px;'>Learn finance concepts and understand the stock market in plain English.</p>", unsafe_allow_html=True)
    
    if st.button("Get Started"):
        st.session_state.page = "companies"

# --- COMPANIES PAGE ---
elif st.session_state.page == "companies":
    st.markdown("<h2 style='text-align: center; color: #2196F3;'>Select a Company</h2>", unsafe_allow_html=True)

    companies = {
        "Microsoft": "https://upload.wikimedia.org/wikipedia/commons/4/44/Microsoft_logo.svg",
        "Apple": "https://upload.wikimedia.org/wikipedia/commons/f/fa/Apple_logo_black.svg",
        "Tesla": "https://upload.wikimedia.org/wikipedia/commons/b/bd/Tesla_Motors.svg",
        "Amazon": "https://upload.wikimedia.org/wikipedia/commons/a/a9/Amazon_logo.svg",
        "Google": "https://upload.wikimedia.org/wikipedia/commons/2/2f/Google_2015_logo.svg"
    }

    for name, logo_url in companies.items():
        col1, col2 = st.columns([1, 5])
        with col1:
            st.image(logo_url, width=40)
        with col2:
            if st.button(name):
                st.session_state.page = "company_detail"
                st.session_state.company = name

    if st.button("Back to Home"):
        go_to_home()

# --- COMPANY DETAIL PAGE ---
elif st.session_state.page == "company_detail":
    company = st.session_state.company
    st.markdown(f"<h2 style='text-align: center; color: #2196F3;'>{company}</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size:18px;'>Select an analysis option to learn more.</p>", unsafe_allow_html=True)

    options = ["Financial Ratios", "Financial Statements", "Industrial Comparisons", "Economic / Political Impact"]
    
    for option in options:
        st.button(option, key=option)
    
    if st.button("Back to Companies"):
        st.session_state.page = "companies"

