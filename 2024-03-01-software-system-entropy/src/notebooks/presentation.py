# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.16.1
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# + [markdown] editable=true slideshow={"slide_type": "slide"}
# <center>
#     
# ## Software Entropy and Failure
# #### Journal Club 2024-03-01
#
# </center>

# + [markdown] editable=true slideshow={"slide_type": "slide"}
# __Challenge__
#
# - We have many software heuristics when it comes to best practices.
# - How can we quantify and scientifically improve upon these practices (within the context of avoiding failures)?

# + editable=true slideshow={"slide_type": "skip"}
# slide diagram preparations
import pathlib

import requests
from IPython.display import SVG

# create an images dir
pathlib.Path("images").mkdir(exist_ok=True)


def render_mermaid_diagram(mermaid_code, filename, filedir="images"):
    """
    Saves and renders SVG of Mermaid diagram using Kroki service.
    """
    response = requests.post(
        "https://kroki.io/",
        json={
            "diagram_source": mermaid_code,
            "diagram_type": "mermaid",
            "output_format": "svg",
        },
    )

    if response.status_code == 200:
        decoded = response.content.decode("utf-8")
        with open(f"{filedir}/{filename}", mode="w") as file:
            file.write(decoded)
        return SVG(decoded)
    else:
        return f"Failed to render diagram. Status code: {response.status_code}"


# + editable=true slideshow={"slide_type": "skip"}
render_mermaid_diagram(
    """
    flowchart LR
        software["Software"] --> | changes include\nvarying | complexity
        complexity --> | which may\ncause | failures
    """,
    "title_understanding.svg",
)

# + [markdown] editable=true slideshow={"slide_type": "slide"}
# __Journal article focus__
#
# ![](images/title_understanding.svg)
#
# A. E. Hassan, __"Predicting faults using the complexity of code changes"__.
#
# DOI: [10.1109/ICSE.2009.5070510](https://doi.org/10.1109/ICSE.2009.5070510)
#

# + [markdown] editable=true slideshow={"slide_type": "slide"}
# __Title definitions__
#
# - __Faults__: _"In document ISO 10303-226, a fault is defined as an abnormal condition or defect at the component, equipment, or sub-system level which may lead to a failure."_ ([Wikipedia: Fault (technology)](https://en.wikipedia.org/wiki/Fault_(technology)))
# - __Complexity__: "... _un-certainty/randomness/complexity_ ..." (article Section 4)

# + [markdown] editable=true slideshow={"slide_type": "slide"}
# __Complexity__
#
# - Complexity as uncertainty or randomness may be understood as ___entropy___ from information theory.

# + [markdown] editable=true slideshow={"slide_type": "subslide"}
# __Complexity (information theory)__
#
# _In information theory, the entropy of a __random variable__ is the __average level__ of __"information", "surprise", or "uncertainty"__ inherent to the variable's __possible outcomes__._
#
# [Wikipedia: Entropy (information theory)](https://en.wikipedia.org/wiki/Entropy_(information_theory))
#
#

# + [markdown] editable=true slideshow={"slide_type": "subslide"}
# __Complexity (information theory)__
#
# _Entropy: 1. A measure of the disorder present in a system._
#
# [Wiktionary: Entropy](https://en.wiktionary.org/wiki/entropy)

# + [markdown] editable=true slideshow={"slide_type": "subslide"}
# __Complexity (information theory)__
#
# Wait a minute, what even is "information" in this context?
#

# + [markdown] editable=true slideshow={"slide_type": "subslide"}
# __Complexity (information theory)__
#
# ![image.png](attachment:42f84086-41ef-42ce-a68c-44402a83cc45.png)
#
# $$
# I(E) = -\log_2(p(E))
# $$
#
# Information conveyed by an event or message is inversely proportional to its probability. That is, the less probable an event is, the more information it carries when it occurs.
#
#

# + [markdown] editable=true slideshow={"slide_type": "subslide"}
# __Complexity (information theory)__
#
# Imagine a coin toss as a "message" with two equally probable outcomes.

# + editable=true slideshow={"slide_type": "subslide"}
import math

# Probability of each outcome for a fair coin toss
probability_heads = 0.5
probability_tails = 0.5

# Calculate Shannon information content for each outcome
information_heads = -math.log2(probability_heads)
information_tails = -math.log2(probability_tails)

print(f"Shannon information content for heads: {information_heads:.4f} bits")
print(f"Shannon information content for tails: {information_tails:.4f} bits")

# + editable=true slideshow={"slide_type": "skip"}
render_mermaid_diagram(
    """
flowchart LR

message["message"]
subgraph info_system["Information communication"]
message_source["Information\nsource"]
message_transmitter["Transmitter"]
noise_intersection["message noise\nintersection"]
message_receiver["Receiver"]
message_destination["Destination"]
end

subgraph noise_system["Noise generation"]
noise_source["Noise source"]
end

message -.-> message_source
message_source --> | shares message\nthrough | message_transmitter
message_transmitter --> | sends message\nfor receival | noise_intersection
noise_source --> | noise added\nto message | noise_intersection
noise_intersection --> | noisy message\nreceived by | message_receiver
message_receiver --> | sends message\nto | message_destination

style noise_intersection fill:transparent,stroke:#aaa,stroke-width:1px
    """,
    "shannon_information_communication.svg",
)

# + [markdown] editable=true slideshow={"slide_type": "subslide"}
# __Complexity (information theory)__
#
# ![](images/shannon_information_communication.svg)
#
# Entropy:
#
# $$
# H(X) = -\sum_{x \in \mathcal{X}} p(x) \log_b p(x)
# $$
#
# As understood through Shannon's communication system.

# + editable=true slideshow={"slide_type": "subslide"}
import math

# Probability of each outcome for a fair coin toss
probability_heads = 0.5
probability_tails = 0.5

# Calculate Shannon entropy for the coin toss
entropy = -(
    probability_heads * math.log2(probability_heads)
    + probability_tails * math.log2(probability_tails)
)

print(f"Shannon entropy for the fair coin toss: {entropy:.4f} bits")
print(
    "\nThe result can be understood as 'maximum uncertainty' as it's completely unpredictable (equal probabilities)."
)

# + editable=true slideshow={"slide_type": "subslide"}
import math

# Probabilities for the unfair coin toss
probability_heads = 0.3
probability_tails = 0.7

# Information content for heads and tails
information_heads = -math.log2(probability_heads)
information_tails = -math.log2(probability_tails)

# Entropy calculation
entropy = -(
    probability_heads * math.log2(probability_heads)
    + probability_tails * math.log2(probability_tails)
)

print(f"Information content for heads: {information_heads:.4f} bits")
print(f"Information content for tails: {information_tails:.4f} bits")
print(f"Entropy for the unfair coin toss: {entropy:.4f} bits")
print(
    "\nWe have more information from heads as it's less likely. We have less information from tails as it's more likely. We have less entropy because the outcome is more predictable."
)

# + [markdown] editable=true slideshow={"slide_type": "slide"}
# __Prior work with Software Failures and Complexity Measures__
#
# - Prior modifications to a file are a good predictor of its fault potential (i.e., the more a file is changed, the more likely it will contain faults).
#
# - Most code complexity metrics highly correlate with LOC (lines of code), a much simpler metric.
#
# - Process metrics outperform code metrics as predictors of future faults.
#
# - Prior faults are good predictors of future faults.

# + [markdown] editable=true slideshow={"slide_type": "slide"}
# __"Predicting faults using the complexity of code changes" Conjecture__
#
#
# - _A complex code change process negatively affects its product, the software system._
# - _The more complex changes to a file, the higher the chance the file will contain faults._
