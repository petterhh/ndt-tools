#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Generate data set split (training/development/test) of the Norwegian
Dependency Treebank
"""

import argparse
import os
import sys

def generate_split(ndtpath):
    """Generate data set split (training/development/test) of NDT"""
    if not os.path.exists(ndtpath + '/nob/conll'):
        sys.exit('Error in file directory: {}/nob/conll not found'
                .format(ndtpath))

    os.chdir(ndtpath + '/nob/conll')

    # Create the data set split
    for dataset in ('training', 'dev', 'test'):
        with open(dataset + '.conll', 'a') as out:
            with open(dataset + '_files') as files:
                files = files.read().split('\n')[:-1]
                for conll_file in files:
                    with open(conll_file, 'r') as data:
                        sents = data.read()
                        out.write(sents)

def main(argv):
    """Main function"""
    parser = argparse.ArgumentParser(\
            description='Generates data set split (training/dev/test) of NDT')
    parser.add_argument('--path', '-p',
            required=True,
            type=str,
            help='path to NDT_1-01 directory')
    args = parser.parse_args()
    generate_split(args.path)

if __name__ == '__main__':
    sys.exit(main(sys.argv))
