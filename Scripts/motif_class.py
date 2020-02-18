#!/usr/bin/env python
# coding: utf-8

"""
Nick Wagner
2/17/20

motif class that handles the motif coordinates and exon cooordinates
for illustrating the different motifs per record
"""

import cairo


class motif:

    header = ""
    motif_sequence = ""
    motif_coordinates = []
    exon_coordinates = []
    motif_count = 0

    def __init__(self, motif_seq, header):
        self.motif_sequence = motif_seq
        self.header = header

    

    def add_exon(self):
        pass


    def add_motif(self):
        pass


    def draw(self):
        pass

    def test(self):
        print(self.motif_sequence)


