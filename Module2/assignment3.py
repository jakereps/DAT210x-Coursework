import pandas as pd

# Load up the dataset
# Ensuring you set the appropriate header column names
#
# .. your code here ..
df = pd.read_csv('./Datasets/servo.data', header=None,
                 names=['motor', 'screw', 'pgain', 'vgain', 'class'])


# Create a slice that contains all entries
# having a vgain equal to 5. Then print the
# length of (# of samples in) that slice:
#
# .. your code here ..
vgain_5 = df[df.vgain == 5]
print('Number of samples with a vgain of 5: %s' % len(vgain_5))


# Create a slice that contains all entries
# having a motor equal to E and screw equal
# to E. Then print the length of (# of
# samples in) that slice:
#
# .. your code here ..
eq_E = df[(df.motor == 'E') & (df.screw == 'E')]
print('Number of samples with both a motor and screw of "E": %s' % len(eq_E))


# Create a slice that contains all entries
# having a pgain equal to 4. Use one of the
# various methods of finding the mean vgain
# value for the samples in that slice. Once
# you've found it, print it:
#
# .. your code here ..
mean_vgain = df[df.pgain == 4].vgain.mean()
print('Mean vgain of all samples with a pgain of 4: %s' % mean_vgain)


# (Bonus) See what happens when you run
# the .dtypes method on your dataframe!
print('DataFrame dtypes: \n', df.dtypes)
