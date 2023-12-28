from shiny import *
from lernerlabdb.input_modules.note_input import NoteInput
from lernerlabdb.interface_modules.drug import Drug
from lernerlabdb.interface_modules.enums import *

class SurgeryInput:
    
    @property
    def surgery_date_selector(self):
        surgery_date_selector = ui.input_date("surgery_date",
                                              "Surgery Date",
                                              format="mm/dd/yy",
                                              autoclose=True)
        return surgery_date_selector
        
    @property
    def drug_selector(self):
        drug_selector = ui.input_checkbox_group("drugs", "Drugs",
                                           choices=[v.value for v in DrugType])
        return drug_selector
    
    @property
    def column_layout(self):
        columns = ui.layout_column_wrap(
            (self.surgery_date_selector, self.drug_selector),
            width=1/2
        )
        
        return columns

    def surgery_input(self):
        
        
        surgery_input_form = ui.page_fillable(
            self.column_layout,
            ui.markdown("---"),
            NoteInput().display_note_input(),
        )
        
        return surgery_input_form
