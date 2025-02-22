import streamlit as st
# import pandas as pd
import datetime
# from io import BytesIO
# from fpdf import FPDF2 as FPDF

# Title
st.title("🌱 Mind Growth App")

# Session state to store data
if "thoughts" not in st.session_state:
    st.session_state.thoughts = []
if "mistakes" not in st.session_state:
    st.session_state.mistakes = []
if "quotes" not in st.session_state:
    st.session_state.quotes = []

# 1️⃣ Thought Journal
st.subheader("📝 Save Your Thoughts")
thought = st.text_area("Write your daily thoughts here:")
if st.button("Save Thought"):
    st.session_state.thoughts.append({"date": datetime.date.today(), "thought": thought})
    st.success("Saved successfully!")

# Show past thoughts
if st.session_state.thoughts:
    st.subheader("📜 Your Past Thoughts")
    for entry in st.session_state.thoughts:
        st.write(f"**{entry['date']}:** {entry['thought']}")

# 2️⃣ Mistake Recognition
st.subheader("⚡ Recognize & Learn from Mistakes")
mistake = st.text_area("What mistake did you make?")
lesson = st.text_area("What did you learn from it?")
if st.button("Save Mistake"):
    st.session_state.mistakes.append({"date": datetime.date.today(), "mistake": mistake, "lesson": lesson})
    st.success("Mistake recorded!")

# Show past mistakes
if st.session_state.mistakes:
    st.subheader("🔍 Past Mistakes & Lessons")
    for entry in st.session_state.mistakes:
        st.write(f"**{entry['date']}:** {entry['mistake']} → {entry['lesson']}")

# 3️⃣ Motivational Quotes
st.subheader("🌟 Save Your Favorite Quotes")
quote = st.text_input("Enter a motivational quote:")
if st.button("Save Quote"):
    st.session_state.quotes.append(quote)
    st.success("Quote saved!")

# Show saved quotes
if st.session_state.quotes:
    st.subheader("📖 Your Favorite Quotes")
    for q in st.session_state.quotes:
        st.write(f"🌱 {q}")

# 4️⃣ Generate PDF Report
st.subheader("📥 Download Your Mind Growth Report")

# def generate_pdf():
#     pdf = FPDF()
#     pdf.set_auto_page_break(auto=True, margin=15)
#     pdf.add_page()
#     pdf.set_font("Arial", style='B', size=16)
#     pdf.cell(200, 10, "Mind Growth Report", ln=True, align="C")
    
#     # Thoughts
#     pdf.set_font("Arial", size=12)
#     pdf.cell(200, 10, "Your Thoughts:", ln=True)
#     for entry in st.session_state.thoughts:
#         pdf.multi_cell(0, 10, f"{entry['date']}: {entry['thought']}")
    
#     # Mistakes & Lessons
#     pdf.cell(200, 10, "Mistakes & Lessons:", ln=True)
#     for entry in st.session_state.mistakes:
#         pdf.multi_cell(0, 10, f"{entry['date']}: {entry['mistake']} → {entry['lesson']}")
    
#     # Quotes
#     pdf.cell(200, 10, "Favorite Quotes:", ln=True)
#     for q in st.session_state.quotes:
#         pdf.multi_cell(0, 10, f"🌱 {q}")
    
#     # Save to buffer
#     buffer = BytesIO()
#     pdf_bytes = pdf.output(dest='S').encode('latin-1')  # Convert to bytes
#     buffer.write(pdf_bytes)
#     buffer.seek(0)
#     return buffer.getvalue()

# if st.button("Download PDF Report"):
#     pdf_data = generate_pdf()
#     st.download_button("📩 Click to Download", data=pdf_data, file_name="Mind_Growth_Report.pdf", mime="application/pdf")

st.success("🚀 Keep growing and improving!")


