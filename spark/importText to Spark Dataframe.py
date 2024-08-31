# spark is from the previous example
sc = spark.sparkContext

# A CSV dataset is pointed to by path.
# The path can be either a single CSV file or a directory of CSV files
path = "examples/src/main/resources/people.csv"

df = spark.read.csv(path)
df.show()
# +------------------+
# |               _c0|
# +------------------+
# |      name;age;job|
# |Jorge;30;Developer|
# |  Bob;32;Developer|
# +------------------+

# Read a csv with delimiter, the default delimiter is ","
df2 = spark.read.option(delimiter=';').csv(path)
df2.show()
# +-----+---+---------+
# |  _c0|_c1|      _c2|
# +-----+---+---------+
# | name|age|      job|
# |Jorge| 30|Developer|
# |  Bob| 32|Developer|
# +-----+---+---------+

# Read a csv with delimiter and a header
df3 = spark.read.option("delimiter", ";").option("header", True).csv(path)
df3.show()
# +-----+---+---------+
# | name|age|      job|
# +-----+---+---------+
# |Jorge| 30|Developer|
# |  Bob| 32|Developer|
# +-----+---+---------+

# You can also use options() to use multiple options
df4 = spark.read.options(delimiter=";", header=True).csv(path)

# "output" is a folder which contains multiple csv files and a _SUCCESS file.
df3.write.csv("output")

# Read all files in a folder, please make sure only CSV files should present in the folder.
folderPath = "examples/src/main/resources"
df5 = spark.read.csv(folderPath)
df5.show()
# Wrong schema because non-CSV files are read
# +-----------+
# |        _c0|
# +-----------+
# |238val_238|
# |  86val_86|
# |311val_311|
# |  27val_27|
# |165val_165|
# +-----------+