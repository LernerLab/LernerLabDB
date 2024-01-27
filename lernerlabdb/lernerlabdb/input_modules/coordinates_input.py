from shiny import *
from lernerlabdb.interface_modules.coordinates import Coordinates


class CoordinatesInput:

    @property
    def title(self):
        title = ui.markdown("#### Coordinates")
        return title

    def single_input_form(self, name, display):
        single_input = ui.input_text(id=name, label=display)
        return single_input

    @property
    def coordinates_input(self):
        input_form = ui.row(
            ui.column(2, self.single_input_form("ap", "AP")),
            ui.column(2, self.single_input_form("ml", "ML")),
            ui.column(2, self.single_input_form("dv", "DV"))
        )
        return input_form

    @property
    def coordinates_input_form(self):
        form = ui.page_fillable(
            self.title,
            self.coordinates_input,
        )
        return form
