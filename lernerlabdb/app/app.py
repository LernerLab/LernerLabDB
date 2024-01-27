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


class NavigationCard(ABC):
    def __init__(self, card_input):
        self._card_input = None
        self.card_name = None

    def create_card_input(self):
        card_input = ui.nav(self.card_name, self.card_input())
        return card_input

    @property
    def card(self):
        if not self._card_input:
            self._card_input = self.create_card_input()
        return self._card_input


class MouseNavigationCard(NavigationCard):
    def __init__(self, mouse_input: MouseInput):
        self._card_input = mouse_input
        self.card_name = "Mouse"


class AppUI:
    def __init__(self, navigation_cards: List[NavigationCard]):
        self.navigation_cards = navigation_cards

    def generate_navigation_cards(self):

        cards = [c.card for c in self.navigation_cards]

        return ui.navset_underline(*cards)

    def render_user_interface(self):
        return ui.page_fluid(
            shinyswatch.theme.darkly(),
            Sidebar.sidebar(),
            ui.markdown("---"),
            self.generate_navigation_cards()
        )


mouse_card = MouseNavigationCard(MouseInput())

user_interface = AppUI(navigation_cards=[mouse_card])


def server(input: Inputs, output: Outputs, session: Session):
    shinyswatch.theme.darkly()


app = App(user_interface.render_user_interface(), server=server)
