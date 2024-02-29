# 2024-03-01-software-system-entropy Presentation

A presentation on software system entropy and failures.

## Installation

### Python

Usage of the contents found within this repository depend on Python being available on the system.
One suggested way to use and manage Python is through [`pyenv`](https://github.com/pyenv/pyenv?tab=readme-ov-file#installation) (there are many other ways too!).
Please reference the `pyproject.toml` file for more information on Python versions which are compatible with this project.

### Poetry environment

Please use Python [`poetry`](https://python-poetry.org/) to run and install a Python environment related to this project.
The Poetry environment for this project includes dependencies which help run IDE environments, manage the data, and run workflows.
See here for more information about [installing Poetry](https://python-poetry.org/docs/#installation) within your environment.

```bash
# context: within the root of the repository
# after installing poetry, create the environment
poetry install
```

## Development

### Running and updating Jupyter notebooks

Please follow installation steps above and then use a related Jupyter environment to open and explore the notebooks under the `notebooks` directory.
These notebooks leverage [Jupyter Lab extensions](https://jupyterlab.readthedocs.io/en/stable/user/extensions.html) (such as [`jupytext`](https://jupytext.readthedocs.io/en/latest/)) through the related Poetry environment for this repository.
Usage of the notebooks outside of Jupyter Lab as an IDE may have varied experiences.

```bash
# context: within the root of the repository
# after creating poetry environment, run jupyter
poetry run jupyter lab
```

### Executing sequences of Python modules as tasks

We use [Poe the Poet](https://poethepoet.natn.io/index.html) to define and run tasks defined within `pyproject.toml` under the section `[tool.poe.tasks*]`.
This allows for the definition and use of a task workflow when implementing multiple procedures in sequence.

For example, use the following to run the `present` task:

```bash
# context: within the root of the repository
# run data_prep task using poethepoet defined within `pyproject.toml`
poetry run poe present
```
