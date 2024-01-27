from lernerlabdb.interface_modules.enums import *
from lernerlabdb.input_modules.note_input import NoteInput
from lernerlabdb.interface_modules.enums import BrainStructure

from lernerlabdb.input_modules.structure_input import StructureInput
from shiny import *


class ProcedureInput:

    @property
    def name_input(self):
        name_input = ui.input_text("name", "Procedure Name")
        return name_input

    def add_structure(self):
        pass

    @property
    def procedure_meta_input_layout(self):
        columns = ui.layout_column_wrap(
            self.name_input, width=1/2)
        return columns

    def procedure_input(self):

        procedure_input_form = ui.page_fillable(
            self.procedure_meta_input_layout,
            ui.markdown("---"),
            StructureInput().structure_input_form,
            ui.markdown("---"),
            NoteInput().display_note_input(),
        )

        return procedure_input_form
