import numpy as np
from shiny import App, Inputs, Outputs, Session, reactive, req, ui, render
from lernerlabdb.input_modules import StructureInput, NoteInput, ProcedureInput


class AppUI():
    @property
    def app_ui(self):
        app_ui_page = ui.page_fluid(
            ui.input_select("numb_structures", "Number of structures in procedure",
                            choices=[i for i in range(1, 11, 1)]
                            ),
            ui.output_ui('procedure_structures_columns')

        )
        return app_ui_page


def server(input: Inputs, output: Outputs, session: Session):
    @render.ui
    def procedure_structures_columns():
        number_of_structure_inputs = int(input.numb_structures())
        columns = [StructureInput().structure_input_form(numb)
                   for numb in range(number_of_structure_inputs)
                   ]
        input_columns = ui.TagList(ui.layout_columns(*columns))
        return input_columns


app_ui = AppUI().app_ui
app = App(app_ui, server)
