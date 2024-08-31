## pandas EDA snippets & scratchpad - JC's Data Wrangling / Data Prep / Transformation ##
==========================================================================================
#ongoing list code & approaches related to INGEST - CLEAN - VALIDATE Exploratory Data Analysis 

Libraries to Check out Next:
> dataprep.AI (EDA, Clean & Connect)
> great_expectations (Validation)
> PipeRider (profiling reports & validation checks) - https://docs.piperider.io/
> ODDP (Open Data Discovery platform - data/ML Feature Store & quality validation) - https://opendatadiscovery.org/
> popmon (time series profiling)
> Optimus (data prep & processing for modeling)


==============================
# dataprep.eda
	plot(df,x,y) #column distributions & stats, can pass 1 or 2 columns to plot()

	plot_correlation(df,x,y) #correlations plots btw columns, one or two columns

	plot_missing(df,x,y) #analyze missing values in dataset

	plot_diff() #differences of column distributions and statistics across multiple datasets
		from dataprep.eda import plot_diff
		df1 = load_dataset("house_prices_test")
		df2 = load_dataset("house_prices_train")
		plot_diff([df1, df2])



==============================
# De-duplicate
df.drop_duplicates()

=============================
# Drop missing values/incomplete rows
df.dropna()

==============================
# Replace Missing Values - df.fillna()
	#Fill with the average
	fill_value = df.price.mean()
	df.fillna(value=fill_value)

	#Fill with the previous value in that column
	df.fillna(method='pad')

	#Fill the data using the average
	df = df.fillna(value=df.price.mean())

=============================
# Encode Ordinal Category (String) Labels w Numerical ID
	from sklearn.preprocessing import LabelEncoder
	rating_encoder = LabelEncoder()
	df.rating = rating_encoder.fit_transform(df.rating)
	df

	#Convert back to Text Categories 
	rating_encoder.inverse_transform(df.rating)

	#Encode Odrinal Labels w custom mapping
	ordinal_map = {
	    rating: index
	    for index, rating in enumerate(['low', 'medium', 'high'])
	}
	print(ordinal_map)
	df.rating = df.rating.map(ordinal_map)
	df

	#One-hot-encode Product features (take column of Product Colors, expand across columns with TRUE=1/FALSE=0 values in row.
	df = pd.get_dummies(df)
	df


=============================
# start and end date for data grab
end = datetime.now()
end = datetime.now()
start = datetime(end.year-4,end.month,end.day)

===========
# loop for grabing finance data
for stock in tech_list:
    globals()[stock] = data.DataReader(stock,'yahoo',start,end)
    # taking string of stock ticker into global variable,and create a data frame

===========
# Calculate the moving average of the stock
ma_day = [30,60,180]

for ma in ma_day:
    column_name = "MA for %s days"%(str(ma))

    data[column_name] = data['Open'].rolling(window=ma).mean()


==============================
# Calling histogram of daily return
#data['column'].hist(bins=#)
data['Open'].hist(bins=50)
plt.show()

================================
# Quantile Method
#data['column'].quantile(%.%%)
rets['GOOG'].quantile(0.05)


===========
# pandas Profiling in Command Line 
! pandas_profiling --title "Example Profiling Report" --config_file default.yaml data.csv report.html



