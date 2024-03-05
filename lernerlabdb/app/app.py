from lernerlabdb.interface_modules.enums import *
from typing import List

from lernerlabdb.input_modules.navigation_cards import NavigationCards, MouseInputCard, SurgeryCard, ProcedureCard
from lernerlabdb.input_modules.inputs import MouseInput, NoteInput, ProcedureInput, SurgeryInput

from lernerlabdb.input_modules.user_input_sidebar import Sidebar

from shiny import *

import shinyswatch
from abc import ABC, abstractmethod
from shiny import Session


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

    class Outputs:
        pass


def server(input: Inputs, output: Outputs, session: Session):
    # inputs.
    pass


nav_cards = NavigationCards()
nav_cards.create_nav_cards(MouseInputCard(card_input=MouseInput()),
                           SurgeryCard(card_input=SurgeryInput()),
                           ProcedureCard(card_input=ProcedureInput())
                           )
app_ui = AppUI(sidebar=Sidebar, navigation_cards=nav_cards)


app = App(app_ui.user_interface, server=server)
