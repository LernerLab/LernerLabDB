
from lernerlabdb.interface_modules.enums import *
from lernerlabdb.input_modules.note_input import NoteInput

from shiny import *


class MouseInput:

    @property
    def dob_selector(self):
        dob_selector = ui.input_date("dob", "Date of Birth",
                                     format="mm/dd/yy",
                                     autoclose=True)
        return dob_selector

    @property
    def ear_tag_input(self):
        ear_tag_input = ui.input_text("ear_tag", "Ear Tag")
        return ear_tag_input

    @property
    def genotype_selector(self):
        genotype_selector = ui.input_selectize(
            "genotype", "Genotype", choices=[v.value for v in Genotype])
        return genotype_selector

    @property
    def status_selector(self):
        status_selector = ui.input_switch(
            "status", "Dead")
        return status_selector

    @property
    def sex_radio(self):
        sex_radio = ui.input_radio_buttons(
            "sex", label="Sex", choices=[s.value for s in Sex])
        return sex_radio

    @property
    def zygosity_selector(self):
        selector = ui.input_selectize(
            "zygosity", "Zygosity", choices=[v.value for v in Zygosity])
        return selector

    @property
    def column_layout(self):
        columns = ui.layout_column_wrap(
            (self.status_selector, self.dob_selector,
             self.sex_radio, self.ear_tag_input),
            (self.genotype_selector, self.zygosity_selector),
            width=1/4)

        return columns

    def mouse_input(self):

        mouse_button = ui.input_action_button("mouse_input", "Add Mouse")

        mouse_form = ui.page_fillable(
            self.column_layout,
            ui.markdown("---"),
            NoteInput().display_note_input(),
            mouse_button)

        return mouse_form
