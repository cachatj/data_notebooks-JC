## CSV to pandas Series

	btc = pd.read_csv('/content/drive/MyDrive/btc.csv', index_col='Date', parse_dates=True)

	btc.head()

	btc.index