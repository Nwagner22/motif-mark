#!/usr/bin/env python3
# coding: utf-8

"""
Nick Wagner
2/17/20

Program to parse fasta files and illustrate motifs
"""

import argparse
from motif_class import *
from helpers import *

def get_args():
    parser = argparse.ArgumentParser(description="A program to parse fasta files and illustrate morifs")
    parser.add_argument("-f", "--fasta", help="use to specify input .fasta file name", required=False, type = str)  
    return parser.parse_args()













# test_class = motif(motif_seq = 'AAAAAA', header="test")

# test_class.test()
