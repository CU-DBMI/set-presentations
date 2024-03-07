---
id: dox8bs8lu3ez5rmtskxvupb
title: TR01 RTX-KG2 updates 2024 03 06
desc: ''
updated: 1707424376031
created: 1678810754228
presentation:
  theme: simple.css
  slideNumber: true
output: pdf_document
---
<!-- slide -->

![](assets/images/2024-02-08-13-11-35.png)

- [__RTX-KG2__](https://github.com/RTXteam/RTX-KG2) "... is the second-generation knowledge graph for the ARAX biomedical reasoning system."
- Includes a pipeline and data output.
- Some data not publicly available due to licensing.

<!-- slide -->

![](assets/images/2024-02-08-13-11-35.png)

- RTX-KG2 Versions:
  - __"non-canonicalized"__: untranslated from data sources.
  - __"canonicalized"__: builds a unified new ontology specific to RTX-KG2
  - __"lite"__: removes certain nodes and relationships removed to slim the graph down.

<!-- slide -->

### 🛤️ Reproducing RTX-KG2 Pipeline Execution

<br>

- ["Extended Pipeline" fork on GitHub](https://github.com/CU-DBMI/RTX-KG2)
- Attempted modified Singularity-based execution on HPC Alpine: likely requires significant redesign.
- Attempting GCP VM-based execution: some progress but blocked by data requirements and existing software bugs.
  - See: [RTX-KG2#366](https://github.com/RTXteam/RTX-KG2/issues/366), [RTX-KG2#365](https://github.com/RTXteam/RTX-KG2/issues/365), [RTX-KG2#362](https://github.com/RTXteam/RTX-KG2/issues/362), [RTX-KG2#303 (comment)](https://github.com/RTXteam/RTX-KG2/issues/303#issuecomment-1915672904)

<!-- slide -->

### 💾 Accessing RTX-KG2 Data Exports

<br>

- ["RTX-KG2-gateway" repo on GitHub](https://github.com/CU-DBMI/rtx-kg2-gateway)
- JSON property graph available at [translator-lfs-artifacts](https://github.com/ncats/translator-lfs-artifacts) offers one-way use of data (17.63 GB JSON file, 686 MB compressed).
- Used Parquet for intermediary for ingest.

<!-- slide -->

### 🔄 RTX-KG2 Data through Kuzu

<br>

<img src="assets/images/2024-03-06-09-33-40.png" style="height:150px;">

- [Kuzu](https://kuzudb.com/) is an embedded graph database technology.
- [Kuzu database of RTX-KG2](https://github.com/CU-DBMI/rtx-kg2-gateway/releases/tag/v0.0.1) successfully created (23 GB directory, 1 GB compressed).
- Working on support for the project through Cypher queries and exploration of schema.
