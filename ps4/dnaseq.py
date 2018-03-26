#!/usr/bin/env python2.7

import unittest
from dnaseqlib import *

### Utility classes ###

# Maps integer keys to a set of arbitrary values.
class Multidict:
    # Initializes a new multi-value dictionary, and adds any key-value
    # 2-tuples in the iterable sequence pairs to the data structure.
    def __init__(self, pairs=[]):
        self.dict = dict()
        if pairs:
            for pair in pairs:
                key, value = pair[0], pair[1]
                self.put(key, value)

    # Associates the value v with the key k.
    def put(self, k, v):
        if k in self.dict:
            self.dict[k].append(v)
        else:
            self.dict[k] = [v]
    
    # Gets any values that have been associated with the key k; or, if
    # none have been, returns an empty sequence.
    def get(self, k):
        if k in self.dict:
            return self.dict[k]
        else:
            return []

# Given a sequence of nucleotides, return all k-length subsequences
# and their hashes.  (What else do you need to know about each
# subsequence?)
def subsequenceHashes(seq, k):
    subseq = ''
    while len(subseq) < k:
        new_c = next(seq)
        subseq += new_c
    rh = RollingHash(subseq)
    pos = 0
    try:
        while True:
            if len(subseq) < k:
                new_c = next(seq)
                subseq += new_c
                pos += 1
                rh.slide(prev_letter, new_c)
            yield rh.current_hash(), (subseq, pos)
            prev_letter = subseq[0]
            subseq = subseq[1:]
    except StopIteration:
        return

# Similar to subsequenceHashes(), but returns one k-length subsequence
# every m nucleotides.  (This will be useful when you try to use two
# whole data files.)
def intervalSubsequenceHashes(seq, k, m):
    try:
        pos = 0
        while True:
            subseq = ''
            for i in range(k):
                subseq += next(seq)
            rh = RollingHash(subseq)
            yield rh.current_hash(), (subseq, pos)
            # jump to m
            for _ in range(k, m):
                pos += 1
    except StopIteration:
        return

# Searches for commonalities between sequences a and b by comparing
# subsequences of length k.  The sequences a and b should be iterators
# that return nucleotides.  The table is built by computing one hash
# every m nucleotides (for m >= k).
def getExactSubmatches(a, b, k, m):
    if k <= m:
        table = Multidict(intervalSubsequenceHashes(a, k, m))
    else:
        table = Multidict(subsequenceHashes(a, k))
    for b_hash, (b_sub, b_pos) in subsequenceHashes(b, k):
        for a_match in table.get(b_hash):
            if a_match[0] == b_sub:
                yield a_match[1], b_pos

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print('Usage: {0} [file_a.fa] [file_b.fa] [output.png]'.format(sys.argv[0]))
        sys.exit(1)

    # The arguments are, in order: 1) Your getExactSubmatches
    # function, 2) the filename to which the image should be written,
    # 3) a tuple giving the width and height of the image, 4) the
    # filename of sequence A, 5) the filename of sequence B, 6) k, the
    # subsequence size, and 7) m, the sampling interval for sequence
    # A.
    compareSequences(getExactSubmatches, sys.argv[3], (500,500), sys.argv[1], sys.argv[2], 8, 100)
