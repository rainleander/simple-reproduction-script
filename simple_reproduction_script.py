# import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# load the data
data = pd.read_csv('data.csv')

# process the data
grouped_data = data.groupby('category').mean()

# visualize the results
grouped_data.plot.bar()
plt.title('Mean Values per Category')
plt.xlabel('Category')
plt.ylabel('Mean Value')
plt.savefig('results.png')
