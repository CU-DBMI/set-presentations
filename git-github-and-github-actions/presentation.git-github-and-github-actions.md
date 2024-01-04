---
id: dox8bs8lu3ez5rmtskxvupb
title: GitHub Best Practices and GitHub Actions
desc: ''
updated: 1680299258279
created: 1678810754228
presentation:
  theme: simple.css
    # Display the page number of the current slide
  slideNumber: True
output: pdf_document
---

<!-- slide -->

### <span style="color:#777; text-align:center;">Bioinfo Primer

### <span style="color:#222; text-align:center;font-weight:bold">Git, GitHub, and GitHub Actions: Using Developer Tools for Scientific Software</span>

<!-- slide -->

### Presentation Outline

<br>

1. 👤 Brief Introduction
1. 🌱 Git Concepts
1. 🚀 GitHub Features

<!-- slide -->

### Brief Introduction

<br>

👋🤓 Hi, I'm Dave!

&bull;

University of Colorado Anschutz Medical Campus
Department of Biomedical Informatics
Software Engineering Team

<!-- slide -->

### Git &bull; Preamble

<br>

- ⏲️ Git has many interesting but confusing aspects which may result in lost time.

- 🪴 __Software gardening approach__: development is messy, we're all learning and growing.

- 😃 Focus on __good communication__ and __progress__ instead of perfection.

<!-- slide -->

### Git &bull; Preamble

<br>

Distinguish between:

1. __Coding:__ doing the programming / problem solving.

1. __Source control (Git):__ saving and sharing the work.

1. __GitHub__: communication and automation for code.

<!-- slide -->

### Git &bull; Definitions

![](/assets/images/2023-03-14-11-18-42.png)
<span style="font-size:.5em;">_[https://www.xkcd.com/1597](https://www.xkcd.com/1597)_</span>

<!-- slide -->

### Git &bull; Definitions

<br>

- [Git](https://en.wikipedia.org/wiki/Git) is software for managing code collaboration.

- [GitHub](https://github.com/) is a <span style="font-weight: bold">_platform_</span> which enables code collaboration and hosting through __Git__.

- One can use Git independent of GitHub.

<!-- slide -->

### Git &bull; Concepts

![](/assets/images/2023-03-29-12-20-26.png)

Git keeps track of code using __repositories__ ("repos").

<!-- slide -->

### Git &bull; Concepts

![](/assets/images/2023-03-27-14-11-51.png)

How do we add code to repositories in Git?

<!-- slide -->

### Git &bull; Concepts

![](/assets/images/2023-03-27-14-26-47.png)

Code is stored inside a repository __branch__.

<!-- slide -->

### Git &bull; Concepts

![](/assets/images/2023-03-28-12-27-13.png)

Branches are timelines of code changes.

<!-- slide -->

### Git &bull; Concepts

![](/assets/images/2023-03-27-14-45-30.png)
<span style="font-size:.8em;">Think of these timelines like Google Docs revision history.</span>

<!-- slide -->

### Git &bull; Concepts

![](/assets/images/2023-03-28-12-27-46.png)

Branch timeline changes are recorded in __commits__.

<!-- slide -->

### Git &bull; Concepts

![](/assets/images/2023-03-28-12-28-02.png)

Commits record changes in one or many files.

<!-- slide -->

### Git &bull; Concepts

![](/assets/images/2023-03-29-12-37-50.png)

Repositories may have multiple branches.

<!-- slide -->

### Git &bull; Concepts

![](/assets/images/2023-03-29-12-38-42.png)

Branches are usually __based__ on one another.

<!-- slide -->

### Git &bull; Concepts

![](/assets/images/2023-03-29-12-38-59.png)

Branches are often __merged__ to include new changes.

<!-- slide -->

### Git &bull; Concepts

![](/assets/images/2023-03-28-16-24-20.png)

Changes can be independent at first...

<!-- slide -->

### Git &bull; Concepts

![](/assets/images/2023-03-28-16-25-09.png)

Changes can be merged to unify the timelines.

<!-- slide -->

### Git &bull; Concepts

![](/assets/images/2023-03-30-10-09-22.png)
<span style="font-size:.8em;">Merging from another branch is also called __pulling__*.
(*pulling technically involves __fetching__ updates then __merging__)</span>
<span style="font-size:.5em;">([Image from Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Daubigny_-_Ship%E2%80%99s_Boy_Pulling_on_the_Line_(Hauling_on_the_Rope),_1927.2632a.jpg))</span>

<!-- slide -->

### Git &bull; Concepts

![](/assets/images/2023-03-29-12-23-20.png)

Repositories are stored __locally__ and __remotely__.
(GitHub provides remote repository hosting)

<!-- slide -->

### Git &bull; Concepts

![](/assets/images/2023-03-29-12-21-19.png)

Development usually happens in a local repository.

<!-- slide -->

### Git &bull; Concepts

![](/assets/images/2023-03-29-12-27-44.png)

Local work may be synchronized with __remotes__.

<!-- slide -->

### Git &bull; Concepts

![](/assets/images/2023-03-30-09-44-52.png)
<span style="font-size:.9em;">Duplicating a repository locally is called __cloning__.</span>

<!-- slide -->

### Git &bull; Concepts

![](/assets/images/2023-03-30-10-12-52.png)
<span style="font-size:.9em;">Cloned repositories include references to remote branches.
</span>

<!-- slide -->

### Git &bull; Concepts

![](/assets/images/2023-03-30-09-30-22.png)
<span style="font-size:.9em;">Local and remote repositories are not automatically in sync.
(after updates are made)
</span>

<!-- slide -->

### Git &bull; Concepts

![](/assets/images/2023-03-30-09-14-04.png)

Local branch updates are __pushed__ to remotes.

<!-- slide -->

### Git &bull; Concepts

![](/assets/images/2023-03-30-09-15-15.png)
Local branches may __pull__ updates from remotes.

<!-- slide -->

### Git &bull; Concepts

![](/assets/images/2023-03-30-09-16-40.png)
<span style="font-size:.9em;">Remote branches may also __pull__ updates from each other.
(similar to local branches)</span>

<!-- slide -->

### Git &bull; Concepts

<br>

Recommended repository files:

- __`README.md`__: General documentation.
- __`LICENSE`__: Licensing and copyright details.
- __`.gitignore`__: What to keep out of repo.

<!-- slide -->

### Git &bull; Concepts

![](/assets/images/2023-03-29-14-03-38.png)

A developer uses a __Git client__
to interact with repositories.

<!-- slide -->

### Git &bull; Client

<br>

Use a Git client which reduces barriers
or brings joy to ___you___(!).

<!-- slide -->

### Git &bull; Clients

![](/assets/images/2023-03-29-14-10-33.png)
[GitHub Desktop](https://desktop.github.com/) (<https://desktop.github.com/>)

<!-- slide -->

### Git &bull; Clients

![](/assets/images/2023-03-21-15-47-40.png)
<span style="font-size:.8em">[Visual Studio Code: Source Control](https://code.visualstudio.com/docs/sourcecontrol/overview) (<https://code.visualstudio.com/>)</span>

<!-- slide -->

### Git &bull; Clients

```bash
username ~ % git --help
usage: git [-v | --version] [-h | --help] [-C <path>] [-c <name>=<value>]
           [--exec-path[=<path>]] [--html-path] [--man-path] [--info-path]
           [-p | --paginate | -P | --no-pager] [--no-replace-objects] [--bare]
           [--git-dir=<path>] [--work-tree=<path>] [--namespace=<name>]
           [--super-prefix=<path>] [--config-env=<name>=<envvar>]
           <command> [<args>]
...
```

Git command line (<https://git-scm.com/downloads>)

<!-- slide -->

### Git &bull; Clients

![](/assets/images/2023-03-29-15-06-14.png)
The Github website provides git-like capabilities.

<!-- slide -->

### Git &bull; Demonstration

<br>

An _opinionated_ demo of concepts using:

<br>

- Github website to create a repo.
- Github Desktop app to interact with the repo.
- VS Code to make some changes.
<!-- slide -->

### GitHub Features

<br>

GitHub adds features on top of Git to help
save time, communicate, and more.

<!-- slide -->

### GitHub Features - Brief Notes

<br>

- ⚽ Software can be a __team__ sport!

- Treat changes like __"shots on goal"__.

- Leaning on and learning from
 your team gives you __strength__.

- __Communicate__ and act with __kindness__.

<!-- slide -->

### GitHub Features - Pull Requests

![](/assets/images/2023-03-30-11-40-31.png)
Updates are requested between
branches using __Pull Requests__.

<!-- slide -->

### GitHub Features - Pull Requests

![](/assets/images/2023-03-30-11-48-14.png)
__Pull Requests__ are a way to ensure
changes are ready for a merge.

<!-- slide -->
### GitHub Features - Pull Requests

![](/assets/images/2023-03-30-11-55-16.png)
__Pull Request Reviews__ are added to PR's
to formalize and track decisions.

<!-- slide -->

### GitHub Features - Issues

![](/assets/images/2023-03-30-12-12-32.png)
__GitHub Issues__ provide a way to track
bugs, features, and questions in a repo.

<!-- slide -->
### GitHub Features - Issues

![](/assets/images/2023-03-30-12-38-32.png)
Pull Requests can reference and help __close__ issues.

<!-- slide -->

### GitHub Features - GitHub Actions

![](/assets/images/2023-03-31-09-36-38.png)
__GitHub Actions__ are triggered __workflows__ for repos.

<!-- slide -->

### GitHub Features - GitHub Actions

![](/assets/images/2023-03-31-09-24-16.png)
__GitHub Actions__ can provide automatic checks for PR's.

<!-- slide -->

### GitHub Features - Demonstration

![](/assets/images/2023-03-31-09-47-03.png)
A quick walkthrough of these features on
<https://github.com/r-lib/lintr>

<!-- slide -->

<br>

Further references:

- __Pull Requests:__ <https://cu-dbmi.github.io/set-website/2023/02/13/Branch-Review-and-Learn.html>
- __GitHub Actions:__ <https://cu-dbmi.github.io/set-website/2023/03/15/Automate-Software-Workflows-with-Github-Actions.html>

<!-- slide -->

<br>

__Thank you!__

Questions / Comments?
