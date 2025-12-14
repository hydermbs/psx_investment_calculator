import streamlit as st
from file import PSXInvestmentCalculator

st.set_page_config(
    page_title="PSX Investment Calculator",
    page_icon="📈",
    layout="centered"
)

def load_css():
    with open("styles.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
        st.markdown('<meta name="viewport" content="width=device-width, initial-scale=1">', unsafe_allow_html=True)


def design_Header():
    st.title("KSE-100 Investment Calculator")
    st.write("Kickstart your PSX portfolio. Get instant access to leading KSE-100 companies, sorted by market index weight.")

def design_Results_Header(top_companies):
    col1, col2, col3,col4 = st.columns(4)
    with col1:
        st.subheader("Company Name")
    with col2:
        st.subheader("Sector")
    with col3:
        st.subheader("Percentage")
    with col4:
        st.subheader("Amount (PKR)")
    
    st.divider()
    
def design_Results_Data(top_companies):
    for _, row in top_companies.iterrows():
        col1, col2, col3,col4 = st.columns(4)
        with col1:
            st.write(row["NAME"])
        with col2:
            st.write(row["sectorName"])
        with col3:
            st.write(f"{row['Normalized_percentage']:.2f}%")
        with col4:
            st.write(f"{row['Investment amount']:,.2f}")

def get_input():
    total_investment = st.number_input("Total Investment", value=100000, min_value=0)
    num_companies = st.number_input("Number of Companies", value=5, min_value=1)
    index_name = st.selectbox("Select Index", ["KSE100", "KMI30"])
    return total_investment, num_companies, index_name

load_css()
design_Header()
total_investment, num_companies, index_name = get_input()
if st.button("Calculate"):

    top_companies = PSXInvestmentCalculator(total_investment,num_companies, index_name).main()
    design_Results_Header(top_companies)
    design_Results_Data(top_companies)
