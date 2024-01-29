from lernerlabdb.interface_modules.enums import *
from typing import List

from lernerlabdb.input_modules.navigation_cards import NavigationCards, MouseInputCard, SurgeryCard, ProcedureCard
from lernerlabdb.input_modules.inputs import MouseInput, NoteInput, ProcedureInput, SurgeryInput

from lernerlabdb.input_modules.user_input_sidebar import Sidebar

from shiny import *

import shinyswatch
from abc import ABC, abstractmethod
#! rework injection and abstracting cards


class InputCard(ABC):
    @abstractmethod
    def __init__(self):
        self._card_input = None
        self.card_name = None


class MouseInputCard(InputCard):
    def __init__(self, card_input: MouseInput):
        self.card_input = card_input
        self.card_name = "Mouse"

    @property
    def card(self):
        card = ui.nav(
            self.card_name,
            self.card_input.mouse_input()
        )
        return card


class SurgeryCard(InputCard):
    def __init__(self, card_input: SurgeryInput):
        self.card_input = card_input
        self.card_name = "Surgery"

    @property
    def card(self):
        card = ui.nav(
            self.card_name,
            self.card_input.surgery_input()
        )
        return card


class ProcedureCard(InputCard):
    def __init__(self, card_input: ProcedureInput):
        self.card_input = card_input
        self.card_name = "Procedure"

    @property
    def card(self):
        card = ui.nav(
            self.card_name,
            self.card_input.procedure_input()
        )
        return card


class NavigationCards:
    def __init__(self):
        self.navigation_cards = None

    @property
    def cards(self):
        cards = [c.card for c in self.navigation_cards]
        return ui.navset_underline(*cards)

    def create_nav_cards(self, *cards):
        self.navigation_cards = None  # clears cards and makes new ones
        self.navigation_cards = [nav_card for nav_card in cards]
        return self.navigation_cards


class AppUI:
    def __init__(self, sidebar: Sidebar, navigation_cards: NavigationCards):
        self.navigation_cards = navigation_cards
        self.sidebar = sidebar

    @property
    def user_interface(self):
        return ui.page_fluid(
            shinyswatch.theme.darkly(),
            self.sidebar.sidebar(),
            ui.markdown("---"),
            self.navigation_cards.cards
        )


def server(input: Inputs, output: Outputs, session: Session):
    shinyswatch.theme.darkly()


nav_cards = NavigationCards()
nav_cards.create_nav_cards(MouseInputCard(card_input=MouseInput()),
                           SurgeryCard(card_input=SurgeryInput()),
                           ProcedureCard(card_input=ProcedureInput())
                           )
app_ui = AppUI(sidebar=Sidebar, navigation_cards=nav_cards)


app = App(app_ui.user_interface, server=server)
