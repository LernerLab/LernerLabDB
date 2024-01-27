from shiny import *
from lernerlabdb.input_modules.coordinates_input import CoordinatesInput
from lernerlabdb.interface_modules.structure import Structure
from lernerlabdb.interface_modules.enums import BrainStructure, Hemisphere


class StructureInput:

    @property
    def title(self):
        title = ui.markdown("### Structure")
        return title
    @property
    def structure_selector(self):
        structure_choices = [s.value for s in BrainStructure]
        selector = ui.input_selectize(
            "structure", "Structure", choices=structure_choices)

        return selector

    @property
    def hemisphere_select(self):
        hemisphere_choices = [s.value for s in Hemisphere]
        selector = ui.input_selectize(
            "hemisphere", "Hemisphere", choices=hemisphere_choices)

        return selector

    @property
    def column_layout(self):
        columns = ui.column(4,
            (self.structure_selector, self.hemisphere_select,
            CoordinatesInput().coordinates_input_form)
        
)
        return columns

    @property
    def structure_input_form(self):
        structure_input_form = ui.page_fillable(
            self.title, 
            self.column_layout
        )

        return structure_input_form
