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


# WIDTH, HEIGHT = 256, 256

# surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
# ctx = cairo.Context(surface)

# # win = Gtk.Window()
# # win.connect('destroy', Gtk.main_quit)
# # win.set_default_size(450, 550)


# ## change background color
# ctx.rectangle(0, 0, WIDTH, HEIGHT)
# ctx.set_source_rgb(1, 1, 1)
# ctx.fill()

# ## drawing line
# ctx.move_to(10,10)     # have to convert coordinates to values between 0 and 1
# ctx.line_to(50,10)
# # ctx.close_path()
# ctx.set_source_rgb(255,0,0)
# ctx.set_line_width(2)
# ctx.stroke()


# ## Drawing rectangle


# # ### example curve
# # ctx.move_to(0,0)
# # # Arc(cx, cy, radius, start_angle, stop_angle)
# # # ctx.arc(0.2, 0.1, 0.1, -math.pi / 2, 0)
# # ctx.line_to(0.5, 0.1)  # Line to (x,y)
# # # Curve(x1, y1, x2, y2, x3, y3)
# # ctx.curve_to(0.5, 0.2, 0.5, 0.4, 0.2, 0.8)
# # ctx.close_path()
# # ctx.set_source_rgb(0.3, 0.2, 0.5)  # Solid color
# # ctx.set_line_width(0.02)
# # ctx.stroke()

# surface.write_to_png('test.png')




# expected = [(0,3),(28,31),(52,55)]
# test_sequence = "testlsjflkneakdcjalkdfjalkfjtestkasdjfksdjfkdalkdjfrtest"
# output = find_motifs(test_sequence, 'test')
# print(expected, output[0])



expected = [18,19,20,21,22,23,24,25,26]
test_sequence = 'jghfkuurnmfdjdkfndLKJDSFLKJjaskdfjosijd'
output = find_exons(test_sequence)
print(expected, output)





