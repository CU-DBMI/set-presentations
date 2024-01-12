---
id: dox8bs8lu3ez5rmtskxvupb
title: Bridges for Tabular Dimension Chasms
desc: ''
updated: 1705092313395
created: 1678810754228
presentation:
  theme: simple.css
  slideNumber: true
output: pdf_document
---

<!-- slide -->

### <span style="color:#777; text-align:center;">Research in Progress

### <span style="color:#222; text-align:center;font-weight:bold">Bridges for Tabular Dimension Chasms</span>

<!-- slide -->

### Presentation Outline

<br>

1. Tabular data formats
1. Dimensional data
1. Relationships

<!-- slide -->

### Context

<br>
<br>

Why?

- [CytoTable](https://github.com/cytomining/CytoTable): a work in progress building on these concepts.

<!-- slide -->

### Tabular data

<br>

<table>
<tr><th>Col_A</th><th>Col_B</th><th>Col_C</th></tr>
<tr><td>1</td><td>a</td><td>0.01</td></tr>
<tr><td>2</td><td>b</td><td>0.02</td></tr>
</table>

<br>

A visual example of tabular data.

<!-- slide -->

### Tabular data

<br>

- __Definitions__:
  - __Encoding__: "convert into a "coded" form."
  - __Coded__: "converted into a code to convey a secret meaning."

<br>

Source: [Oxford Languages via Google](https://languages.oup.com/google-dictionary-en/)

<!-- slide -->

### Tabular data

<br>

🤖 &nbsp; 💬 &nbsp; 🤖

<br>

Computer secrets? 🤷

<!-- slide -->

### Tabular data &bull; CSV

<br>

```html
Col_A,Col_B,Col_C
1,a,0.01
2,b,0.02
```

<br>

A CSV (comma delimited spreadsheet) table.

<!-- slide -->

### Tabular data &bull; CSV

<br>

Strengths of CSV's

- Simple
- Interoperable
- Human-readable

<!-- slide -->

### Tabular data &bull; CSV

<br>

```html
Col_A,Col B,Col_C,COL_D
,a,"0.01"
2,null,0.02,{'color':'blue'}
```

<br>

A challenging CSV table.

<!-- slide -->

### Tabular data &bull; CSV

<br>

Challenges with CSV's

- No data types
- Expensive to slice (cols or rows)
- Missing data handling
- 2D dimensionality

<!-- slide -->

### Tabular data &bull; Parquet

<br>

```text
file.parquet (unable to view)
```

Parquet files stored as a table.

<!-- slide -->

### Tabular data &bull; Parquet

<br>
<br>

What even is a parquet file?

Why would we use it?

<!-- slide -->

### Tabular data &bull; Parquet

<br>
<br>

- "__Apache Parquet__ is an open source, column-oriented data file format designed for efficient data storage and retrieval." (<https://parquet.apache.org/>)

<!-- slide -->

### Tabular data &bull; Parquet

<br>
<br>

- Column orientation?
  - Data is stored with column-wise access in mind.
  - Whereas, with CSV, we must access data row-wise.
  - We can access a single column without reading the full dataset.

<!-- slide -->

### Tabular data &bull; Parquet

<br>

![](/assets/images/2024-01-12-10-19-10.png)

<!-- slide -->

### Tabular data &bull; Parquet

<br>

![](/assets/images/2024-01-12-10-20-30.png)

<!-- slide -->

### Tabular data &bull; Parquet

<br>

![](/assets/images/2024-01-12-11-08-51.png)

Parquet files can be "chunks" of rows from a directory.

(They all need the same columns + types to do this)

<!-- slide -->

### Tabular data &bull; Parquet

<br>

- Open question: what if columns or groups of columns were split into subdirectories?
- Some inspiration for this: [Firebolt whitepaper](https://www.firebolt.io/resources/firebolt-cloud-data-warehouse-whitepaper)

<!-- slide -->

### Tabular data &bull; Parquet

<br>

```text
ParquetDataset/
├── Column1/
│   ├── file1.parquet
│   └── file2.parquet
└── Column2/
    ├── file1.parquet
    └── file2.parquet
```

<br>

Ex. columnar + row-wise chunking Parquet dataset.

<br>

<!-- slide -->

### Tabular data &bull; Parquet

<br>

- Could you:
  - Parse infinitely different groups of columns?
  - Scale better column-wise?

<!-- slide -->

### Tabular data &bull; Parquet

<br>
<br>

What else is inside Parquet? 👀

<!-- slide -->

### Tabular data &bull; Parquet

<br>

- __Definitions__:
  - __Schema__: "a representation of a plan or theory in the form of an outline or model." ([Oxford Languages via Google](https://languages.oup.com/google-dictionary-en/))
  - __Metedata__: "data that provides information about other data" ([Wikipedia: Metadata](https://en.wikipedia.org/wiki/Metadata))

<!-- slide -->

### Tabular data &bull; Parquet

<br>

Okay, cool, what else? 🤔

- Data typing: every column has a type.
- Schema: can view types without inference
- Metadata: provide custom metadata

<!-- slide -->

### Tabular data &bull; Parquet

<br>

_Why are you bothering me about these things?!_

- Data typing: no second guessing a column type!
- Schema: documented data structure (see above)!
- Metadata: where/why did this data come to be?!

<!-- slide -->

### Quick Technical Demonstration

<br>

A quick demonstration of these things in Parquet.

[Google Colab Notebook](https://colab.research.google.com/drive/1e5pxTKOjRbUXQfFmZLJa7ZwQRwG2PZfB)

Jump back here when things get _awkward_. 🙃

<!-- slide -->

### Tabular data &bull; Dimensionality

<br>

- Dimensionality: Parquet supports a number of multidimensional data types which enhance our ability to share information about the data.

Controversial: most things aren't _perfectly_ 2D!

<!-- slide -->

### Tabular data &bull; Dimensionality

<br>

![](/assets/images/2024-01-12-10-44-18.png)

Dimensionality: most things aren't _perfectly_ 2D!

There are hidden regularity expectations with data.

What if the data aren't regular?

<!-- slide -->

### Tabular data &bull; Dimensionality

<br><br>

What if the data aren't regular?

We spend ___a lot___ of time trying to make it regular. 😦

<!-- slide -->

### Tabular data &bull; Dimensionality

<br>

- Concept: __Jagged arrays__
- "... a jagged array, also known as a ragged array or irregular array is an array of arrays of which the member arrays can be of different lengths ..."([Wikipedia: Jagged array](https://en.wikipedia.org/wiki/Jagged_array))

<!-- slide -->

### Tabular data &bull; Dimensionality

<br>

![](/assets/images/2024-01-12-10-58-19.png)

Jagged arrays in Python: [Awkward Array](https://github.com/scikit-hep/awkward).

<!-- slide -->

### Tabular data &bull; Dimensionality

<br>

Back to the Awkward demonstration.

[Google Colab Notebook](https://colab.research.google.com/drive/1e5pxTKOjRbUXQfFmZLJa7ZwQRwG2PZfB)

<!-- slide -->

### Tabular data &bull; Dimensionality

<br>

![](/assets/images/2024-01-12-11-28-21.png)

<br>

Dimensionality can also be about __relationships__.

<!-- slide -->

### Tabular data &bull; Relationships

<br>

- To-do's:
  - Explore [linked data](https://en.wikipedia.org/wiki/Linked_data) and Parquet.
  - Investigate portable graph technologies for Parquet ([Kuzu](https://kuzudb.com/docusaurus/getting-started/)).
  - Expand understanding on query languages in context, SQL and [Cypher](https://kuzudb.com/docusaurus/cypher).

<!-- slide -->

<br>

__Thank you!__

Questions / Comments?
