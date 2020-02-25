#!/usr/bin/env python3
# coding: utf-8

"""
Nick Wagner
2/17/20

Program to parse fasta files and illustrate motifs
"""

import sys
import argparse
from motif_class import *
from drawer_class import *
from helpers import *

def get_args():
    parser = argparse.ArgumentParser(description="A program to parse fasta files and illustrate morifs")
    parser.add_argument("-f", "--fasta", help="use to specify input .fasta file name. Required to be in two-line fasta format", required=True, type = str)  
    parser.add_argument("-m", "--motif", help="use to specify file that contains all of the desired motifs", required=True, type = str)  
    return parser.parse_args()

args = get_args()
FASTA_FILE = args.fasta
MOTIF_FILE = args.motif
LIST_OF_GIVEN_MOTIF_EXPRESSIONS = []
LIST_OF_GIVEN_MOTIF_LENGTHS = []
LIST_OF_MOTIF_OBJECTS = []
NUMBER_OF_MOTIFS = 0

nucleac_acid_dict = {'y':'[tcu]', 'Y':'[TCU]', 'U':'[UT]', 'u':'[ut]',
                     's':'[cg]', 'S':'[CG]', 'm':'[ac]', 'M':'[AC]',
                     'k':'[gtu]', 'K':'[GTU]', 'r':'[ag]', 'R':'[AG]',
                     'w':'[atu]', 'W':'[ATU]'}

with open(MOTIF_FILE, 'r') as motifFile:
    for line in motifFile:
        line = line.strip()

        current_length = len(line)

        current_motif = ""
        for letter in line:
            if letter == 'y':
                current_motif += nucleac_acid_dict['y']
            elif letter == 'Y':
                current_motif += nucleac_acid_dict['Y']
            elif letter == 'U':
                current_motif += nucleac_acid_dict['U']
            elif letter == 'u':
                current_motif += nucleac_acid_dict['u']
            elif letter == 's':
                current_motif += nucleac_acid_dict['s']
            elif letter == 'S':
                current_motif += nucleac_acid_dict['S']
            elif letter == 'm':
                current_motif += nucleac_acid_dict['m']
            elif letter == 'M':
                current_motif += nucleac_acid_dict['M']
            elif letter == 'k':
                current_motif += nucleac_acid_dict['k']
            elif letter == 'K':
                current_motif += nucleac_acid_dict['K']
            elif letter == 'r':
                current_motif += nucleac_acid_dict['r']
            elif letter == 'R':
                current_motif += nucleac_acid_dict['R']
            elif letter == 'w':
                current_motif += nucleac_acid_dict['w']
            elif letter == 'W':
                current_motif += nucleac_acid_dict['W']
            else:
                current_motif += letter

        LIST_OF_GIVEN_MOTIF_EXPRESSIONS.append(current_motif)
        LIST_OF_GIVEN_MOTIF_LENGTHS.append(current_length)
        NUMBER_OF_MOTIFS += 1


# Loop through the fasta file and create a motif object for each record
# This loop utilizes functions from the helpers.py file to get all of the
# information about motifs and exons
with open(FASTA_FILE, 'r') as fastaFile:
    count = 0
    for line in fastaFile:
        if(line[0] == '>'):  # header line, grab whole record
            header = line.strip()
            sequence = fastaFile.readline().strip()
            current_motif_object = motif(header,sequence)
            
            motif_output = find_motifs(sequence, LIST_OF_GIVEN_MOTIF_EXPRESSIONS,LIST_OF_GIVEN_MOTIF_LENGTHS)
            exon_coordinates = find_exon(sequence)

            current_motif_object.add_motif_sequences(motif_output[0])
            current_motif_object.add_motif_coordinates(motif_output[1])
            current_motif_object.add_motif_counts(motif_output[2])
            current_motif_object.add_exon(exon_coordinates)

            LIST_OF_MOTIF_OBJECTS.append(current_motif_object)

            count += 1


drawer_object = drawer(LIST_OF_MOTIF_OBJECTS, NUMBER_OF_MOTIFS)
drawer_object.draw()

# print(LIST_OF_MOTIF_OBJECTS[0].exon_coordinates)
# print(LIST_OF_MOTIF_OBJECTS[1].exon_coordinates)
# print(LIST_OF_MOTIF_OBJECTS[2].exon_coordinates)
# print(LIST_OF_MOTIF_OBJECTS[3].exon_coordinates)

# print("")

# print(LIST_OF_MOTIF_OBJECTS[0].motif_coordinates)
# print(LIST_OF_MOTIF_OBJECTS[1].motif_coordinates)
# print(LIST_OF_MOTIF_OBJECTS[2].motif_coordinates)
# print(LIST_OF_MOTIF_OBJECTS[3].motif_coordinates)











# test_class = motif(motif_seq = 'AAAAAA', header="test")

# test_class.test()
