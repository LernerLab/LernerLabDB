import numpy as np
from shiny import App, Inputs, Outputs, Session, reactive, req, ui, render
from lernerlabdb.input_modules import StructureInput, NoteInput, ProcedureInput


class AppUI(Inputs):
    @property
    def app_ui(self):
        app_ui_page = ui.page_fluid(
            ui.input_select("numb_structures", "Number of structures in procedure",
                            choices=[i for i in range(1, 11, 1)]
                            ),
            ui.br(),
            ui.output_ui('structure')

        )
        return app_ui_page


def server(input, output, session):
    @render.ui
    def structure():
        numb_structs = int(input.numb_structures())
        procedure_input = ProcedureInput(numb_structs)
        return procedure_input.procedure_input()


app_ui = AppUI.app_ui
app = App(app_ui, server)
