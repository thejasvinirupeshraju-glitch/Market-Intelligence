import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Market Intelligence",
    page_icon="📊",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- COLORS & BUTTON STYLE ---
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
        width: 200px;
        display: block;
        margin-left: auto;
        margin-right: auto;
    }}
    .stButton>button:hover {{
        background-color: {primary_color};
        color: white;
    }}
    .company-btn {{
        text-align: left;
    }}
    </style>
"""
st.markdown(button_style, unsafe_allow_html=True)

# --- SESSION STATE FOR NAVIGATION ---
if "page" not in st.session_state:
    st.session_state.page = "home"
if "company" not in st.session_state:
    st.session_state.company = None
if "analysis_page" not in st.session_state:
    st.session_state.analysis_page = None

# --- NAVIGATION FUNCTIONS ---
def go_to_home():
    st.session_state.page = "home"
    st.session_state.company = None
    st.session_state.analysis_page = None

def go_to_companies():
    st.session_state.page = "companies"
    st.session_state.analysis_page = None

def go_to_analysis(option):
    st.session_state.analysis_page = option

# --- HOMEPAGE ---
if st.session_state.page == "home":
    st.markdown("<h1 style='text-align: center; color: #2196F3;'>Market Intelligence</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size:18px;'>Learn finance concepts and understand the stock market in plain English.</p>", unsafe_allow_html=True)
    
    st.markdown("<div style='text-align:center;'>", unsafe_allow_html=True)
    if st.button("Get Started"):
        go_to_companies()
    st.markdown("</div>", unsafe_allow_html=True)

# --- COMPANIES PAGE ---
elif st.session_state.page == "companies":
    st.markdown("<h2 style='text-align: center; color: #2196F3;'>Select a Company</h2>", unsafe_allow_html=True)

    companies = {
        "Microsoft": "https://1000logos.net/wp-content/uploads/2021/04/Microsoft-logo.png",
        "Apple": "https://1000logos.net/wp-content/uploads/2016/10/Apple-Logo.png",
        "Tesla": "https://1000logos.net/wp-content/uploads/2021/04/Tesla-Logo.png",
        "Amazon": "https://1000logos.net/wp-content/uploads/2016/10/Amazon-Logo.png",
        "Google": "https://1000logos.net/wp-content/uploads/2016/10/Google-Logo.png"
    }

    for name, logo_url in companies.items():
        col1, col2 = st.columns([1, 5])
        with col1:
            st.image(logo_url, width=50, use_column_width=False)
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
        if st.button(option):
            go_to_analysis(option)

    if st.session_state.analysis_page:
        st.markdown(f"<h3 style='text-align:center; color: #4CAF50;'>{st.session_state.analysis_page}</h3>", unsafe_allow_html=True)
        st.write("This is where the explanation of **plain English finance concepts** will go.")
        st.write("You can later fill this with charts, text, or interactive examples for users.")

    if st.button("Back to Companies"):
        go_to_companies()
