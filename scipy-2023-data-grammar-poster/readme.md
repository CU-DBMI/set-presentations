# SciPy 2023 Way Lab CytoTable Data Grammar Poster

This directory includes content related to building a poster via [Posterdown](https://github.com/brentthorne/posterdown), an R package which helps you build posters. See below for more details.

Related charts for various benchmarks may be found in the related repository: [CytoTable-benchmarks](https://github.com/cytomining/CytoTable-benchmarks).

Poster dimensions follow SciPy 2023's specifications: `3 ft tall by 4 ft wide in “horizontal”/“landscape” format`.

## Dependencies

- [R](https://www.r-project.org/) >= 4.2.3
- [Pandoc](https://pandoc.org/)
- [mermaid-cli](https://github.com/mermaid-js/mermaid-cli)
- [ImageMagick](http://www.imagemagick.org/)

## Development

[Renv](https://rstudio.github.io/renv/index.html) is used to maintain the R environment.
Change directory to scipy-2023-data-grammar and activate an R session.

```R
# install renv
install.packages("renv")

# activate the renv environment
# note: this may not be necessary depending on
# whether the environment is automatically loaded.
renv::activate()

# next, restore the environment using the following command
renv::restore()
```

## Rendering

Within your R session use the following to perform various steps related to the content found in this directory.
Note: this depends on Pandoc in order to run.

```R
# create an html and PDF copy of the poster from `poster.rmd`
pagedown::chrome_print("poster.rmd")
```

## Additional notes

- [mermaid-cli](https://github.com/mermaid-js/mermaid-cli) was used to render an image for the main/center block of the poster via the following command: `mmdc -i main-diagram.mmd -o main-diagram.png -b transparent -s 2`
- [ImageMagick](http://www.imagemagick.org/) was used to form the bottom logos together as one and render the poster pdf as png using the following commands:

```shell
# create a transparent spacer
convert -size 100x453 xc:transparent images/spacer.png

# combine the images together as one using the spacer for separation
convert +append images/qr-code.png images/spacer.png images/waylab.png images/spacer.png images/dbmi.png images/combined.png

# convert the poster pdf to png with 150 dpi
convert -density 150 poster.pdf poster.png
```
