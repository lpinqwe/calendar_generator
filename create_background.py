import re

import svgwrite as svg
import svgwrite.gradients

import class_cell


class Back_creator:
    width, heigth = [500, 250]
    pkt_begin = [20, 50]
    current_place_x = 0
    current_place_y = 0
    current_elem = 0
    shift = [0, 0]
    dict_coords = {0: [pkt_begin[0], pkt_begin[1]]}
    current_elem_y = 1
    dwg = ''
    filename = 'default.svg'
    def set_filename(self,text):
        self.filename=text
    def generate_coords(self):
        for i in range(1, 32):
            self.dict_coords[i] = [self.current_elem * self.shift[0] + self.dict_coords[0][0],
                                   self.current_elem_y * self.shift[1] + self.dict_coords[0][1]]
            self.current_elem += 1
            if (self.current_elem >= 8):
                self.current_elem = 1
                self.current_elem_y += 1
        print(self.dict_coords)

    def __init__(self,filename=filename):
        self.dwg = svg.Drawing(width=self.width, height=self.heigth, filename=filename,
                               size=(self.width, self.heigth))

    def create_back(self):
        gradient = svgwrite.gradients.LinearGradient(id="grad", start=(0, 0), end=(1, 1))
        # gradient.add_stop_color(offset='0%', color='red')
        gradient.add_stop_color(offset='0%', color='red')
        gradient.add_stop_color(offset='100%', color='yellow')
        self.dwg.defs.add(gradient)
        self.dwg.add(self.dwg.rect((0, 0), (self.width, self.heigth), fill='url(#grad)', stroke='none'))

    def shift_precount(self):
        cell = class_cell.Cell(1, 1, '', '10', (1, 1))
        self.shift = cell.rozm_count()
        print(f"precount shape_shift:{self.shift}")

    def cell_placer(self):
        for i in range(1, 32):
            cell = class_cell.Cell(self.dict_coords[i][0], self.dict_coords[i][1], self.dwg, str(i),
                                   (self.width, self.heigth))
            cell.rozm_count()
            cell.plase()

    def place_notes_lines(self):
        for i in range(1, 32, 7):
            print(f"{(self.dict_coords[i][0], self.dict_coords[i][1])}")
            self.dwg.add(self.dwg.line((self.dict_coords[i][0] + 100, self.dict_coords[i][1]),
                                       (self.dict_coords[i][0] + 300, self.dict_coords[i][1]),
                                       stroke=svgwrite.rgb(0, 0, 0), stroke_width="1"))
    def place_text_label(self,text):
        self.dwg.add(self.dwg.text(text,insert=(self.width//2-len(text)*10,30)))
    def cell_generator(self, arr='none'):
        arr = arr.strip()

        # if(len(arr)<2):
        #    arr=" "+arr
        # print(arr)
        begin_point_x, begin_point_y = self.pkt_begin[0], self.pkt_begin[1]
        x_point = begin_point_x + self.current_place_x  # * self.shift[0]
        y_point = begin_point_y + self.current_place_y  # * self.shift[1]

        print(
            f"elem:{arr},place current_elem:{self.current_elem},"
            f"current_place_x:{self.current_place_x},current_place_y:{self.current_place_y}"
            f",x_point:{x_point},y_point{y_point}")
        cell = class_cell.Cell(x_point, y_point, self.dwg, arr, (self.width, self.heigth))
        self.shift = cell.rozm_count()
        print(f"self.shift:{self.shift}")
        cell.string = arr
        cell.plase()
        if (self.current_elem <= 6):
            self.current_elem += 1
        else:
            print("HERE")
            self.current_elem = 1
            self.current_place_y += self.shift[1]
            self.current_place_x = begin_point_x
        self.current_place_x += self.shift[0]

    def save_calendar(self):
        self.dwg.save()

    def preprocess(self, arr):
        pattern = r'\s\w'
        self.current_place_x = self.current_elem = 7 - len(re.findall(pattern, arr[0]))

    def process(self, arr):
        pattern = r'\s\w'
        for i in range(len(arr)):
            self.current_place_x = self.current_elem = 7 - len(re.findall(pattern, arr[i]))
            new_arr = arr[i].split(" ")

            for ii in new_arr:
                if (ii == ''):
                    continue
                self.cell_generator(ii)

'''
calendar_svg = Back_creator()
calendar_svg.create_back()
calendar_svg.shift_precount()
# calendar_arr = ['                   1', ' 2  3  4  5  6  7  8', ' 9 10 11 12 13 14 15', '16 17 18 19 20 21 22',
#                '23 24 25 26 27 28 29', '30 31', '']

calendar_arr = ['    January 2019', 'Mo Tu We Th Fr Sa Su', '    1  2  3  4  5  6', ' 7  8  9 10 11 12 13',
                '14 15 16 17 18 19 20', '21 22 23 24 25 26 27', '28 29 30 31', '']
calendar_svg.preprocess(calendar_arr)
calendar_svg.generate_coords()
calendar_svg.cell_placer()
calendar_svg.place_notes_lines()
calendar_svg.place_text_label("dadada")

# calendar_svg.process(calendar_arr)

calendar_svg.save_calendar()
'''