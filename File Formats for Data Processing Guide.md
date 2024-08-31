# File Formats for Local Data Processing

## Performance Metrics
Writing Data - Feather, Parquet & HDF5 fastest write time
File Size - Parquet is smallest uncompressed file, Parquet & HDF5 are smallest compressed
Reading Time - Pickle & HDF5 have fastest reading times

Pickle and Feather are intended for short-term storage. 
    Pickle is intended for saving Python objects between work sessions and therefore is only supported by Python. 
    Feather is intended for exchanging data between Python and R. 
---
## Optimize Dataframes
1. change categorical feature as "category" vs "string" (drop 10s of MB)
    `data["team"] = data["team"].astype("category")`
    `data .info`
2. optimize numerical attributes with smaller datatype. uint8 &  float32 store far less significant digits (drop 100s of MB)
    `data["age"] = data["age"].astype("uint8")`
    `data["win_prob"] = data["win_prob"].astype("float32")`
3. store binary attributes as boolean 
4. provide schema (column name & datatype) during input
    `sample = pd.read_csv("XYZ.csv",usecols=["team","age","won_before","win_prob"])`
    or
    `dtypes = {
    "id1": "object",
    "id2": "object",
    "id3": "object",
    "id4": "object",
    "id5": "object",
    "id6": "object",
    "v1": "object",
    "v2": "object",
    "v3": "object",
    }
    data = pd.read_csv("path/file.csv", dtype=dtypes)`


## CSV
    # Reading
    df = pd.read_csv(file_name, 
                    dtype = {...})
    # Writing
    df.to_csv(file_name, 
            index = False,
            compression = ...) # None or "gzip" 
---
## Pickle 
data.pkl
binary serializing
    
    # Reading
    df = pd.read_pickle(file_name)
    # Writing
    df.to_pickle(file_name, 
                compression = ...) # None or "gzip"
---
## Parquet
data.parquet
columnar storage, use pyarrrow engine

    # Reading
    df = pd.read_parquet(file_name)
    # Writing
    df.to_parquet(file_name, 
                engine = "pyarrow", 
                compression = ...) # None or "gzip"
---
## Feather 
data.feather 
Arrow tables or dataframes (from Python or R)

    # Reading
    df = pd.read_feather(file_name)
    # Writing
    df.to_feather(file_name, 
                compression = ...) # None or "zstd"
---
## Hierarchical Data Format (HDF5)
data.h5
unlimited datatypes, efficient I/O
    
two format options
    "fixed" - write fast
    "table" - slower, but supports searching and subsetting 

to use, install `tables` or `pytables` package
    `conda install -c conda-forge pytables`





---
### sources
- [How to Handle Large Datasets in Python
A Comparison of CSV, Pickle, Parquet, Feather, and HDF5](https://towardsdatascience.com/how-to-handle-large-datasets-in-python-1f077a7e7ecf)

- [PyTables Install Guide](https://www.pytables.org/usersguide/installation.html)
