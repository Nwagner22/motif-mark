#!/usr/bin/env python3
# coding: utf-8


"""
Nick Wagner
2/17/20

File to hold all of the helper functions that assist with parsing 
a fasta file and locating exons and motifs
"""






def find_motifs(sequence, motif_seq):
    list_of_motifs = []

    motif_length = len(motif_seq)
    count = 0
    for i in range(len(sequence) - motif_length + 1):
        current_slice = sequence[i:i+motif_length]
        if current_slice == motif_seq:
            current_coordinates = (i,i + motif_length - 1)
            list_of_motifs.append(current_coordinates)
            count += 1
            

    return list_of_motifs, count



def find_exons(sequence):
    list_of_exon_indexes = []
    count = 0

    for i in range(len(sequence)):
        if sequence[i].isupper() == True:
            list_of_exon_indexes.append(i)

    return list_of_exon_indexes



    