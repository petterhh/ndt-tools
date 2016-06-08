# ndt-tools
Tools for use with Norwegian Dependency Treebank. See
[http://petterhh.github.io/ndt-tools/](http://petterhh.github.io/ndt-tools/)
for full documentation.

## Data set split
The **dataset** folder contains the data set split (training/dev/test) of the
Norwegian Dependency Treebank. 

## Tagger model and parser model
The **models** folder contains a PoS tagger model (for use with SVMTool) and a
syntactic parser model (for use with Mate) for Norwegian. 

## Scripts
The **scripts** folder contains three Python scripts for use with the treebank. 
- `generate_split.py` generates a data set split (training/dev/test) of the
treebank, provided a path to the original treebank files. 
- `map_tagset.py` maps the tag set of the treebank by introducing supplied
  morphological features present in the treebank.
- `tagging_error_analysis.py` performs error analysis in terms of precision,
  recall and F score.

