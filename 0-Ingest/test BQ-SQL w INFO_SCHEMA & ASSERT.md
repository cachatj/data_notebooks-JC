# using INFORMATION_SCHEMA.views & ASSERT to test BigQuery SQL Statements


https://cloud.google.com/bigquery/docs/information-schema-views


https://medium.com/google-cloud/validating-successful-execution-of-bigquery-scripts-using-assert-c82f7ff9cfa8



You can make a smaller randomly sampled version of your table:

CREATE TABLE `project.testdataset.tablename`

AS SELECT * FROM `project.proddataset.tablename` WHERE RAND() > 0.9

to get 10% of the rows. Or 0.01 to get 1%. Run it more than once and you'll get different rows of course, since RAND() is random. Hash a timestamp to get repeatable results.

Then all you're changing is the dataset name between test and prod.


https://ianwhitestone.work/testing-sql/

https://pypi.org/project/bq-test-kit/

