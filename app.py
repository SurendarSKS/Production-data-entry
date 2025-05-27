import streamlit as st
import pandas as pd
import os

file_name = "data.xlsx"

st.title("AI Industrial Manager - Data Entry")

# Form
with st.form("entry_form"):
    date = st.date_input("Date")
    shift = st.text_input("Shift")
    operator = st.text_input("Operator")
    machine = st.text_input("Machine")
    component = st.text_input("Component")
    quantity = st.number_input("Quantity", min_value=0)
    cost = st.number_input("Cost", min_value=0.0)
    submitted = st.form_submit_button("Submit")

    if submitted:
        row = {
            "Date": date,
            "Shift": shift,
            "Operator": operator,
            "Machine": machine,
            "Component": component,
            "Quantity": quantity,
            "Cost": cost,
        }

        # Save to Excel
        if os.path.exists(file_name):
            df = pd.read_excel(file_name)
            df = pd.concat([df, pd.DataFrame([row])], ignore_index=True)
        else:
            df = pd.DataFrame([row])

        df.to_excel(file_name, index=False)
        st.success("✅ Data saved to Excel!")
