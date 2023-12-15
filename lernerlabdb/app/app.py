from lernerlabdb.interface_modules.enums import *

from lernerlabdb.input_modules.mouse_input import MouseInput
from lernerlabdb.input_modules.note_input import NoteInput
from lernerlabdb.input_modules.surgery_input import SurgeryInput
from lernerlabdb.input_modules.user_input_sidebar import Sidebar

from shiny import *

import shinyswatch





class AppUI:

    
    def navigation_cards(self):
        mouse_card = ui.nav(
           "Mouse",
            MouseInput().mouse_input()
            )

        surgery_card = ui.nav(
            "Surgery", 
             SurgeryInput.surgery_input()
        )

        procedure_card = ui.nav(
            title="Procedure")

        cards = [mouse_card, surgery_card, procedure_card]

        return ui.navset_underline(*cards)

    def render_user_interface(self):
        return ui.page_fluid(
            shinyswatch.theme.darkly(),
            Sidebar.sidebar(),
            ui.markdown("---"),
            self.navigation_cards(),

        )


user_interface = AppUI()



def server(input: Inputs, output: Outputs, session: Session):
    shinyswatch.theme.darkly()
    

    
app = App(user_interface.render_user_interface(), server = None)
