
from lernerlabdb.interface_modules.enums import *
from typing import List

from lernerlabdb.input_modules import *
from shiny import *

import shinyswatch
from abc import ABC, abstractmethod

# create sidebar
# sidebar = sidebar()

# create input panels
mouse_input = MouseInput()
surgery_input = SurgeryInput()
procedure_input = ProcedureInput()
notes_input = NoteInput()

# create navigation panels
mouse_panel = create_mouse_panel(mouse_input)
surgery_panel = create_surgery_panel(surgery_input)
procedure_panel = create_procedure_panel(procedure_input)

# create navigation cards
navigation_cards = create_navigation_cards(
    mouse_panel=mouse_panel,
    surgery_panel=surgery_panel,
    procedure_panel=procedure_panel
)

# create user


app_ui = ui.page_fluid(

    # shinyswatch.theme_picker_ui,
    shinyswatch.theme.minty,
    ui.markdown("# LernerLab"),
    # ui.input_action_button('click_me', "Click me!"),
    # ui.output_ui('say_thanks')
    ui.markdown("---"),
    navigation_cards,
    notes_input.display_note_input()
)

# default at 0/1 use reactive event to update ui.input
# app_ui = create_user_interface(sidebar, navigation_cards)


def server(input: Inputs, output: Outputs, session: Session):

    # @render.ui
    # @reactive.event(input.click_me)
    # def say_thanks():
    #     return ui.markdown("# Thanks!!")

    # shinyswatch.theme_picker_server()

    @render.ui
    def procedure_structures_columns():
        number_of_structure_inputs = int(input.numb_structures())
        columns = [StructureInput().structure_input_form(numb)
                   for numb in range(number_of_structure_inputs)
                   ]
        input_columns = ui.TagList(ui.layout_columns(*columns))
        return input_columns


app = App(app_ui, server)
