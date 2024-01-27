
from shiny import *
from lernerlabdb.interface_modules.enums import NoteType


class NoteInput:
    @property
    def title(self):
        title = ui.panel_title("Notes", "notes")
        return title

    @property
    def note_type_selector(self):
        note_type_selector = ui.input_selectize(
            "note_type", "Note Type", choices=[v.value for v in NoteType])
        return note_type_selector

    @property
    def note_input(self):
        note_input = ui.input_text_area("Notes", "notes")
        return note_input
    @property
    def note_button(self):
        note_button = ui.input_action_button("note_input", "Add Note")
        return note_button
    def display_note_input(self):
        note_form = ui.page_fillable(
            self.title,
            self.note_type_selector,
            self.note_input,
            self.note_button)
        return note_form
