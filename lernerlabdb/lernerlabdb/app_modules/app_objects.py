from lernerlabdb.input_modules.user_input_sidebar import Sidebar
from shiny import *

from lernerlabdb.input_modules.inputs import MouseInput, NoteInput, ProcedureInput, SurgeryInput


class AppUI:
    def __init__(self, sidebar: Sidebar, navigation_cards: NavigationCards):
        self.navigation_cards = navigation_cards
        self.sidebar = sidebar

    @property
    def user_interface(self):
        return ui.page_fluid(
            # shinyswatch.theme.darkly(),
            self.sidebar.sidebar(),
            ui.markdown("---"),
            self.navigation_cards.cards
        )


class AppOutput:
    ...
