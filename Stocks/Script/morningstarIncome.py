import pandas as pd
import matplotlib.pyplot as plt
pd.set_option('display.float_format', lambda x: '%.3f' % x)

stock = "SATS Ltd. (S58.SI)"

# Read data from Morningstar and set metrics as index
income = pd.read_excel("../" + "SATS Ltd. (S58.SI)/" + "Income Statement_Annual_As Originally Reported.xls",  index_col=0)

# Remove whitespaces
income.index = income.index.str.strip()
# Transpose df to make metrics as columns
income = income.T
# Remove commas and convert str to float for all cols
income[income.keys()] = income[income.keys()].replace({',': ''}, regex=True).astype(float)/1000000
# Reorder the rows to be ascending downwards
income = income.sort_index()

# Revenue and profits
print(income['Total Revenue'])
print(income['Gross Profit'])
print(income['Pretax Income'])
income[['Total Revenue', 'Gross Profit', 'Pretax Income']].plot.bar()
plt.ylabel("In SGD Million")
plt.show()


