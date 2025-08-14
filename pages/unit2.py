# Streamlit Page for Unit 2
# Service Account: mdm4u-data-grabber@mdm4u-468715.iam.gserviceaccount.com

# imports
import streamlit as st
import gspread
from datetime import datetime

# data
st.set_page_config(layout="wide")
sheet_key = st.secrets["keys"]["file_key"] # The Google Sheet's Key

gc_cred = st.secrets["google"] # Google Sheets Service Agent credentials
gc = gspread.service_account_from_dict(gc_cred) # Connecting to the Service Account
sheet_file = gc.open_by_key(sheet_key)
worksheet = sheet_file.get_worksheet(2) # Getting the Google Form Response Sheet
data = worksheet.get_all_records() # Fetching all records from the sheet

sub_units = {}

for item in data:
    if item['sub_unit'] in sub_units:
        sub_units[item['sub_unit']].append({
            'title': item['title'],
            'description': item['description'],
            'resource_link': item['resource_link'],
            'youtube': item['youtube'],
            'tb_pages': item['tb_pages']
        })
    else:
        sub_units[item['sub_unit']] = [{
            'title': item['title'],
            'description': item['description'],
            'resource_link': item['resource_link'],
            'youtube': item['youtube'],
            'tb_pages': item['tb_pages']
        }]
# end of data processing

st.page_link("pages/home.py", label="Back to Homepage", icon=":material/home_app_logo:", width="stretch")
st.title("Unit 2 - Probability")

# st.write(data)
counter = 0
st.subheader("Sub Units:")
for sub_unit, items in sub_units.items():
    #with st.container(border=True, key=f"sub_unit_{counter}"):
    with st.expander(f"{sub_unit.split('_')[1]}"):
        #st.subheader(f"{sub_unit.split('_')[1]}")
        for i, lesson_data in enumerate(items):
            with st.container(key=f"sub_unit_{counter}_container_{i}"):
                if 'Review' in lesson_data['title']:
                    st.write(f"**{lesson_data['title']} Class**")
                elif 'Quiz' not in lesson_data['title'] and 'Test' not in lesson_data['title'] and 'Assignment' not in lesson_data['title']:
                    st.write(f"**Lesson: {lesson_data['title']}**")
                    col1, col2, col3, col4 = st.columns(4)
                    with col1:
                        st.write(f"_{lesson_data['description']}_")
                    with col2:
                        if len(lesson_data['resource_link']) > 2:
                            st.write(f"[Resource Link]({lesson_data['resource_link']})")
                        else:
                            st.write("_No Resource Link_")
                    with col3:
                        if len(lesson_data['youtube']) > 2:
                            st.write(f"[YouTube Playlist]({lesson_data['youtube']})")
                        else:
                            st.write("_No YouTube Playlist_")
                    with col4:
                        st.write(f"**TB:** {lesson_data['tb_pages']}")
                else:
                    st.badge(f"**{lesson_data['title']}:** _{lesson_data['description']}_", icon=":material/check:", color="green")
                st.divider()
        # end of inner for
    # end of sub_unit container
    counter += 1
# end of outer for