# ndt-tools
Tools for use with the Norwegian Dependency Treebank. See
[http://petterhh.github.io/ndt-tools/](http://petterhh.github.io/ndt-tools/)
for full documentation.

*Note that this repository is under development and updated continuously.*

## Data set split
The **dataset** folder contains a data set split (training/dev/test) of the
Norwegian Dependency Treebank. 

## Tagger model and parser model
The **models** folder contains PoS tagger models (for use with SVMTool) and
syntactic parser models (for use with Mate) for Norwegian. 

## Scripts
The **scripts** folder contains three Python scripts for use with the treebank. 
- `generate_split.py` generates a data set split (training/dev/test) of the
treebank, provided a path to the original treebank files. 
- `map_tagset.py` maps the tag set of the treebank by introducing supplied
  morphological features present in the treebank.
- `tagging_error_analysis.py` performs error analysis in terms of precision,
  recall and F score.

