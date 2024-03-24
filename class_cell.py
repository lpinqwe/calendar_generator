class Cell():
    string = None
    x = None
    y = None
    x_frame_y_frame = [None, None]
    len_x_frame_len_y_frame = [None, None]
    x_text_y_text = [None, None]
    dwg = None
    width, heigth = [None, None]

    def __init__(self, x_place_point, y_place_point, dwg, text, rozmiary):
        self.x = x_place_point
        self.y = y_place_point
        self.dwg = dwg
        self.width, self.heigth = rozmiary
        self.string = text
        if (len(self.string) <= 1):
            self.string=f" {text}"

    def rozm_count(self):
        a = len(self.string) * 7 + 12
        self.len_x_frame_len_y_frame = [a, 20]
        self.x_frame_y_frame = [self.x - 4, self.y - 15]
        self.x_text_y_text = [self.x, self.y]
        return self.len_x_frame_len_y_frame

    def plase(self):
        self.add_text()
        self.add_cell_figure()

    def add_text(self):
        self.dwg.add(self.dwg.text(self.string, insert=(self.x_text_y_text[0], self.x_text_y_text[1])))

    def add_cell_figure(self):
        self.dwg.add(self.dwg.rect(self.x_frame_y_frame, self.len_x_frame_len_y_frame, fill='none', stroke='black',
                                   stroke_width=1))

    def add_rect_with_text(self):
        for i in range(len(self.string)):
            x = len(self.string[i]) - 2
            y = 1
            self.add_text()
            self.add_cell_figure()

    def add_text_line(self):
        None