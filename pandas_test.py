import pandas as pd

s1 = pd.Series([1, 2], index=['Sun', 'Mon'])
s2 = pd.Series([3], index=['Tue'])

print(s1)
print(s2)
s3 = s1.append(s2)
print(s3)
