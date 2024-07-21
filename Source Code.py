import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

def create_tables():
    conn = sqlite3.connect('finance_manager.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY,
        date TEXT,
        category TEXT,
        description TEXT,
        amount REAL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS budgets (
        id INTEGER PRIMARY KEY,
        category TEXT,
        amount REAL
    )
    ''')

    conn.commit()
    conn.close()

def add_transaction(date, category, description, amount):
    conn = sqlite3.connect('finance_manager.db')
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO transactions (date, category, description, amount)
    VALUES (?, ?, ?, ?)
    ''', (date, category, description, amount))
    conn.commit()
    conn.close()

def add_budget(category, amount):
    conn = sqlite3.connect('finance_manager.db')
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO budgets (category, amount)
    VALUES (?, ?)
    ''', (category, amount))
    conn.commit()
    conn.close()

def get_transactions():
    conn = sqlite3.connect('finance_manager.db')
    df = pd.read_sql_query('SELECT * FROM transactions', conn)
    conn.close()
    return df

def get_budgets():
    conn = sqlite3.connect('finance_manager.db')
    df = pd.read_sql_query('SELECT * FROM budgets', conn)
    conn.close()
    return df

def generate_report():
    transactions = get_transactions()
    budgets = get_budgets()

    total_income = transactions[transactions['amount'] > 0]['amount'].sum()
    total_expense = transactions[transactions['amount'] < 0]['amount'].sum()

    category_expense = transactions.groupby('category')['amount'].sum()

    print("Total Income:", total_income)
    print("Total Expense:", total_expense)
    print("Category-wise Spending:\n", category_expense)

    for _, budget in budgets.iterrows():
        category = budget['category']
        budget_amount = budget['amount']
        actual_spending = category_expense.get(category, 0)
        print(f"Budget for {category}: {budget_amount}, Actual Spending: {actual_spending}")

def visualize_spending():
    transactions = get_transactions()
    category_expense = transactions.groupby('category')['amount'].sum()

    category_expense.plot(kind='bar')
    plt.title('Category-wise Spending')
    plt.xlabel('Category')
    plt.ylabel('Amount')
    plt.show()

# Initialize the database and tables
create_tables()

# Example usage
add_transaction('2024-07-20', 'Groceries', 'Supermarket shopping', -50.75)
add_transaction('2024-07-21', 'Salary', 'Monthly paycheck', 1500.00)
add_budget('Groceries', 300)

# Generate report and visualize spending
generate_report()
visualize_spending()
