import pandas as pd
# from pathlib import Path
from tkinter import Tk, filedialog
import matplotlib.pyplot as plt


# Hide the main tkinter window
Tk().withdraw()

# Open file picker
file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])

# Read CSV
df = pd.read_csv(file_path)

# print(df.columns) # show the column names in the dataframe
# print(list(df.columns)) # creates a list of the columns in the dataframe
# df.info() # get full structure of the dataframe, including data types and non-null counts



# select the columns from the dataframe to plot after looking at the info
x = df['Description']
y = df['Amount']

# create a scatter plot of the selected columns
plt.scatter(x,y)
plt.xlabel("Description")
plt.ylabel("Amount")
plt.title("Scatter Plot of columnA vs columnB")

plt.show()
