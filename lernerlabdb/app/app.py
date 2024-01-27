from lernerlabdb.interface_modules.enums import *

from lernerlabdb.input_modules.mouse_input import MouseInput
from lernerlabdb.input_modules.procedure_input import ProcedureInput
from lernerlabdb.input_modules.note_input import NoteInput
from lernerlabdb.input_modules.surgery_input import SurgeryInput
from lernerlabdb.input_modules.user_input_sidebar import Sidebar

from shiny import *

import shinyswatch

class NavigationCards:
    def __init__(self,
                mouse_input:MouseInput,
                surgery_input: SurgeryInput,
                procedure_input: ProcedureInput):
    self.mouse_input = mouse_input
    self._mouse_card = None
    self.surgery_input = surgery_input
    self._surgery_card = None
    self.procedure_input = procedure_input
    self._procedure_card = None
    
    @property
    def mouse_card(self):
        if not self._mouse_card:
            self._mouse_card = ui.nav(
                    "Mouse",
                    self.mouse_input.mouse_input()
                )
        return self._mouse_card
    @property
    def surgery_card(self):
        if not self._surgery_card:
            self._surgery_card = ui.nav(
                    "Surgery",
                    self.surgery_input.surgery_input()
                )
        return self._surgery_card
    
    @property
    def procedure_card(self):
        if not self._procedure_card:
            self._procedure_card = ui.nav(
                    "Procedure",
                    self.procedure_input.procedure_input()
                )
        return self._procedure_card

class AppUI:
    def __init__(self, navigation_cards: NavigationCards):
        self.navigation_cards = navigation_cards

    def navigation_cards(self):

        cards = [self.navigation_cards.mouse_card, surgery_card, procedure_card]

        return ui.navset_underline(*cards)

    def render_user_interface(self):
        return ui.page_fluid(
            shinyswatch.theme.darkly(),
            Sidebar.sidebar(),
            ui.markdown("---"),
            self.navigation_cards(mouse_input=MouseInput(),
                                  surgery_input=SurgeryInput(),
                                  procedure_input=ProcedureInput()
                                  )

        )


user_interface = AppUI()


def server(input: Inputs, output: Outputs, session: Session):
    shinyswatch.theme.darkly()


app = App(user_interface.render_user_interface(), server=server)
