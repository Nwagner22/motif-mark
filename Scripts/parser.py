"""
Nick Wagner
2/17/20

Program to parse fasta files and illustrate motifs
"""

import argparse
from motif_class import *

def get_args():
    parser = argparse.ArgumentParser(description="A program to convert FASTA files into two lines per record")
    parser.add_argument("-f", "--fasta", help="use to specify input .fasta file name", required=False, type = str)  
    return parser.parse_args()


test_class = motif(motif_seq = 'AAAAAA', header="test")

test_class.test()
