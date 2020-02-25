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
    list_of_exon_indexes = []
    count = 0

    re_search = re.search('[A-Z]{2,5000}', sequence)
    list_of_exon_indexes.append(re_search.span())

    # for i in range(len(sequence)):
    #     if sequence[i].isupper() == True:
    #         list_of_exon_indexes.append(i)

    return list_of_exon_indexes



    