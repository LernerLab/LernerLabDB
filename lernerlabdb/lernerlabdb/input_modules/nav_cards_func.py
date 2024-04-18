from shiny import *
from lernerlabdb.input_modules import MouseInput, ProcedureInput, SurgeryInput


""" side bar functions """


def sidebar():
    title = ui.markdown(
        text="# User Info",
    )
    input_date = ui.input_date("date", "Date",
                               format="mm/dd/yy",
                               autoclose=True)
    user_info = ui.page_fillable(
        ui.input_text("name", "Name (Enter as: First Last)"),
        ui.input_text("netid", "NetID"),
        ui.br(),
        ui.br(),

    )
    submit_button = ui.input_action_button("submit", "Submit")

    user_info_sidebar = ui.page_sidebar(

        ui.sidebar(
            title,
            input_date,
            user_info,
            submit_button,
        )
    )
    return user_info_sidebar


""" navigation card functions """


def create_mouse_panel(mouse_input: MouseInput):
    mouse_panel = ui.nav_panel(
        "Mouse",
        mouse_input.mouse_input()
    )
    return mouse_panel


def create_surgery_panel(surgery_input: SurgeryInput):
    surgery_panel = ui.nav_panel(
        "Surgery",
        surgery_input.surgery_input()
    )
    return surgery_panel


def create_procedure_panel(procedure_input: ProcedureInput):
    procedure_panel = ui.nav_panel(
        "Procedure",
        procedure_input.procedure_input()
    )
    return procedure_panel


def create_navigation_cards(mouse_panel, surgery_panel, procedure_panel):
    navigation_cards = ui.navset_underline(
        mouse_panel,
        surgery_panel,
        procedure_panel
    )
    return navigation_cards
