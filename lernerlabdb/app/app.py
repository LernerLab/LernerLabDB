from lernerlabdb.interface_modules.enums import *

from shiny import *

import shinyswatch

class Sidebar:
    pass
class AppUI:

    def user_info_sidebar(self):
        title = ui.markdown(
         text = "# User Info",
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
    
    def mouse_input(self):
        sex_radio = ui.input_radio_buttons("sex", label = "Sex", choices = [s.value for s in Sex])
        # zygosity_radio = ui.input_radio_buttons("zygosity", "Zygosity", [Zygosity.HETERO, Zygosity.HOMO])
        mouse_form = [
            ui.page_fillable(
            ui.input_text("NONE", "PLACE_HOLDER"),

            ui.br())]
        
        mouse_button = ui.input_action_button("mouse_input", "Add Mouse")
        
        mouse_form = ui.page_fillable(sex_radio, mouse_form, mouse_button)
   
        return mouse_form
    def navigation_cards(self):
        mouse_card = ui.nav(
            "Mouse",
            self.mouse_input())
        
        surgery_card = ui.nav(
            title="Surgery")
        
        procedure_card = ui.nav(
            title="Procedure")
        
        cards = [mouse_card, surgery_card, procedure_card]
        
        return ui.navset_underline(*cards)

    def render_user_interface(self):
        return ui.page_fluid(
            self.user_info_sidebar(),
            self.navigation_cards(),

        )


user_interface = AppUI()



app = App(user_interface.render_user_interface(), server = None)
