# Personal-Finance-Manager
The Personal Finance Manager is a Python-based project that helps users track their income, expenses, and budget goals.
## Project Overview
The Personal Finance Manager is an intuitive and lightweight Python application tailored to assist users in managing their personal finances. By leveraging SQLite, a serverless and self-contained database engine, the application ensures ease of use and portability. This project provides essential financial management features through a user-friendly command-line interface (CLI).

## Key Features
### Transaction Management:
* Users can log income and expenses with details such as date, category, description, and amount.
* Transactions are stored in an SQLite database, ensuring reliable and persistent storage without the need for complex configuration.

### Budget Tracking:
* Users can set budget goals for various categories (e.g., Groceries, Entertainment).
* The system tracks spending against these budgets and provides feedback on budget adherence.

### Financial Reporting:
* Generate detailed reports summarizing total income, total expenses, and category-wise spending.
* Reports help users understand their financial habits and make informed decisions.

### Data Visualization:
* Visualize spending patterns with bar charts using matplotlib.
* Visual aids make it easier to identify trends and areas for improvement.

## Implementation Details
### Database Setup:
* The project uses SQLite to manage financial data.
* The database includes two main tables: transactions and budgets.
* The transactions table stores individual financial transactions, while the budgets table stores budget goals for different categories.

### Command-Line Interface:
* A user-friendly CLI allows users to perform various operations such as adding transactions, setting budgets, generating reports, and visualizing data.
* The CLI provides an interactive and straightforward way to manage personal finances.

### Data Operations:
* Functions are provided to add transactions and budgets to the SQLite database.
* Data retrieval functions fetch transactions and budgets for reporting and visualization.

### Reporting and Visualization:
* Reports summarize financial data and provide insights into spending habits.
* Visualization with matplotlib helps users see their spending patterns clearly.

## Usage Instructions
### Setup:
* Ensure Python is installed on your system.
* The script does not require any additional database setup beyond Python's standard library (sqlite3 module).

### Running the Script:
* Run the script from the command line.
* Use the CLI to add transactions, set budgets, generate reports, and visualize spending.

### Example Commands:
* Add a transaction: Enter the date, category, description, and amount.
* Add a budget: Enter the category and budget amount.
* Generate a report: View total income, total expenses, and category-wise spending.
* Visualize spending: See a bar chart of spending by category.
