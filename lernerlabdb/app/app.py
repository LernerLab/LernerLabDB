from lernerlabdb.interface_modules.enums import *
from typing import List

from lernerlabdb.input_modules.mouse_input import MouseInput
from lernerlabdb.input_modules.procedure_input import ProcedureInput
from lernerlabdb.input_modules.note_input import NoteInput
from lernerlabdb.input_modules.surgery_input import SurgeryInput
from lernerlabdb.input_modules.user_input_sidebar import Sidebar

from shiny import *

import shinyswatch
from abc import ABC, abstractmethod
#! rework injection and abstracting cards


class InputCard(ABC):
    def __init__(self, card_input, card_name):
        self._card_input = None
        self.card_name = None

    @property
    def card_input(self):
        if not self._card_input:
            self._card_input = self.create_card_input()
        return self._card_input


class MouseInputCard(InputCard):
    def __init__(self, mouse_input: MouseInput):
        self._card_input = mouse_input
        self.card_name = "Mouse"
        
    def card(self):


class NavigationCards:
    def __init__(self, navigation_cards: List[InputCard]):
        self.navigation_cards = navigation_cards

    def generate_navigation_cards(self):
        cards = [c.card_input for c in self.navigation_cards]
        return ui.navset_underline(*cards)


class AppUI:
    def __init__(self, sidebar: Sidebar, navigation_cards: List[NavigationCards]):
        self.navigation_cards = navigation_cards
        self.sidebar = sidebar

    @property
    def user_interface(self):
        return ui.page_fluid(
            shinyswatch.theme.darkly(),
            self.sidebar.sidebar(),
            ui.markdown("---"),
            # NavigationCard.navigation_cards(),
        )







def server(input: Inputs, output: Outputs, session: Session):
    shinyswatch.theme.darkly()


app_ui = AppUI(sidebar=Sidebar, navigation_cards=NavigationCards)


app = App(app_ui.user_interface, server=server)
