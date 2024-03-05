from abc import ABC, abstractmethod
from shiny import *


from lernerlabdb.input_modules.inputs import MouseInput, NoteInput, ProcedureInput, SurgeryInput


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
        card = ui.nav_panel(
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
        card = ui.nav_panel(
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
        card = ui.nav_panel(
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
