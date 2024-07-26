# The Art and Craft of Python Packaging: Organizing your Python Code for Others

Expects local availability of [Quarto](https://quarto.org/docs/) and [decktape](https://github.com/astefanutti/decktape) for development work.

## Development

Use the following command to help render slides within a browser window:
`quarto preview presentation/building-and-publishing-python-packages.qmd --render slides`

## Rendering

Use the following steps to render the `qmd` file as a PDF.

1. Render the content using revealjs through quarto: `quarto render presentation/building-and-publishing-python-packages.qmd -t revealjs`
2. Use decktape to render a PDF from the html content: `decktape reveal presentation/building-and-publishing-python-packages.html presentation/building-and-publishing-python-packages.pdf`
