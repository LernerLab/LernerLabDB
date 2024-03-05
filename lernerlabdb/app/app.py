from lernerlabdb.interface_modules.enums import *
from typing import List

from lernerlabdb.input_modules.navigation_cards import NavigationCards, MouseInputCard, SurgeryCard, ProcedureCard
from lernerlabdb.input_modules.inputs import MouseInput, NoteInput, ProcedureInput, SurgeryInput
from lernerlabdb.app_modules.app_objects import AppUI
from lernerlabdb.input_modules.user_input_sidebar import Sidebar

from shiny import *

import shinyswatch
from abc import ABC, abstractmethod


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
