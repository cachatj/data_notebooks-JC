# pandas Data Wrangling / Data Prep / Transformation - jc's global notes



## De-duplicate
	df.drop_duplicates()

## Drop missing values/incomplete rows
	df.dropna()

## Replace Missing Values - df.fillna()
	#Fill with the average
	fill_value = df.price.mean()
	df.fillna(value=fill_value)

	#Fill with the previous value in that column
	df.fillna(method='pad')

	#Fill the data using the average
	df = df.fillna(value=df.price.mean())


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


	