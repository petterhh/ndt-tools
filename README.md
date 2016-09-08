# ndt-tools
Tools for use with the Norwegian Dependency Treebank. 

*Note that this repository is under development.*

## Optimized PoS tag set
Hohle (2016) proposes a tag set optimized for syntactic parsing of Norwegian,
hitherto referred to as the optimized tag set. This tag set is based on the
original tag set of NDT, with the addition of 20 PoS tags providing more
fine-grained morphosyntactic information.

## Data set split
This repository provides a data set split (training/dev/test) of the Norwegian
Dependency Treebank. This split follows the commonly used 80-10-10 split, where
80% of the data resides in the training data, 10% is used for testing during
development and 10% is held-out and used for final evaluation. In the creation
of this split, care was taken to preserve contiguous texts and to keep the
split balanced in terms of genre.

###Using the original tag set
* `training.conll` contains the training data.
* `dev.conll` contains the development data.
* `test.conll` contains the test data.

###Using the optimized tag set
* `training-optimized.conll` contains the training data.
* `dev-optimized.conll` contains the development data.
* `test-optimized.conll` contains the test data.

##PoS tagger model and syntactic parser model
* `svmtool-tagger-model` contains the model files for use with the SVMTool
  tagger, using the original tag set.
* `svmtool-optimized-tagger-model` contains the model files for use with the
  SVMTool tagger, using the optimized tag set.  
* `mate-parser-model` contains the model file for use with the Mate parser,
  using the original tag set.
* `mate-optimized-parser-model` contains the model file for use with the Mate
  parser, using the optimized tag set.

##Usage
For more information on these tools, please consult the documentation for SVMTool and Mate.

##Scripts

* `generate_split.py` generates a data set split (training/dev/test) of the
    treebank, provided a path to the original treebank files.
* `map_tagset.py` maps the tag set of the treebank by introducing supplied
    morphological features present in the treebank.
* `tagging_error_analysis.py` performs error analysis in terms of precision,
    recall and F score.

##References
Please cite the following thesis if you use these resources in academic works:

Hohle, P. (2016). *[Optimizing a PoS Tag Set for Norwegian Dependency
Parsing](https://www.duo.uio.no/bitstream/handle/10852/51091/Hohle-master.pdf)* (Master's thesis). University of Oslo, Oslo, Norway.
