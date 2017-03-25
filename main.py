import pandas as pd

a = 0
df = pd.read_csv('newResultCsv.csv')
for i in df.Gene_symbol:
	if pd.isnull(i):
		a = a + 1

print "the number of missing entries", a

df = df[pd.notnull(df['Gene_symbol'])]
df.drop_duplicates(subset=['Gene_symbol'], keep='last')
df.to_csv('filter.csv')