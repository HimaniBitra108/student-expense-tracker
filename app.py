import streamlit as st
from src.expense_utils import (
    load_expenses,
    get_total_expenses,
    get_category_summary,
    get_highest_category
)

# Page settings
st.set_page_config(
    page_title="Student Expense Tracker",
    page_icon="💰",
    layout="wide"
)

# Title
st.title("💰 Student Expense Tracker")
st.write("Track your expenses and understand where your money is going.")

# Load data
expenses = load_expenses()

# Calculate insights
total = get_total_expenses(expenses)
category_summary = get_category_summary(expenses)
highest_category = get_highest_category(expenses)

# Summary cards
col1, col2 = st.columns(2)

with col1:
    st.metric("Total Spending", f"₹{total:,.0f}")

with col2:
    st.metric("Highest Spending Category", highest_category)

# Category summary
st.subheader("📊 Spending by Category")
st.bar_chart(category_summary)

# Expense table
st.subheader("🧾 All Expenses")
st.dataframe(expenses, use_container_width=True)