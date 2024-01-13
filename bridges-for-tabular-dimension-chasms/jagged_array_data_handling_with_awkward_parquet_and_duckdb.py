#!/usr/bin/env python
# coding: utf-8

# In[1]:


# create some demonstrational tabular data in a python dictionary
import json

example_tabular = {
            "name": ["Alice", "Bob"],
            "age": [30, 25],
            "occupation": ["Software Engineer", "Data Scientist"],
        }
print(json.dumps(example_tabular, indent=4))


# In[2]:


# demonstrate the data as a pandas dataframe
import pandas as pd

example_pd_dataframe = pd.DataFrame(example_tabular)

example_pd_dataframe


# In[3]:


# demonstrate the data as a pyarrow table
import pyarrow as pa

example_pa_table = pa.Table.from_pydict(example_tabular)

example_pa_table


# In[4]:


# show how the schema is a distinct component of a pyarrow table
example_pa_table.schema


# In[5]:


# show how schema metadata can be changed
example_pa_table = example_pa_table.replace_schema_metadata({"data-producer":"a-lab", "data-version":"v0.0.1"})
example_pa_table.schema


# In[6]:


# show how the data may be written to a parquet file
import pathlib
from pyarrow import parquet

parquet.write_table(table=example_pa_table, where="example.parquet")

print(pathlib.Path("./example.parquet").resolve())


# In[7]:


# show how the schema may be read from a parquet file (with everything intact)

parquet.read_schema(where="example.parquet")


# In[8]:


# show how partial data may be read from a parquet file

parquet.read_table(source="example.parquet", columns=["name"])


# In[9]:


# show how the full data may be read from a parquet file

parquet.read_table(source="example.parquet")


# In[10]:


# show how row-wise portions of pyarrow tables can be selected and written
pathlib.Path("./example_dataset").mkdir(exist_ok=True)

parquet.write_table(table=example_pa_table.take([0]), where="./example_dataset/example-0.parquet")
parquet.write_table(table=example_pa_table.take([1]), where="./example_dataset/example-1.parquet")

parquet.read_table(source="./example_dataset/example-0.parquet")


# In[11]:


# show how a parquet dataset can be read (composing of one or many files)

example_dataset = parquet.read_table(source="./example_dataset/")

print(example_dataset.schema, end="\n\n")
print(example_dataset)
# why is this list of lists?


# In[12]:


# what if we have inequal nodes?
nodes = {
    "nodes": [
        {
            "name": "Alice",
            "age": 30,
            "occupation": "Software Engineer",
        },
        {
            "name": "Bob",
            "age": 25,
            "occupation": "Data Scientist",
            "favorite_color": "pink",
        },
    ],
}

nodes_df = pd.DataFrame(nodes)
nodes_df


# In[13]:


# how can we access the age data of each node?
nodes_df.nodes.apply(lambda x: x["age"])


# In[14]:


# what if the attributes are misaligned (some have them, some don't)?
try:
  nodes_df.nodes.apply(lambda x: x["favorite_color"])
except Exception as e:
  import traceback
  traceback.print_exc()


# In[15]:


get_ipython().system('pip install awkward')


# In[16]:


# show how awkard arrays can be used to understand the data differently
import awkward as ak

nodes_as_array = ak.Array(nodes)
nodes_as_array


# In[17]:


# show how fields may be accessed
nodes_as_array.fields


# In[18]:


# show how fields may be accessed (nested)
nodes_as_array.nodes.fields


# In[19]:


# show how masking works (filter for only nodes with occupation of "Data Scientist")
nodes_as_array.mask[nodes_as_array.nodes.favorite_color == "pink"]


# In[20]:


# show how data may be exported and imported from a parquet file
ak.to_parquet(nodes_as_array, "awkward_example.parquet")
ak.from_parquet("awkward_example.parquet")


# In[21]:


# show how we can abstract jagged data queries into DuckDB SQL
import duckdb

with duckdb.connect() as ddb:
  result = ddb.execute("""
      SELECT
        nodes.name,
        nodes.favorite_color
      FROM read_parquet('awkward_example.parquet')
      WHERE nodes.favorite_color NOT NULL
    """).arrow()

result

