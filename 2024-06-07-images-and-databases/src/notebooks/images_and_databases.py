# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.16.2
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# + [markdown] editable=true slideshow={"slide_type": "slide"}
# <center>
#     
# # Images and Databases
# #### Way Lab - Research in Progress - 2024-06-07
#
# </center>

# + [markdown] editable=true slideshow={"slide_type": "slide"}
# ### Background
#
# ![image.png](attachment:eef20a15-c038-40d2-9ca1-f4549909b59f.png)
#
# - [`mitocheck_data`](https://github.com/WayScience/mitocheck_data) project

# + [markdown] editable=true slideshow={"slide_type": "slide"}
# ### Background
#
# ![image.png](attachment:ab3857d3-8c67-47ef-afde-667863810c54.png)
#
# - [`idr_stream`](https://github.com/WayScience/IDR_stream) project

# + [markdown] editable=true slideshow={"slide_type": "slide"}
# ### Background
#
# ![image.png](attachment:01ff3fcf-93e3-40d3-b154-4d5690761e66.png)
#
# __How could we "package" the `mitocheck_data` data in such a way to enable development iteration and usefulness to others?__

# + [markdown] editable=true slideshow={"slide_type": "slide"}
# ### Background
#
# __"Data Packaging" Story__
#
# _"As a research data participant I need a way to analyze (understand, contextualize, and explore) and implement (engineer solutions which efficiently scale for time and computing resources) the data found here in order to effectively reproduce findings, make new discoveries, and avoid challenging (or perhaps incorrect) translations individually."_

# + [markdown] editable=true slideshow={"slide_type": "slide"}
# ## Data Files
#
# ![image.png](attachment:fc1dcf51-fcdc-4cc9-805e-aefd7e2d7ab5.png)
#
# - text file data ([CSV](https://en.wikipedia.org/wiki/Comma-separated_values)'s, TSV's, etc)
# - ch5 files (microscopy-focused [HDF](https://en.wikipedia.org/wiki/Hierarchical_Data_Format))
# - tiff files ([tagged image file format](https://en.wikipedia.org/wiki/TIFF))

# + [markdown] editable=true slideshow={"slide_type": "slide"}
# ## Implied Data
#
# ![image.png](attachment:a5c003dc-786a-4f33-a90d-f3070eb9bafc.png)
#
# - arrays from images (for in-memory calculations)

# + [markdown] editable=true slideshow={"slide_type": "slide"}
# ## Implied Data
#
# ![image.png](attachment:bd48b6a5-26fa-4bee-980f-ac272594e0bd.png)

# + [markdown] editable=true slideshow={"slide_type": "slide"}
# ## Data package needs
#
# __Okay, so we need something that can store and distribute:__
#
# - text file tables
# - images
# - arrays

# + [markdown] editable=true slideshow={"slide_type": "slide"}
# ## Files and databases
#
# ![image.png](attachment:8b16edf5-c53c-4e0a-824f-8075d2d8dc47.png)
#
# Files and directories follow patterns within databases.

# + [markdown] editable=true slideshow={"slide_type": "slide"}
# ## Images and databases
#
# <br><br>
#
# __Might be thinking: but images aren't tables!__

# + [markdown] editable=true slideshow={"slide_type": "slide"}
# ## Images and databases
#
# ![image.png](attachment:3a42cef8-a6c8-47fc-8369-d628accebeff.png)
#
# - Images as _values_ within a table.
# - The dimensionality is determined by the file.

# + [markdown] editable=true slideshow={"slide_type": "slide"}
# ## Images and databases
#
# ![image.png](attachment:1bfb5208-74c3-4925-b6c6-6e360d7bf03b.png)
#
# - When we talk about images this way we can call them ["BLOB's" or "objects (object storage)"](https://en.wikipedia.org/wiki/Object_storage).

# + [markdown] editable=true slideshow={"slide_type": "slide"}
# ## Data package needs
#
# __Okay, so we need something that can store and distribute:__
#
# - files:
#     - text file tables
#     - images (blobs / objects)
#     - arrays
# - dimensions:
#     - multiple tables
#     - multiple values (and dimensions) within tables

# + [markdown] editable=true slideshow={"slide_type": "slide"}
# ## LanceDB
#
# ![image.png](attachment:83107c9c-6e2f-4d0c-b805-40142e099af7.png)
#
# > LanceDB is an open-source vector database for AI that's designed to store, manage, query and retrieve embeddings on large-scale multi-modal data. The core of LanceDB is written in Rust 🦀 and is built on top of Lance, an open-source columnar data format designed for performant ML workloads and fast random access.
#
# - Source: [https://lancedb.github.io/lancedb/](https://lancedb.github.io/lancedb/)

# + [markdown] editable=true slideshow={"slide_type": "slide"}
# ## LanceDB
#
# ![image.png](attachment:be8575f1-b5c2-46ba-94d6-75b832cb4b65.png)
#
# - Source: [https://lancedb.github.io/lancedb/](https://lancedb.github.io/lancedb/)

# + [markdown] editable=true slideshow={"slide_type": "slide"}
# ## LanceDB
#
# ![image.png](attachment:0d615e48-a45c-483d-9ec2-53beb4af59f3.png)
#
# - LanceDB is purpose-built with embeddings and vector search in mind.
# - Source: [https://lancedb.github.io/lancedb/concepts/vector_search/](https://lancedb.github.io/lancedb/concepts/vector_search/)

# + colab={"base_uri": "https://localhost:8080/"} id="Pe1jKrHZbLOk" outputId="2369acdb-7098-41fe-e84f-06dfa9c9112d" editable=true slideshow={"slide_type": "skip"}
# !uname -a

# + colab={"base_uri": "https://localhost:8080/"} id="SJjPiiqHbmbk" outputId="8633a2e3-c008-44df-ccf1-76d775bd08c6" editable=true slideshow={"slide_type": "skip"}
# !python --version

# + colab={"base_uri": "https://localhost:8080/"} id="tjQu6k1FboUc" outputId="3a184d1b-04a4-470a-df52-af6efa155961" editable=true slideshow={"slide_type": "skip"}
# !pip install scikit-image lancedb pyarrow awkward matplotlib pandas

# + colab={"base_uri": "https://localhost:8080/"} id="lQR9HGU2dHA3" outputId="29e340bb-23f2-4426-f2ef-fb8cfd9ce7b5" editable=true slideshow={"slide_type": "skip"}
# images source:
# mitocheck_data: https://github.com/WayScience/mitocheck_data
# Image Data Resource (IDR): idr0013(screenA)
# !rm -f mitocheck_example_images.zip
# !wget https://github.com/user-attachments/files/15669319/mitocheck_example_images.zip
# !unzip -o mitocheck_example_images.zip

# + colab={"base_uri": "https://localhost:8080/"} id="0fUuND1uh4cw" outputId="ae27a19c-9975-4700-9931-df4efb9d725e" editable=true slideshow={"slide_type": "slide"}
import pathlib

# images from:
# mitocheck_data: https://github.com/WayScience/mitocheck_data
# Image Data Resource (IDR): idr0013(screenA)

# show some images in an image dir
image_dir = "mitocheck_example_images"

# create a list of images using glob on the dir
images = list(pathlib.Path(image_dir).glob("*"))

images

# + id="Ejkq98LneAJi" editable=true slideshow={"slide_type": "slide"}
from IPython.display import display
from PIL import Image

# display the image
display(Image.open(images[0]))

# + id="oRDbC8u6fJVH" editable=true slideshow={"slide_type": "slide"}
from IPython.display import display
from PIL import Image

# display the image
display(Image.open(images[1]))

# + colab={"base_uri": "https://localhost:8080/"} id="ri7BwiROtXby" outputId="e7f41d5e-cb44-439b-84c1-38358898273a" editable=true slideshow={"slide_type": "slide"}
# file size in bytes
print(images[0])
print(images[0].stat().st_size)

# + colab={"base_uri": "https://localhost:8080/"} id="SlP4cMPNsOmk" outputId="5ec4c619-464c-4b7b-a821-03ec7e5bee7c" editable=true slideshow={"slide_type": "slide"}
# show first few bytes as byte string
with open(images[0], "rb") as f:
    print(f.read(10))

# + colab={"base_uri": "https://localhost:8080/"} id="MXnf6LEbusFg" outputId="2aa57f50-62da-4628-ef2a-fa3f11ceff7f" editable=true slideshow={"slide_type": "slide"}
# show some metadata associated with the image
# !tifffile mitocheck_example_images/LT0001_02.LT0001_02_15_43_IC.tif

# + colab={"base_uri": "https://localhost:8080/"} id="yKN4CN-D7M87" outputId="ee8eb7a6-4a2b-40fb-fe87-dc11ff09be02" editable=true slideshow={"slide_type": "slide"}
import skimage

# read the image as an array
array = skimage.io.imread(images[0])
print(array.shape)
print(array)

# + colab={"base_uri": "https://localhost:8080/", "height": 125} id="4pIsHUkgwuVm" outputId="55b39f45-c5ac-4985-824c-faec9f8bebc0" editable=true slideshow={"slide_type": "slide"}
import pandas as pd

# create a pandas dataframe with image paths
df = pd.DataFrame({"path": images})

df

# + colab={"base_uri": "https://localhost:8080/", "height": 125} id="qoy2eXU4w-bl" outputId="601e14fd-bc1b-41ad-b690-735061c94368" editable=true slideshow={"slide_type": "slide"}
# add the filesize bytes as a column to the dataframe
df["filesize_bytes"] = df.apply(lambda row: row["path"].stat().st_size, axis=1)
df


# + colab={"base_uri": "https://localhost:8080/", "height": 125} id="1XjAd6ELxVlc" outputId="a6666e4a-8690-4dd2-a072-99f9649de9a0" editable=true slideshow={"slide_type": "slide"}
def read_image_bytes(image_path):
    with open(image_path, "rb") as f:
        return f.read()


# read the image as a bytearray object and store in dataframe
df["image_bytes"] = df.apply(lambda row: read_image_bytes(row["path"]), axis=1)
df

# + colab={"base_uri": "https://localhost:8080/", "height": 125} id="hObhfgMzzMjr" outputId="a22b903a-4977-48a7-e8e8-390cebfe72c9" editable=true slideshow={"slide_type": "slide"}
from io import BytesIO

import skimage

# read the bytearray from the dataframe as an array in new column
df["image_array"] = df.apply(
    lambda row: skimage.io.imread(BytesIO(row["image_bytes"])), axis=1
)
df

# + id="YelaLzO-1Nvl" editable=true slideshow={"slide_type": "skip"}
import base64

import pandas as pd
import skimage
from IPython.display import HTML
from PIL import Image


def ImageDataFrame(df: pd.DataFrame):
    def tiff_to_png_bytes(tiff_bytes):
        # Read the TIFF image from the byte array
        tiff_image = skimage.io.imread(BytesIO(tiff_bytes))

        # Convert the image array to a PIL Image
        pil_image = Image.fromarray(tiff_image)

        # Save the PIL Image as PNG to a BytesIO object
        png_bytes_io = BytesIO()
        pil_image.save(png_bytes_io, format="PNG")

        # Get the PNG byte data
        png_bytes = png_bytes_io.getvalue()

        return png_bytes

    def path_to_image_html(bytes_arr):
        return f'<img src="data:image/png;base64,{base64.b64encode(tiff_to_png_bytes(bytes_arr)).decode("utf-8")}" style="width:300px;"/>'

    pd.set_option("display.max_colwidth", 20)

    display(
        HTML(df.to_html(escape=False, formatters={"image_bytes": path_to_image_html}))
    )


# + editable=true slideshow={"slide_type": "slide"}
# show images within the dataframe output
ImageDataFrame(df[["path", "filesize_bytes", "image_bytes"]])

# + colab={"base_uri": "https://localhost:8080/", "height": 217} id="o3-uODnfDF3d" outputId="9908f245-a1bf-4a3d-bc6d-a1c953ff8bd3" editable=true slideshow={"slide_type": "slide"}
# try to write to parquet
df.to_parquet("mitocheck_example_images.parquet")

# + id="aIwFlwx-loQB" editable=true slideshow={"slide_type": "slide"}
# show columns and types
df.info()

# + id="-k2RSbt1DTFB" editable=true slideshow={"slide_type": "slide"}
# show the type of a single path value
type(df["path"].iloc[0])

# + id="9hYVZDhWAhvw" editable=true slideshow={"slide_type": "slide"}
import pyarrow as pa

# update the paths to be strings, then try conversion again
df["path"] = df.apply(lambda row: str(row["path"]), axis=1)
pa.Table.from_pandas(df)

# + id="ySbEhL_Y_b5j" editable=true slideshow={"slide_type": "slide"}
# show the type of a single image_array value
type(df["image_array"].iloc[0])

# + id="1y0OrCvvCjog" editable=true slideshow={"slide_type": "slide"}
import awkward as ak

# use awkward array to interpret the nested arrays from dict records
awk_arr = ak.Array(df.to_dict(orient="records"))
awk_arr

# + id="ldlY9cZSAup7" editable=true slideshow={"slide_type": "slide"}
from pyarrow import parquet

# write a parquet table from the awkward array
parquet.write_table(
    table=ak.to_arrow_table(awk_arr), where="mitocheck_example_images.parquet"
)
# show that we have a file
pathlib.Path("mitocheck_example_images.parquet").is_file()

# + id="07eaMZUHBAf2" editable=true slideshow={"slide_type": "slide"}
# read the file as a dataframe
df = pd.read_parquet(path="mitocheck_example_images.parquet")
# show that it's the same
ImageDataFrame(df[["path", "filesize_bytes", "image_bytes"]])

# + id="fdslV0LsFAB9" editable=true slideshow={"slide_type": "slide"}
import shutil

import lancedb
from pyarrow import parquet

# remove any earlier work
shutil.rmtree("mitocheck_example_images.lance")

# specify a dir where the lancedb database may go and create lancedb client
lancedb_dir = pathlib.Path("mitocheck_example_images.lance")
ldb = lancedb.connect(lancedb_dir)

# create a lancedb table from the parquet data
ldb.create_table(
    data=parquet.read_table("mitocheck_example_images.parquet"),
    name="mitocheck_example_images",
)

# + id="jEAzMQ47Zuqo" editable=true slideshow={"slide_type": "slide"}
# show the parquet file schema
parquet.read_table("mitocheck_example_images.parquet").schema

# + id="2Ypp9dWpWjMI" editable=true slideshow={"slide_type": "slide"}
import lancedb
from pyarrow import parquet

# specify a dir where the lancedb database may go and create lancedb client
lancedb_dir = pathlib.Path("mitocheck_example_images.lance")
ldb = lancedb.connect(lancedb_dir)

# create the table from pandas via parquet file
ldb.create_table(
    data=pd.read_parquet("mitocheck_example_images.parquet"),
    name="mitocheck_example_images",
    mode="overwrite",
)

# + id="4eatce4Mce0l" editable=true slideshow={"slide_type": "slide"}
# read from lancedb to pandas
ldb.open_table("mitocheck_example_images").to_pandas()

# + id="skVqe5d9dZ5G" editable=true slideshow={"slide_type": "slide"}
# show that the dataframes are equal
pd.testing.assert_frame_equal(
    pd.read_parquet("mitocheck_example_images.parquet"),
    ldb.open_table("mitocheck_example_images").to_pandas(),
)

# + id="z6E2cmw4E6ZV" editable=true slideshow={"slide_type": "slide"}
# %%timeit

# time pd read_parquet
pd.read_parquet(path="mitocheck_example_images.parquet")

# + id="E6wwDZgYbl4j" editable=true slideshow={"slide_type": "slide"}
# %%timeit

# time pyarrow parquet read
parquet.read_table(source="mitocheck_example_images.parquet")

# + id="25gbDc6fZTma" editable=true slideshow={"slide_type": "slide"}
# %%timeit

# time lancedb read
ldb.open_table("mitocheck_example_images").to_pandas()

# + id="BEBG7JyWcCCM" editable=true slideshow={"slide_type": "slide"}
# show how to add data to an existing table
ldb.open_table("mitocheck_example_images").add(
    pd.read_parquet(filename := "mitocheck_example_images.parquet")
)
ldb.open_table("mitocheck_example_images").to_pandas()

# + id="67KNXUykfCPa" editable=true slideshow={"slide_type": "slide"}
# show version of the table
ldb.open_table("mitocheck_example_images").version

# + id="9LHtdomOfVv4" editable=true slideshow={"slide_type": "slide"}
# show a change to original version
ldb.open_table("mitocheck_example_images").checkout(version=1)
ldb.open_table("mitocheck_example_images").to_pandas()

# + [markdown] editable=true slideshow={"slide_type": "slide"}
# ## Reflections
#
# <br>
# <br>
# <br>
#
# - Images can be treated as values through objects in a database table.
# - LanceDB seems like a good option for storing multiple tables together as a "package".
# - LanceDB integrates well with Parquet, Arrow, and Pandas.
# - LanceDB feels fast!

# + [markdown] editable=true slideshow={"slide_type": "slide"}
# ## __Thank you for attending!__
#
# <br>
# <br>
#
# #### Questions / comments?
