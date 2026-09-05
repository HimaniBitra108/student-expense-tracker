import pandas as pd


def load_expenses():
    """Load expense data from the CSV file."""
    return pd.read_csv("data/expenses.csv")
import pandas as pd


def load_expenses():
    """Load expense data from the CSV file."""
    return pd.read_csv("data/expenses.csv")


def get_total_expenses(expenses):
    """Calculate the total amount spent."""
    return expenses["Amount"].sum()


def get_category_summary(expenses):
    """Calculate total spending for each category."""
    return expenses.groupby("Category")["Amount"].sum()


def get_highest_category(expenses):
    """Find the category with the highest spending."""
    category_summary = get_category_summary(expenses)
    return category_summary.idxmax()