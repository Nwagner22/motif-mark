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
        function to add the exon coordinates to the class object

        :param: list_of_coordinates <list> - list that contains a tuple that
                corresponds to the start and stop positions for the exon (start,stop)
                (list because I thought there were multiple exons per record at first)
        """
        self.exon_coordinates = list_of_coordinates

    def add_motif_coordinates(self, list_of_coordinates):
        """
        function to add the list of motif coordinates to the class object

        :param: list_of_coordinates <list> - list that contains tuples corresponding
                to each of the motifs in a given record (start,stop,motif_type)
        """
        self.motif_coordinates = list_of_coordinates

    def add_motif_sequences(self, list_of_sequences):
        """
        function to add the list of motif sequences to the class object

        :param: list_of_sequences <list> - list that contains all of the given
                motif sequences read from the file
        """
        self.motif_sequences = list_of_sequences

    def add_motif_counts(self, list_of_counts):
        """
        function to add the list of motif counts to the class object

        :param: list_of_counts <list> - list that contains an integer value for how
                many times each of the motifs was seen in the record
        """
        self.motif_counts = list_of_counts

