import create_background
import create_calendar_data


class calendar_placer():
    svg_placer = None
    calendar = None

    def __init__(self):
        self.svg_placer = create_background.Back_creator()
        self.calendar = create_calendar_data.create_calendar_data()
        self.calendar.create_lables()

    def create_year_calendar(self, year):
        for i in range(1, 12):
            self.calendar = create_calendar_data.create_calendar_data()
            self.calendar.set_data(i,year)
            self.calendar.create_lables()
            self.svg_placer = create_background.Back_creator(f"new_dir/{self.calendar.get_label()}.svg")
            self.svg_placer.set_filename(f"new_dir/{self.calendar.get_label()}.svg")
            self.svg_placer.create_back()
            self.svg_placer.shift_precount()
            calendar_arr = self.calendar.get_month_arr()
            self.svg_placer.preprocess(calendar_arr)
            self.svg_placer.generate_coords()
            self.svg_placer.cell_placer()
            self.svg_placer.place_notes_lines()
            self.svg_placer.place_text_label(f"{self.calendar.get_label()}")
            self.svg_placer.set_filename(self.calendar.get_label())
            self.svg_placer.save_calendar()

    def create_calendar(self):
        self.svg_placer.create_back()
        self.svg_placer.shift_precount()
        calendar_arr = self.calendar.get_month_arr()
        self.svg_placer.preprocess(calendar_arr)
        self.svg_placer.generate_coords()
        self.svg_placer.cell_placer()
        self.svg_placer.place_notes_lines()
        self.svg_placer.place_text_label(f"{self.calendar.get_label()}")
        self.svg_placer.set_filename(self.calendar.get_label())
        self.svg_placer.save_calendar()
