# Main Home Page for MDM4U
# Service Account: mdm4u-data-grabber@mdm4u-468715.iam.gserviceaccount.com

# imports
import streamlit as st
import gspread
from datetime import datetime

# configuration, secrets, google sheets connection
st.set_page_config(layout="wide")
sheet_key = st.secrets["keys"]["file_key"] # The Google Sheet's Key

gc_cred = st.secrets["google"] # Google Sheets Service Agent credentials
gc = gspread.service_account_from_dict(gc_cred) # Connecting to the Service Account
sheet_file = gc.open_by_key(sheet_key)
worksheet = sheet_file.get_worksheet(0) # Getting the Google Form Response Sheet
data = worksheet.get_all_records() # Fetching all records from the sheet

assessments = []
homeworks = []
completed = []
current_date = datetime.now().strftime("%m/%d/%Y")

for row in data:
    current_dict = {
        'timestamp' : row['Timestamp'],
        'link': row['link'],
        'due_date': row['due_date'],
        'title': row['title']
    }

    today = datetime.strptime(current_date, "%m/%d/%Y")
    task_date = datetime.strptime(current_dict["due_date"], "%m/%d/%Y")

    if today > task_date:
        completed.append(current_dict)
    elif row["task_type"] == "Homework":
        homeworks.append(current_dict)
    elif row["task_type"] == "Assessment":
        assessments.append(current_dict)

assessments.sort(
    key=lambda x: datetime.strptime(x["due_date"], "%m/%d/%Y"),
)
homeworks.sort(
    key=lambda x: datetime.strptime(x["due_date"], "%m/%d/%Y"),
)
# end of initialization

# content
st.title("Data Management (MDM4U)")
st.write(f"Current Date: {current_date}")

# Links to other pages
st.badge("Links:", color="blue", icon=":material/link:")
link1, link2, link3 = st.columns(3, border=False)
with link1:
    st.page_link("pages/unit1.py", label="Unit 1: Data and Statistical Analysis", icon=":material/analytics:", width="stretch")

with link2:
    st.page_link("pages/unit2.py", label="Unit 2: Probability", icon=":material/casino:", width="stretch")

with link3:
    st.page_link("https://classroom.google.com/c/Nzk1MjE4NzAwODA2?cjc=zy2wwl6d", label="Google Classroom", icon=":material/school:", width="stretch")

# Assessment Data
st.header(":material/assignment: Assessment Dates")
for i, task in enumerate(assessments):
    #st.markdown(f"- **{task['title']}**: [Link]({task['link']}) (Due: {task['due_date']})")
    with st.container(border=True, key=f"a_row_{i}"):
        col1, col2 = st.columns(2)

        with col1:
            if len(task["link"]) < 2:
                st.write(f"**{task["title"]}**")
            else:
                st.write(f"**[{task["title"]}]({task["link"]})**")
        
        with col2:
            st.write(f"**Due Date:** {task["due_date"]}")
# End of Assessments

# Homework Data
st.header(":material/checklist: Homework")
for i, task in enumerate(homeworks):
    #st.markdown(f"- **{task['title']}**: [Link]({task['link']}) (Due: {task['due_date']})")
    with st.container(border=True, key=f"hw_row_{i}"):
        col1, col2 = st.columns(2)

        with col1:
            if len(task["link"]) < 2:
                st.write(f"**{task["title"]}**")
            else:
                st.write(f"**[{task["title"]}]({task["link"]})**")
        
        with col2:
            st.write(f"**Due Date:** {task["due_date"]}")
# End of Homework

# Completed Tasks
with st.expander("**Completed Tasks**"):
    for row in completed:
        if len(row["link"]) < 2:
            st.markdown(f"- **{row['title']}** (Completed on: {row['due_date']})")
        else:
            st.markdown(f"- **{row['title']}**: [Link]({row['link']}) (Completed on: {row['due_date']})")
# End of Completed Tasks