import pandas as pd
import numpy as np

header_names = ['education', 'age', 'capital-gain', 'race', 'capital-loss',
                'hours-per-week', 'sex', 'classification']


# Load up the dataset, setting correct header labels
# Use basic pandas commands to look through the dataset...
# get a feel for it before proceeding!
# Find out what value the dataset creators used to
# represent "nan" and ensure it's properly encoded as np.nan
#
# .. your code here ..
df = pd.read_csv('./Datasets/census.data', header=None, names=header_names,
                 usecols=list(np.arange(len(header_names)) + 1), na_values=0)


# Figure out which features should be continuous + numeric
# Conert these to the appropriate data type as needed,
# that is, float64 or int64
#
# .. your code here ..
df = df.apply(lambda x: pd.to_numeric(x, errors='ignore'))


# Look through your data and identify any potential categorical
# features. Ensure you properly encode any ordinal types using
# the method discussed in the chapter.
#
# .. your code here ..
df.education = df.education.astype('category').cat.codes


# Look through your data and identify any potential categorical
# features. Ensure you properly encode any nominal types by
# exploding them out to new, separate, boolean fatures.
#
# .. your code here ..
df = pd.get_dummies(df, columns=['race', 'sex', 'classification'])


# Print out your dataframe
print(df)
