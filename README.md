*Please note that this repository is under development.*

# ndt-tools
This repository provides NLP resources for Norwegian, based on the [Norwegian
Dependency Treebank
(NDT)](http://www.nb.no/sprakbanken/show?serial=oai%3Anb.no%3Asbr-10&lang=en).
It provides a data set split (training/dev/test) of the treebank as well as PoS
tagger models and syntactic parser models trained on the training data in the
treebank. 

## Optimized PoS tag set
Hohle (2016) proposes a tag set optimized for syntactic dependency parsing of Norwegian,
hitherto referred to as the optimized tag set. This tag set is based on the
original tag set of NDT, with the addition of 20 PoS tags providing more
fine-grained morphosyntactic information.

## Data set split
This repository provides a data set split (training/dev/test) of NDT. This
split follows the commonly used 80-10-10 split, where 80% of the data resides
in the training data, 10% is used for testing during development and 10% is
held-out and used for final evaluation. In the creation of this split, care was
taken to preserve contiguous texts and to keep the split balanced in terms of
genre.

### Using the original tag set
* `training.conll` contains the training data.
* `dev.conll` contains the development data.
* `test.conll` contains the test data.

### Using the optimized tag set
* `training-optimized.conll` contains the training data.
* `dev-optimized.conll` contains the development data.
* `test-optimized.conll` contains the test data.

## PoS tagger models and syntactic parser models
* `svmtool-tagger-model` contains the model files for use with the SVMTool
  tagger, using the original tag set.
* `svmtool-optimized-tagger-model` contains the model files for use with the
  SVMTool tagger, using the optimized tag set.  
* `mate-parser-model` contains the model file for use with the Mate parser,
  using the original tag set.
* `mate-optimized-parser-model` contains the model file for use with the Mate
  parser, using the optimized tag set.

### Installation
In the evaluation of PoS taggers and syntactic dependency parsers in Hohle (2016), 
I found that SVMTool was the best tagger and Mate the best parser on NDT. 

* [Download SVMTool (version 1.3.1)](http://www.cs.upc.edu/~nlp/SVMTool/SVMTool.v1.3.1.tar.gz) 
* [Download Mate (version 3.6.1)](https://storage.googleapis.com/google-code-archive-downloads/v2/code.google.com/mate-tools/anna-3.61.jar)

Please consult the documentation for
[SVMTool](http://www.cs.upc.edu/~nlp/SVMTool/SVMTool.v1.4.pdf) and
[Mate](https://storage.googleapis.com/google-code-archive-downloads/v2/code.google.com/mate-tools/shortmanual.pdf)
for details on how to install and run these tools once they are downloaded.

## Scripts
* `generate_split.py` generates a data set split (training/dev/test) of the
    treebank, provided a path to the original treebank files.
* `map_tagset.py` maps the tag set of the treebank by introducing supplied
    morphological features present in the treebank.
* `tagging_error_analysis.py` performs error analysis in terms of precision,
    recall and F score.

## References
Please cite the following thesis if you use these resources in academic works:

>Hohle, P. (2016). *[Optimizing a PoS Tag Set for Norwegian Dependency
>Parsing](https://www.duo.uio.no/bitstream/handle/10852/51091/Hohle-master.pdf)*
>(Master's thesis). University of Oslo, Oslo, Norway.
