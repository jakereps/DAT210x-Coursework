import pandas as pd

# Load up the 'tutorial.csv' dataset
#
# .. your code here ..
csv = pd.read_csv('./Datasets/tutorial.csv')


# Print the results of the .describe() method
#
# .. your code here ..
print('Describe tutorial.csv: \n', csv.describe())


# Figure out which indexing method you need to
# use in order to index your dataframe with: [2:4,'col3']
# And print the results
#
# .. your code here ..
print('Column 3 of rows 2 and 3: \n', csv.loc[2:4, 'col3'])
