import pandas as pd
import tkinter as tk
from tkinter import filedialog

# Step 1: Open file picker
root = tk.Tk()
root.withdraw()  # Hide the main window

file_path = filedialog.askopenfilename(
    title="Select a CSV file",
    filetypes=[("CSV files", "*.csv")]
)

if not file_path:
    print("No file selected.")
    exit()

# Step 2: Load CSV into DataFrame
df = pd.read_csv(file_path)
print("Original Data:")
print(df.head())

# Step 3: Remove unwanted columns
columns_to_drop = ['column_to_remove_1', 'column_to_remove_2']  # change these
df = df.drop(columns=columns_to_drop, errors='ignore')

# Step 4: Data Quality Checks
print("\n--- Data Quality Checks ---")

# Check for nulls
null_counts = df.isnull().sum()
print("\nNull values per column:")
print(null_counts)

# Remove rows with nulls (optional)
df = df.dropna()

# Check data types
print("\nData types:")
print(df.dtypes)

# Remove duplicates
df = df.drop_duplicates()

# Step 5: Filter for non-negative values in a specific column
column_to_filter = 'your_numeric_column'  # change this
df_filtered = df[df[column_to_filter] >= 0]

print("\nFiltered Data:")
print(df_filtered.head())

# Step 6: Export to Excel
output_path = filedialog.asksaveasfilename(
    defaultextension=".xlsx",
    filetypes=[("Excel files", "*.xlsx")],
    title="Save the cleaned file"
)

if output_path:
    df_filtered.to_excel(output_path, index=False)
    print(f"\nFile saved to: {output_path}")
else:
    print("Save operation canceled.")
