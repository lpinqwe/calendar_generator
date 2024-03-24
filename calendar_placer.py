import create_background
import create_calendar_data
class calendar_placer():
    svg_placer=None
    calendar=None
    def __init__(self):
        self.svg_placer=create_background.Back_creator()
        self.calendar=create_calendar_data.create_calendar_data()
        self.calendar.create_lables()
    def create_calendar(self):
        self.svg_placer.create_back()
        self.svg_placer.shift_precount()
        # calendar_arr = ['                   1', ' 2  3  4  5  6  7  8', ' 9 10 11 12 13 14 15', '16 17 18 19 20 21 22',
        #                '23 24 25 26 27 28 29', '30 31', '']

        calendar_arr = self.calendar.get_month_arr()
        self.svg_placer.preprocess(calendar_arr)
        self.svg_placer.generate_coords()
        self.svg_placer.cell_placer()
        self.svg_placer.place_notes_lines()
        self.svg_placer.place_text_label(f"{self.calendar.get_label()}")

        # calendar_svg.process(calendar_arr)

        self.svg_placer.save_calendar()

calendar_placer_1=calendar_placer()
calendar_placer_1.create_calendar()