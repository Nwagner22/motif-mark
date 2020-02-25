#!/usr/bin/env python3
# coding: utf-8

"""
Nick Wagner
2/17/20

motif class that handles the motif coordinates and exon cooordinates
for illustrating the different motifs per record
"""



class motif:

    header = ""
    sequence = ""
    motif_sequences = []
    motif_coordinates = []
    motif_counts = []
    exon_coordinates = []

    def __init__(self, header, sequence):
        self.header = header
        self.sequence = sequence

    
    def add_exon(self, list_of_coordinates):
        """

        """
        self.exon_coordinates = list_of_coordinates

    def add_motif_coordinates(self, list_of_coordinates):
        """
        
        """
        self.motif_coordinates = list_of_coordinates

    def add_motif_sequences(self, list_of_sequences):
        """
        
        """
        self.motif_sequences = list_of_sequences

    def add_motif_counts(self, list_of_counts):
        """
        
        """
        self.motif_counts = list_of_counts

