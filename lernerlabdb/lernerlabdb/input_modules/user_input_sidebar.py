from shiny import *


class Sidebar:
    def sidebar():
        title = ui.markdown(
            text="# User Info",
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
