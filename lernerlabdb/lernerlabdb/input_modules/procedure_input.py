from lernerlabdb.interface_modules.enums import *
from lernerlabdb.input_modules.note_input import NoteInput
from lernerlabdb.interface_modules.enums import BrainStructure
from shiny import *


class ProcedureInput:

    @property
    def name_input(self):
        name_input = ui.input_text("name", "Name")
        return name_input

    @property
    def structure(self):
        structure_choices = [s.value for s in BrainStructure]
        selector = ui.input_selectize(
            "structure", "Structure", choices=structure_choices)

        return selector

    @property
    def column_layout(self):
        columns = ui.layout_column_wrap(
            (self.name_input),
            (self.structure),
            width=1/2)

        return columns

    def procedure_input(self):

        procedure_input_form = ui.page_fillable(
            self.column_layout,
            ui.markdown("---"),
            NoteInput().display_note_input(),
        )

        return procedure_input_form
