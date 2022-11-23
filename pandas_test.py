import pandas as pd
letter = 'A'
df_nasdaq = pd.read_csv('nasdaq_tickers.csv').dropna(axis=0)
tickers = [tick for tick in df_nasdaq['Symbol'].to_list() if tick[0] == letter]

print(tickers)