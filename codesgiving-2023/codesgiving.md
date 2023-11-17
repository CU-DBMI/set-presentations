---
title: Codesgiving
desc: 'Channeling the spirit of Thanksgiving by giving our thanks through code.'
updated: 1666813558462
created: 1666627016984
presentation:
    theme: simple.css
    center: false
output: pdf_document
---

<!-- slide -->

# Codesgiving

<!-- slide -->

## Goals

<br>

- Practice gratitude together
- Share open-source contribution ideas
- Make an impact

<!-- slide -->

## Context

<br>

__Thanksgiving__ is a holiday practiced in many countries which focuses on __gratitude for good harvests__ of the preceding year.


<!-- slide -->

## Context

<br>

This presentation will be about channeling the spirit of Thanksgiving by giving our _thanks_ through _code_.

<!-- slide -->

## Open-source Harvests

<br>

- What have you harvested from open-source?

<!-- slide -->

## Open-source Harvests

<br>

[CytoTable](https://github.com/cytomining/CytoTable) dependencies:


- Show Python dependencies of CytoTable and count the number of lines
- `poetry run pip freeze | wc -l`
- `141`

<!-- slide -->

## Open-source Harvests

<br>

- How can we celebrate open-source harvests?

<!-- slide -->

## Open-source Harvests

<br>

- Open-source can be an _adjective_, _noun_, or a _verb_.
- Open-source is alive and involves software gardening.

<!-- slide -->

## Open-source Participation

<img src="2023-11-17-10-56-25.png" style="width:500px;">

- Influence counts! [Circles of control and influence](https://positivepsychology.com/circles-of-influence/)

<!-- slide -->

## Open-source Participation

<br>

- Communication matters!

> "Six degrees of separation is the idea that all people are six or fewer social connections away from each other."
- [Six degrees of separation](https://en.wikipedia.org/wiki/Six_degrees_of_separation)

<!-- slide -->

## Open-source Participation

<br>

![](2023-11-17-10-59-37.png)
- [Data thinking](https://en.wikipedia.org/wiki/Data_thinking)

<!-- slide -->

## Open-source Impact

<br>

[CPython](https://github.com/python/cpython) example through estimations:

- __Github users__ >= 100,000,000 <br>[GitHub Blog: 100 million developers and counting](https://github.blog/2023-01-25-100-million-developers-and-counting/)
- __Programming languages__ <br>Python entails 17.79% of GitHub Pull Requests <br> [GitHut 2.0 Programming Languages](https://madnight.github.io/githut/#/pull_requests/2023/3)
- __Potential for impact__<br> 17.79% of 100 million : 17,790,000 people (users as developers)

<!-- slide -->

## Open-source Impact

<br>

Open issues:

- ~7,000 issues! 
- [https://github.com/python/cpython/issues](https://github.com/python/cpython/issues)

<!-- slide -->

## Open-source Impact

<br>

> "The Pareto principle states that for many outcomes, roughly 80% of consequences come from 20% of causes (the "vital few")."
- [Pareto principle](https://en.wikipedia.org/wiki/Pareto_principle)

<!-- slide -->

## Open-source Impact

<br>

Are there "vital few" areas where open-source contributions could help?

<!-- slide -->

## Python Example

<br>

Python `sqlite3` and context managers.

1. Saw feedback about closing `sqlite3` connections.
1. [Try to open feature request](https://github.com/python/cpython/issues)<br>(issues indicate to open discussion first)
1. [Opened discussion](https://discuss.python.org/t/implicitly-close-sqlite3-connections-with-context-managers/33320)
1. [Submitted issue](https://github.com/python/cpython/issues/109234)
1. [Fix related to issue](https://github.com/python/cpython/pull/110294/files)

<!-- slide -->

## Python Example

<br>

How much will it help?
- Created public discussion content
- Added public issue documentation
- Resulted in public-facing documentation updates
- Influences developer practices upstream?

<!-- slide -->

## CellProfiler

<br> 

![](2023-11-17-11-10-08.png)

<!-- slide -->

## CellProfiler

<br>

- [@jenna-tomkinson](https://github.com/jenna-tomkinson) helped communicate issues with Conda environments.
- Anecdotally I had witnessed these too, but didn't know how much this might effect the community or whether the issue still existed on my device.

<!-- slide -->

## CellProfiler Impacts

<br>

We can use GitHub, PyPI, and bibliometrics for understanding the impact metrics:

- __GitHub stars__: 817 ([link](https://star-history.com/#cellprofiler/cellprofiler&Date))
- __PyPI downloads__: 491 ([link](https://github.com/ofek/pypinfo))

<!-- slide -->

## CellProfiler Impacts

<br>

- __Google Scholar results__: 15,600 results ([link](https://scholar.google.com/scholar?as_sdt=0,6&q=%22cellprofiler%22&hl=en))
- __BioRxiv results__: 1,801 results ([link](https://www.biorxiv.org/search/cellprofiler))
- __Estimate__: 16,000 articles since 2005 ([initial CellProfiler release](https://en.wikipedia.org/wiki/CellProfiler#History)) = 888 articles per year<br><br>
- __Potential for impact__: about 500 research software engineers (or projects?) and 900 new articles per year

<!-- slide -->

## CellProfiler Impacts

<br>

Open issues: 

- ~270 issues ([total issues link](https://github.com/cellprofiler/cellprofiler/issues))
- __Targeted search__: 11 open issues, 48 closed issues ([issues search link](https://github.com/CellProfiler/CellProfiler/issues?q=is%3Aissue+is%3Aopen+conda+environment))

<!-- slide -->

## CellProfiler Exploration

<br>

- How can we try to communicate, influence, or fix this challenge?

<!-- slide -->

## CellProfiler Exploration

<br>

![](2023-11-17-11-16-25.png)

- [Test driven development](https://en.wikipedia.org/wiki/Test-driven_development)
<!-- slide -->

## CellProfiler Exploration

<br>

Troubleshooting process:

1. Verify challenge
2. Develop solution
3. Test solution

<!-- slide -->

## CellProfiler Exploration

<br>

- Forked the repository with intent to verify
- [Fork branch link](https://github.com/d33bs/CellProfiler/tree/test-driven-conda-environments)

<!-- slide -->

## CellProfiler Exploration

<br>

- Test many platforms in a reproducible container each push during development
- This makes every push a kind of hypothesis test about a fix
- [GitHub Actions matrix strategy](https://github.com/d33bs/CellProfiler/blob/test-driven-conda-environments/.github/workflows/test-conda.yml#L13)
- [GitHub Actions implementation](https://github.com/d33bs/CellProfiler/actions)

<!-- slide -->

## CellProfiler Exploration

<br>

Troubleshooting process:

1. ✅ Verify challenge
2. Develop solution
3. Test solution

<!-- slide -->

## CellProfiler Participation

<br>

More participation to come!

<!-- slide -->

## Closing Thought

<br>

- "You know more than you can say." <br> ([from a Radiolab episode](https://radiolab.org/podcast/cataclysm-sentence/transcript))

- What would you choose to give to the future?

<!-- slide -->

## Gratitude

<br>

Thank you all for who you are and what you give.

__Happy Thanksgiving!__
