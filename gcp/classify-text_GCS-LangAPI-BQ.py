
# Cloud Storage, the Natural Language API, and BigQuery. 
# First, a client is created for each service; then references are created to the BigQuery table. 
# files is a reference to each of the BBC dataset files in the public bucket. 
# We iterate through these files, download the articles as strings,
# and send each one to the Natural Language API in our classify_text function. 
# For all articles where the Natural Language API returns a category, 
# the article and its category data are saved to a rows_for_bq list. 
# When classifying each article is done, the data is inserted into BigQuery using insert_rows().


from google.cloud import storage, language_v1, bigquery
# Set up our GCS, NL, and BigQuery clients
storage_client = storage.Client()
nl_client = language_v1.LanguageServiceClient()
# TODO: replace YOUR_PROJECT with your project id below
bq_client = bigquery.Client(project='qwiklabs-gcp-04-1ed84eb9ab76')
dataset_ref = bq_client.dataset('news_classification_dataset')
dataset = bigquery.Dataset(dataset_ref)
table_ref = dataset.table('article_data') # Update this if you used a different table name
table = bq_client.get_table(table_ref)
# Send article text to the NL API's classifyText method



def classify_text(article):
        response = nl_client.classify_text(
                document=language_v1.types.Document(
                        content=article,
                        type_='PLAIN_TEXT'
                )
        )
        return response
rows_for_bq = []
files = storage_client.bucket('cloud-training-demos-text').list_blobs()
print("Got article files from GCS, sending them to the NL API (this will take ~2 minutes)...")
# Send files to the NL API and save the result to send to BigQuery
for file in files:
        if file.name.endswith('txt'):
                article_text = file.download_as_bytes()
                nl_response = classify_text(article_text)
                if len(nl_response.categories) > 0:
                        rows_for_bq.append((str(article_text), str(nl_response.categories[0].name), nl_response.categories[0].confidence))
print("Writing NL API article data to BigQuery...")
# Write article text + category data to BQ
errors = bq_client.insert_rows(table, rows_for_bq)
assert errors == []



# Count all the categories text was classifed to
# SELECT
#   category,
#   COUNT(*) c
# FROM
#   `news_classification_dataset.article_data`
# GROUP BY
#   category
# ORDER BY
#   c DESC

# Find obscure cateogries
# SELECT * FROM `news_classification_dataset.article_data`
# WHERE category = "/Arts & Entertainment/Music & Audio/Classical Music"

# list articles classification was 90% confident
# SELECT
#   article_text,
#   category
# FROM `news_classification_dataset.article_data`
# WHERE cast(confidence as float64) > 0.9