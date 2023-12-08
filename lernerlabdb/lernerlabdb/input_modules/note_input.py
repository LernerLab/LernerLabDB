
from shiny import *
from lernerlabdb.interface_modules.enums import NoteType


class NoteInput:
    def __init__(self):
        pass

    @property
    def note_type_selector(self):
        note_type_selector = ui.input_selectize(
            "note_type", "Note Type", choices=[v.value for v in NoteType])
        return note_type_selector

    @property
    def note_input(self):
        note_input = ui.input_text_area("note", "Note")
        return note_input

    def display_note_input(self):
        note_button = ui.input_action_button("note_input", "Add Note")
        note_form = ui.page_fillable(
            self.note_type_selector, self.note_input, note_button)
        return note_form
