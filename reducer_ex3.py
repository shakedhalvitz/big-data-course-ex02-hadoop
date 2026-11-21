#!/usr/bin/env python3
"""reducer_ex3.py"""

from itertools import groupby
from operator import itemgetter
import sys

def read_mapper_output(file, separator='\t'):
    for line in file:
        yield line.rstrip().split(separator, 1)

def main(separator='\t'):
    # input comes from STDIN (standard input)
    data = read_mapper_output(sys.stdin, separator=separator)
    results = []
    # groupby groups multiple word-count pairs by word,
    # and creates an iterator that returns consecutive keys and their group:
    #   current_word - string containing a word (the key)
    #   group - iterator yielding all [current_word, count] items
    for current_word, group in groupby(data, itemgetter(0)):
        try:
            total_count = sum(int(count) for current_word, count in group)
            results.append((total_count, current_word))
        except ValueError:
            # count was not a number, so silently discard this item
            pass

    # sort by count descending and print only the top 3 words
    results.sort(reverse=True)
    for count, word in results[:3]:
        print("%s%s%d" % (word, separator, count))

if __name__ == "__main__":
    main()