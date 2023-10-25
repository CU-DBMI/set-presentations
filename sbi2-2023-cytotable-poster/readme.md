# SBI2 2023 Way Lab CytoTable Poster

This directory includes content related to building a poster via [Posterdown](https://github.com/brentthorne/posterdown), an R package which helps you build posters. See below for more details.

Related charts for various benchmarks may be found in the related repository: [CytoTable-benchmarks](https://github.com/cytomining/CytoTable-benchmarks).

Poster dimensions must abide (but not exactly match) SBI2 2023's maximum specifications: `91" wide x 44.75” high`.

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

# next, restore the environment using the following command
renv::restore()

# activate the renv environment
# note: this may not be necessary depending on
# whether the environment is automatically loaded.
renv::activate()
```

## Rendering

Within your R session use the following to perform various steps related to the content found in this directory.
Note: this depends on Pandoc in order to run.

```R
# create an html and PDF copy of the poster from `poster.rmd`
pagedown::chrome_print("poster.rmd")
```

## Additional notes

- [ImageMagick](http://www.imagemagick.org/) was used to form the bottom logos together as one and render the poster pdf as png using the following commands:
- Python [qrcode](https://github.com/lincolnloop/python-qrcode) is used to generate various QR codes via `qr-code-generation.sh` script.
- QR codes with images were generated and saved manually via [https://github.com/kciter/qart.js](https://github.com/kciter/qart.js)

```shell
# scale up images
convert images/qr_cytomining.png -resize 453x453 images/qr_cytomining.png

# append text to qr codes
convert images/qr_cytotable.png -gravity South -background transparent -splice 0x15 -pointsize 40 -font Arial -weight Bold -annotate 0x15 'Scan for CytoTable!' images/qr_cytotable_text.png
convert images/qr_cytomining.png -gravity South -background transparent -splice 0x15 -pointsize 40 -font Arial -weight Bold -annotate 0x15 'Scan for Cytomining!' images/qr_cytomining_text.png

# create a transparent spacer
convert -size 100x460 xc:transparent images/spacer.png

# combine the images together as one using the spacer for separation
convert -background none images/qr_cytomining_text.png images/spacer.png images/qr_cytotable_text.png images/spacer.png images/waylab.png images/spacer.png images/dbmi.png +append images/header_combined_images.png

# downconvert png's to 200x200
convert images/icon_pycytominer.png -resize 200x200 images/icon_pycytominer_small.png
convert images/icon_cytosnake.png -resize 200x200 images/icon_cytosnake_small.png
convert images/icon_cytotable.png -resize 200x200 images/icon_cytotable_small.png

# create a small transparent spacer for icons
convert -size 20x200 xc:transparent images/icon_spacer.png

# combine the images together as one using the spacer for separation for icons
convert +append images/icon_pycytominer_small.png images/icon_spacer.png images/icon_cytosnake_small.png images/icon_spacer.png images/icon_cytotable_small.png images/icon_spacer.png images/icon_cytomining.png images/icons_combined.png

# convert the poster pdf to png and jpg with 150 dpi and a white background
convert -antialias -density 300 -background white -flatten poster.pdf poster.png
convert -antialias -density 300 -background white -flatten poster.pdf poster.jpg
```
