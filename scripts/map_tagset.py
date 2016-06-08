#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Map coarse tag set to more fine-grainedtag set in CoNLL file based on supplied
tags and morphological features
"""

import sys
import argparse
from collections import defaultdict

def map_tagset(conll_file, tagset, output):
    """Map coarse tag set to more fine-grained tag set in conll file"""
    out = open(output, 'w')
    coarse_tags = []
    fine_tags = defaultdict(list)

    # Process the tag set file
    with open(tagset, 'r') as f:
        # Read the coarse tags
        tag = f.readline()
        while tag != '\n':
            tag = tag.strip()
            coarse_tags.append(tag)
            tag = f.readline()

        # Read the tag set modifications
        line = f.readline()
        while line:
            tag = line.strip().split(' ')
            coarse_tag = tag[0]
            features = tag[1]
            fine_tags[coarse_tag].append(features)
            line = f.readline()

    # Process the input file
    with open(conll_file, 'r') as data:
        for line in data:
            if line.strip():
                line = line.split('\t')
                coarse_tag = line[3]
                features = line[5]

                # Finiteness mapping
                # if coarse_tag == 'verb':
                    # if 'inf' in features or 'perf-part' in features:
                        # line[3] += '|infin'
                        # line[4] += '|infin'
                        # line = '\t'.join(line)
                        # out.write(line)
                        # continue
                    # if 'imp' in features or 'pres' in features or 'pret' in features:
                        # line[3] += '|fin'
                        # line[4] += '|fin'
                        # line = '\t'.join(line)
                        # out.write(line)
                        # continue

                # Check whether we want to modify tag
                if fine_tags[coarse_tag]:
                    accumulated_features_set = set()
                    accumulated_features_list = []
                    token_features = set(features.split('|'))

                    # Iterate tag set modifications to find applicable tag
                    for feature in fine_tags[coarse_tag]:
                        tag_features_set = set(feature.split('|'))
                        tag_features_list = list(feature.split('|'))

                        # Test for tag mapping
                        if (tag_features_set.issubset(token_features) and
                                tag_features_set.issuperset(accumulated_features_set)):
                            accumulated_features_set = tag_features_set
                            accumulated_features_list = tag_features_list

                    # Replace original tag with new, fine-grained tag
                    if len(accumulated_features_list) > 0:
                        line[3] += '|' + '|'.join(accumulated_features_list)
                        line[4] += '|' + '|'.join(accumulated_features_list)
                line = '\t'.join(line)
                out.write(line)
            else:
                out.write('\n')
    out.close()

def main(argv):
    """Main function"""
    parser = argparse.ArgumentParser(description='Tag set mapping module')
    parser.add_argument('--corpus', '-c',
            required=True,
            type=str,
            help='input data in CoNLL-X format')
    parser.add_argument('--tagset', '-t',
            required=True,
            type=str,
            help='tag set file')
    parser.add_argument('--output', '-o',
            required=True,
            type=str,
            help='output file')
    args = parser.parse_args()
    map_tagset(args.corpus, args.tagset, args.output)

if __name__ == '__main__':
    sys.exit(main(sys.argv))
