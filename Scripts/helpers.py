#!/usr/bin/env python3
# coding: utf-8

"""
Nick Wagner
2/17/20

File to hold all of the helper functions that assist with parsing 
a fasta file and locating exons and motifs
"""


import re


def find_motifs(sequence, list_of_motif_expressions, list_of_motif_lengths):
    """
    This function is responsible for getting all of the coordinates for each
    of the motifs. It does this by using a sliding window technique for each of
    the motifs and respective lengths. Each time it changes position it uses
    regex to check and see if the current window is equal to the regex expression
    built in motif_mark.py. If the regex returns not NULL then it stores the start,
    stop position as well as what type of motif in a tuple and appends it to a list.

    :param: sequence <string> - one-line sequence from the current
            record in the fasta file
    """
    list_of_motif_coords = []
    list_of_motifs = []
    list_of_counts = []

    for h in range(len(list_of_motif_expressions)):
        motif_length = list_of_motif_lengths[h]
        count = 0
        for i in range(len(sequence) - motif_length + 1):
            current_slice = sequence[i:i+motif_length]

            re_search = re.search(list_of_motif_expressions[h], current_slice)

            if re_search != None:
                current_coordinates = re_search.span()
                list_of_motif_coords.append((i,i+motif_length,h))
                list_of_motifs.append(re_search[0])
                count += 1
        list_of_counts.append(count)
            

    return list_of_motifs, list_of_motif_coords, list_of_counts



def find_exon(sequence):
    """
    This function is responsible for using regex to pull out the
    start and stop positions where the upper case letters are in 
    the sequence line. These upper case letters represent the exon.

    :param: sequence <string> - one-line sequence from the current
            record in the fasta file
    """
    list_of_exon_indexes = []
    count = 0

    re_search = re.search('[A-Z]{2,25000}', sequence)
    list_of_exon_indexes.append(re_search.span())

    return list_of_exon_indexes   