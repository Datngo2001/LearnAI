import pandas as pa

rs = pa.read_csv('addresses.csv')
#print(rs.info())
#print(rs.head(1))
#print(rs.describe())
print(rs.iloc[0,0])