# Main Home Page for MDM4U
# Service Account: mdm4u-data-grabber@mdm4u-468715.iam.gserviceaccount.com

# imports
import streamlit as st
import gspread

# configuration, secrets, google sheets connection
st.set_page_config(layout="wide")
sheet_key = st.secrets["keys"]["file_key"] # The Google Sheet's Key

gc_cred = st.secrets["google"] # Google Sheets Service Agent credentials
gc = gspread.service_account_from_dict(gc_cred) # Connecting to the Service Account
sheet_file = gc.open_by_key(sheet_key)
worksheet = sheet_file.get_worksheet(0) # Getting the Google Form Response Sheet
data = worksheet.get_all_records() # Fetching all records from the sheet
print(data)

# content
st.title("Data Management (MDM4U)")

# Links to other pages
st.badge("Links:", color="blue", icon=":material/link:")
link1, link2, link3 = st.columns(3, border=False)
with link1:
    st.page_link("pages/unit1.py", label="Unit 1: Data and Statistical Analysis", icon=":material/analytics:", width="stretch")

with link2:
    st.page_link("pages/unit2.py", label="Unit 2: Probability", icon=":material/casino:", width="stretch")

with link3:
    st.page_link("https://classroom.google.com/c/Nzk1MjE4NzAwODA2?cjc=zy2wwl6d", label="Google Classroom", icon=":material/school:", width="stretch")

st.header("Assessments Dates")

st.header("Homework")
