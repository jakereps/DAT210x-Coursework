import pandas as pd


# Load up the table, and extract the dataset
# out of it. If you're having issues with this, look
# carefully at the sample code provided in the reading
#
# .. your code here ..
df = pd.read_html(
    'http://espn.go.com/nhl/statistics/player/_/'
    'stat/points/sort/points/year/2015/seasontype/2', skiprows=2)[0]


# Rename the columns so that they match the
# column definitions provided to you on the website
#
# .. your code here ..
df.columns = ['RK', 'PLAYER', 'TEAM', 'GP', 'G', 'A', 'PTS', '+/-', 'PIM',
              'PTS/G', 'SOG', 'PCT', 'GWG', 'PP.G', 'PP.A', 'SH.G', 'SH.A']


# Get rid of any row that has at least 4 NANs in it
#
# .. your code here ..
df = df.dropna(axis=0, thresh=13)


# At this point, look through your dataset by printing
# it. There probably still are some erroneous rows in there.
# What indexing command(s) can you use to select all rows
# EXCEPT those rows?
#
# .. your code here ..
df = df[df.PLAYER != 'PLAYER']


# Get rid of the 'RK' column
#
# .. your code here ..
df = df.drop(labels=['RK'], axis=1)


# Ensure there are no holes in your index by resetting
# it. By the way, don't store the original index
#
# .. your code here ..
df = df.reset_index(drop=True)


# Check the data type of all columns, and ensure those
# that should be numeric are numeric
df = df.apply(lambda x: pd.to_numeric(x, errors='ignore'))


# Your dataframe is now ready! Use the appropriate
# commands to answer the questions on the course lab page.
print('Number of rows in df: %s' % len(df))
print('Number of unique rows of PCT: %s' % len(set(df.PCT)))
print('The addition of GP[15] and GP[16]: %s' % (df.GP[15] + df.GP[16]))
