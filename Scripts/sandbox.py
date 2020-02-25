#!/usr/bin/env python3
# coding: utf-8


"""
Nick Wagner
2/17/20
pycairo test
"""


import math
import cairo
from helpers import *


WIDTH, HEIGHT = 800, 512

surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
ctx = cairo.Context(surface)

# win = Gtk.Window()
# win.connect('destroy', Gtk.main_quit)
# win.set_default_size(450, 550)


## change background color
ctx.rectangle(0, 0, WIDTH, HEIGHT)
ctx.set_source_rgb(1, 1, 1)
ctx.fill()


# not filled rectangle for exons
ctx.rectangle(437,30,473,70)
ctx.set_source_rgb(0,0,0)
ctx.stroke()

# 437.0 30 473.0 70
# 406.5 542 460.5 582
# 379.0 1054 506.0 1094
# 451.0 1566 475.0 1606


# for i in range(1,3):
#     ## drawing line
#     # ctx.move_to(50,i*50)  
#     # ctx.line_to(750,i*50)
#     # ctx.close_path()
#     # ctx.set_source_rgb(0,0,0)
#     # ctx.set_line_width(2)
#     ctx.rectangle(10,(i*50) - 10,50,(i*50) + 10)
#     ctx.set_source_rgb(0,0,0)
#     ctx.stroke()
#     ctx.stroke()


## Drawing rectangle


# ### example curve
# ctx.move_to(0,0)
# # Arc(cx, cy, radius, start_angle, stop_angle)
# # ctx.arc(0.2, 0.1, 0.1, -math.pi / 2, 0)
# ctx.line_to(0.5, 0.1)  # Line to (x,y)
# # Curve(x1, y1, x2, y2, x3, y3)
# ctx.curve_to(0.5, 0.2, 0.5, 0.4, 0.2, 0.8)
# ctx.close_path()
# ctx.set_source_rgb(0.3, 0.2, 0.5)  # Solid color
# ctx.set_line_width(0.02)
# ctx.stroke()

surface.write_to_png('test.png')

LIST_OF_MOTIF_SEQS = ['[tcu]gc[tcu]', 'GCA[UT]G', 'catag', '[TCU][TCU][TCU][TCU][TCU][TCU][TCU][TCU][TCU][TCU]']
LIST_OF_MOTIF_LENGTHS = [4, 5, 5, 10]

# expected = [(0,3),(28,31),(52,55),(7,14),(35,42)]
# test_sequence = "testlsjlongtastcjalkdfjalkfjtestkaslongtastkdalkdjfrtest"
# output = find_motifs(test_sequence, ['test','longtast'])
# print(expected, output[0])



# seq = 'ccctggccccaccacagccccttccccatgacgccgcccccgccccgccccgtactttgcaggtggtaagtttctcagccctggcaggacctgtgtccgccccgttccccctgcgcctgcaggggccacatctccggggcagccccactgcctcctcagcccccacagcccctatagcccccatgccacctccctgccttgataacagtgcctcttgtcctctctggccatagGATAACTGTTCCCCCTCCTCCATCTCTGAGCCCGTGTCACAGGTATCACCCCCTTCTTGCCCTCAGCCCAGCTGCTGTGCCCCTGCCACCCGCGCCCCCTCAGCCCCTTGCGCGTCGCATCCAAGGTcacttgtgctcgcagctccacctggagccgttgccactgctgctgctgcgcttccagtcagggtgggccgctggcctcccactgggcgtcagtttggctcccaggccctgggcagtgccagcctctgggcccgtctgctgcgctgcgttgcgctggctgtgtgctgggctgtctttgctgtggggctgcagtgggggggggcggggtgtctggggacg'
# output = find_motifs(seq,LIST_OF_MOTIF_SEQS,LIST_OF_MOTIF_LENGTHS)
# print(output[0])
# print(output[1])
# print(output[2])



# expected = [18,19,20,21,22,23,24,25,26]
# test_sequence = 'jghfkuurnmfdjdkfndLKJDSFLKJjaskdfjosijd'
# output = find_exons(test_sequence)
# print(expected, output)





