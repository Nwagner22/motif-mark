
import cairo

class drawer:

    list_of_motif_objects = []
    width = 0
    height = 0
    width_of_motif = 2
    page_height = 150
    number_of_motifs = 0


    def __init__(self, list_of_motif_objects, num_motifs):
        self.list_of_motif_objects = list_of_motif_objects
        self.number_of_motifs = num_motifs

    
    def draw(self):
        self.calc_width()
        self.calc_height()

        surface = cairo.SVGSurface("motifs.svg", self.width, self.height)
        ctx = cairo.Context(surface)

        ## change background color
        ctx.rectangle(0, 0, self.width, self.height)
        ctx.set_source_rgb(1, 1, 1)
        ctx.fill()

        ## Variables
        line_spacing = 125
        line_depth = 125
        header_depth = 75

        ## Legend
        ctx.rectangle((self.width/2) + 100, 15, 200, 50)
        ctx.set_source_rgb(0,0,0)
        ctx.set_line_width(1)
        ctx.stroke()


        for i in range(len(self.list_of_motif_objects)):
            current_motif_obj = self.list_of_motif_objects[i]
            current_length_of_seq = len(current_motif_obj.sequence)
            current_motif_coords = current_motif_obj.motif_coordinates
            current_motif_sequences = current_motif_obj.motif_sequences
            current_exon_coords = current_motif_obj.exon_coordinates

            width_left = self.width - current_length_of_seq
            
            ## Draw main sequence line
            ctx.move_to(width_left/2,(i*line_spacing) + line_depth)  
            ctx.line_to((width_left/2) + current_length_of_seq,(i*line_spacing) + line_depth)
            ctx.set_source_rgb(0,0,0)
            ctx.set_line_width(2)
            ctx.stroke()

            ## Draw the exon
            # ctx.move_to((width_left/2) + current_exon_coords[0][0],(i*512) + 50)  
            # ctx.line_to((width_left/2) + current_exon_coords[0][1],(i*512) + 50)
            # ctx.set_source_rgb(0,0,0)
            # ctx.set_line_width(30)
            x1 = (width_left/2) + current_exon_coords[0][0]
            y1 = (i*line_spacing) + line_depth - 20
            rec_width = current_exon_coords[0][1] - current_exon_coords[0][0]
            rec_height = 40
            ctx.rectangle(x1,y1,rec_width,rec_height)
            ctx.set_source_rgb(0,0,0)
            ctx.stroke()

            ## Loop to draw all motifs
            for j in range(len(current_motif_coords)):
                ctx.move_to((width_left/2) + current_motif_coords[j][0],(i*line_spacing) + line_depth)  
                ctx.line_to((width_left/2) + current_motif_coords[j][0] + 2,(i*line_spacing) + line_depth)
                if(current_motif_coords[j][2] == 0):
                    ctx.set_source_rgb(0,0,255)
                if(current_motif_coords[j][2] == 1):
                    ctx.set_source_rgb(0,255,0)
                if(current_motif_coords[j][2] == 2):
                    ctx.set_source_rgb(1,.6,0)
                if(current_motif_coords[j][2] == 3):
                    ctx.set_source_rgb(255,0,0)
                ctx.set_line_width(15)
                ctx.stroke()

            ## adding header text
            ctx.move_to(50, (i*line_spacing) + header_depth)
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

        current_longest = 0

        for i in range(len(self.list_of_motif_objects)):
            current_object = self.list_of_motif_objects[i]
            if(len(current_object.sequence) > current_longest):
                current_longest = len(current_object.sequence)

        self.width = current_longest + 50 + 50


    def calc_height(self):
        num_records = len(self.list_of_motif_objects)

        self.height = num_records * self.page_height