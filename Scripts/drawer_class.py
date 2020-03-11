
"""
Nick Wagner
2/17/20

drawer class that handles all of the motif class objects and outputs a svg
file with a drawing illustrating all of the motif findings per record
"""

import cairo
import math
import sys

class drawer:

    list_of_motif_objects = []
    list_of_motifs = []
    width_of_legend = 150
    width = 0
    height = 0
    width_of_motif = 2
    page_height = 150
    number_of_motifs = 0


    def __init__(self, list_of_motif_objects, num_motifs, given_motifs):
        self.list_of_motif_objects = list_of_motif_objects
        self.number_of_motifs = num_motifs
        self.list_of_motifs = given_motifs

    
    def draw(self, output_file):
        """
        This function handles the bulk of the drawing. It starts by changing the
        background color to white. I then create my own custom color pallette depending
        on how many motifs were given. I then create a legend utilizing the color pallette
        and the information about how many motifs were given and their sequences. Then I 
        loop through all of the motif objects and draw their respective sequence line,
        exon, and all of the motifs.

        :param: output_file <string> - string given by the user to specify what the .svg
        output file should be named. DEFALUT: motif_output.svg
        """
        self.calc_width()
        self.calc_height()

        surface = cairo.SVGSurface(output_file, self.width, self.height)
        ctx = cairo.Context(surface)

        ## change background color
        ctx.rectangle(0, 0, self.width, self.height)
        ctx.set_source_rgb(1, 1, 1)
        ctx.fill()

        ## Variables
        line_spacing = 125
        line_depth = 125
        header_depth = 75
        left_spacing = 35

        ## Create custom color palette
        color_palette = [[],[],[]]
        num_colors_per = self.number_of_motifs//3
        max_num_colors_per = self.number_of_motifs - (2 * num_colors_per)
        gradient = 1/num_colors_per
        max_gradient = 1/max_num_colors_per
        # color_gradient_value = 
        for i in range(3):
            if i == 2:
                for k in range(1,max_num_colors_per + 1):
                    color_palette[i].append(k*max_gradient)
            else:
                for k in range(1,num_colors_per + 1):
                    color_palette[i].append(k*gradient)
        # print(max_num_colors_per)
        # print(color_palette)


        ## Legend
        x_legend = self.width - self.width_of_legend
        y_legend = 75
        legend_width = 145
        legend_height = (self.number_of_motifs * 15) + 8
        ctx.rectangle(x_legend,y_legend,legend_width,legend_height)
        ctx.set_source_rgb(0,0,0)
        ctx.stroke()
        legend_line_length = 35
        count = 1
        for i in range(3):
            for j in range(len(color_palette[i])):
                ctx.move_to(x_legend + 5, y_legend + (count*15))
                ctx.line_to(x_legend + legend_line_length, y_legend + (count*15))
                if i == 0:
                    ctx.set_source_rgb(color_palette[i][j],0,0)
                if i == 1:
                    ctx.set_source_rgb(0,color_palette[i][j],0)
                if i == 2:
                    ctx.set_source_rgb(0,0,color_palette[i][j])
                ctx.set_line_width(3)
                ctx.stroke()

                ctx.move_to((x_legend + legend_line_length) + 10, y_legend + (count*15))
                ctx.set_font_size(11)
                ctx.select_font_face("Arial",cairo.FONT_SLANT_NORMAL,cairo.FONT_WEIGHT_NORMAL)
                ctx.set_source_rgb(0,0,0)
                ctx.show_text(self.list_of_motifs[count-1])

                count += 1

        for i in range(len(self.list_of_motif_objects)):
            current_motif_obj = self.list_of_motif_objects[i]
            current_length_of_seq = len(current_motif_obj.sequence)
            current_motif_coords = current_motif_obj.motif_coordinates
            current_motif_sequences = current_motif_obj.motif_sequences
            current_exon_coords = current_motif_obj.exon_coordinates

            width_left = self.width - current_length_of_seq - self.width_of_legend
            
            ## Draw main sequence line
            ctx.move_to(left_spacing,(i*line_spacing) + line_depth)  
            ctx.line_to(left_spacing + current_length_of_seq,(i*line_spacing) + line_depth)
            ctx.set_source_rgb(0,0,0)
            ctx.set_line_width(2)
            ctx.stroke()

            ## Draw the exon
            x1 = left_spacing + current_exon_coords[0][0]
            y1 = (i*line_spacing) + line_depth - 20
            rec_width = current_exon_coords[0][1] - current_exon_coords[0][0]
            rec_height = 40
            ctx.rectangle(x1,y1,rec_width,rec_height)
            ctx.set_source_rgb(0,0,0)
            ctx.stroke()

            ## Loop to draw all motifs
            for j in range(len(current_motif_coords)):
                ctx.move_to(left_spacing + current_motif_coords[j][0],(i*line_spacing) + line_depth)  
                ctx.line_to(left_spacing + current_motif_coords[j][0] + 2,(i*line_spacing) + line_depth)
                motif_num = current_motif_coords[j][2]
                if(motif_num < num_colors_per):
                    ctx.set_source_rgb(color_palette[0][motif_num],0,0)
                if(motif_num >= num_colors_per and motif_num < (2*num_colors_per)):
                    ctx.set_source_rgb(0,color_palette[1][motif_num-num_colors_per],0)
                if(motif_num >= (2*num_colors_per)):
                    ctx.set_source_rgb(0,0,color_palette[2][motif_num-(2*num_colors_per)])
                ctx.set_line_width(15)
                ctx.stroke()

            ## adding header text
            ctx.move_to(left_spacing, (i*line_spacing) + header_depth)
            ctx.set_font_size(17)
            ctx.select_font_face("Arial",cairo.FONT_SLANT_NORMAL,cairo.FONT_WEIGHT_NORMAL)
            ctx.set_source_rgb(0,0,0)
            ctx.show_text(current_motif_obj.header)

            # ## adding sequence text (MAYBE MAKE THIS OPTIONAL FLAG?)
            # disp_length = 80
            # last_k = 0
            # for k in range(len(current_motif_obj.sequence)//disp_length):
            #     current_seq = current_motif_obj.sequence[k*disp_length:(k*disp_length)+disp_length]
            #     ctx.move_to(50, (i*512) + 125 + (25*k))
            #     ctx.set_font_size(14)
            #     ctx.select_font_face("Arial",cairo.FONT_SLANT_NORMAL,cairo.FONT_WEIGHT_NORMAL)
            #     ctx.set_source_rgb(0,0,0)
            #     ctx.show_text(current_seq)
            #     last_k = k
            # final_num = ((len(current_motif_obj.sequence)//disp_length)*disp_length)
            # the_rest = current_motif_obj.sequence[final_num:]
            # ctx.move_to(50, (i*512) + 125 + (25*(last_k + 1)))
            # ctx.set_font_size(14)
            # ctx.select_font_face("Arial",cairo.FONT_SLANT_NORMAL,cairo.FONT_WEIGHT_NORMAL)
            # ctx.set_source_rgb(0,0,0)
            # ctx.show_text(the_rest)



        surface.finish()



    def calc_width(self):
        """
        This function calculates the width of the page by looping through
        all of the motif objects and figuring out the longest sequence.
        It also adds extra space for clarity as well as space for the
        width of the legend.
        """
        current_longest = 0

        for i in range(len(self.list_of_motif_objects)):
            current_object = self.list_of_motif_objects[i]
            if(len(current_object.sequence) > current_longest):
                current_longest = len(current_object.sequence)
        
        width_for_drawing = current_longest + 50 + 15 

        self.width = width_for_drawing + self.width_of_legend


    def calc_height(self):
        """
        This function calculates the height of the page by multiplying
        the number of records by the designated height per record listed
        at the top of the class
        """
        num_records = len(self.list_of_motif_objects)

        self.height = num_records * self.page_height