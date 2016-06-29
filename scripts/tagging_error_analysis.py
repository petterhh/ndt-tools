#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Compute precision, recall and F-score for each PoS tag
"""

from __future__ import division
from collections import defaultdict
from itertools import izip
import argparse
import sys

def tagging_eval(gold_data, predicted_data, tagger, output):
    """Computes precision, recall and F-score for each PoS tag"""
    tags = []
    true_positives = defaultdict(int)
    false_positives = defaultdict(int)
    false_negatives = defaultdict(int)

    with open(gold_data, 'r') as gold, open(predicted_data, 'r') as predicted:
        if tagger == 'tnt':
            predicted = predicted.readlines()[12:]

        for gold_line, predicted_line in izip(gold, predicted):
            if gold_line.strip() and predicted_line.strip():
                if tagger == 'tnt':
                    gold_line = gold_line.strip().split('\t')
                    predicted_line = predicted_line.strip().split('\t')
                elif tagger == 'svmtool':
                    gold_line = gold_line.strip().split(' ')
                    predicted_line = predicted_line.strip().split(' ')
                else:
                    sys.exit('Unsupported tagger: {}'.format(tagger))

                if gold_line[0] != predicted_line[0]:
                    print('Token discrepancy between gold and predicted data:')
                    print('{} != {}'.format(gold_line[0], predicted_line[0]))
                    sys.exit()

                gold_tag = gold_line[len(gold_line)-1]
                predicted_tag = predicted_line[len(predicted_line)-1]

                if gold_tag not in tags:
                    tags.append(gold_tag)

                if gold_tag == predicted_tag:
                    # Correct tag
                    true_positives[gold_tag] += 1
                else:
                    # Incorrect tag
                    false_positives[predicted_tag] += 1
                    false_negatives[gold_tag] += 1

    out = open(output, 'w')
    out.write('  Precision, recall and F-score of tagging\n\n')
    out.write('  ---------------------+------+---------+--------+-----------+--------+--------\n')
    out.write('  tag                  | gold | correct | system | precision | recall | F-score\n')
    out.write('  ---------------------+------+---------+--------+-----------+--------+--------\n')

    for tag in sorted(tags):
        try:
            precision = true_positives[tag] / (true_positives[tag] + false_positives[tag])
            precision *= 100
        except ZeroDivisionError:
            precision = 0.00

        try:
            recall = true_positives[tag] / (true_positives[tag] + false_negatives[tag])
            recall *= 100
        except ZeroDivisionError:
            recall = 0.00

        try:
            fscore = (2 * precision * recall) / (precision + recall)
        except ZeroDivisionError:
            fscore = 0.00

        gold = true_positives[tag] + false_negatives[tag]
        correct = true_positives[tag]
        predicted = true_positives[tag] + false_positives[tag]

        out.write('  {0:<16}     | {1:>4} |    {2:>4} |   {3:>4} |    {4:>6.2f} | {5:>6.2f} | {6:>6.2f}\n'.format(
                tag, gold, correct, predicted, precision, recall, fscore))
    out.close()

def main():
    """Main function"""
    parser = argparse.ArgumentParser(
            description='Computes precision, recall and F-score for each PoS tag')
    parser.add_argument(
            '--gold',
            '-g',
            required=True,
            type=str,
            help='gold tags')
    parser.add_argument(
            '--predicted',
            '-p',
            required=True,
            type=str,
            help='predicted tags')
    parser.add_argument(
            '--tagger',
            '-t',
            required=True,
            type=str,
            help='PoS tagger')
    parser.add_argument(
            '--output',
            '-o',
            type=str,
            required=True,
            help='output file')
    args = parser.parse_args()
    tagging_eval(args.gold, args.predicted, args.tagger, args.output)

if __name__ == '__main__':
    sys.exit(main())
