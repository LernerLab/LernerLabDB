from lernerlabdb.interface_modules import Coordinates, Drug, BrainStructure, Hemisphere, Structure, ImplantType, InjectionType, NoteType, Sex, Genotype, Zygosity, DrugType
from shiny import *


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


class CoordinatesInput:

    @property
    def title(self):
        title = ui.markdown("#### Coordinates")
        return title

    def single_input_form(self, name, display):
        single_input = ui.input_text(id=name, label=display)
        return single_input

    @property
    def coordinates_input(self):
        input_form = ui.row(
            ui.column(2, self.single_input_form("ap", "AP")),
            ui.column(2, self.single_input_form("ml", "ML")),
            ui.column(2, self.single_input_form("dv", "DV"))
        )
        return input_form

    @property
    def coordinates_input_form(self):
        form = ui.page_fillable(
            self.title,
            self.coordinates_input,
        )
        return form


class StructureInput:

    def __init__(self):
        self._numb_structure_input_columns = 1
        self._structure_input_columns = None

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
    def implant_selector(self):
        implant_choices = [i.value for i in ImplantType]
        selector = ui.input_selectize(
            "implant", "Implant", choices=implant_choices)
        return selector

    @property
    def injection_selector(self):
        injection_choices = [i.value for i in InjectionType]
        selector = ui.input_selectize(
            "injection", "Injection", choices=injection_choices)
        return selector

    @property
    def single_structure_input_column(self):
        single_input = (self.structure_selector, self.hemisphere_select,
                        CoordinatesInput().coordinates_input_form,
                        self.implant_selector,
                        self.injection_selector)
        return single_input

    @property
    def structure_input_columns(self):
        if not self._structure_input_columns:
            self._structure_input_columns = [
                self.single_structure_input_column]
        return self._structure_input_columns

    @structure_input_columns.setter
    def structure_input_columns(self, value):
        self._structure_input_columns = value

    @property
    def structure_input_column_layout(self):
        columns = ui.layout_column_wrap(
            *self.structure_input_columns
        )
        return columns

    def structure_input_form(self, numb):

        structure_input_form = ui.page_fillable(
            ui.panel_title(f'Structure {numb+1}'),
            self.structure_input_column_layout,
            # self.add_structure_button
        )

        return structure_input_form


class MouseInput:

    @property
    def dob_selector(self):
        dob_selector = ui.input_date("dob", "Date of Birth",
                                     format="mm/dd/yy",
                                     autoclose=True)
        return dob_selector

    @property
    def ear_tag_input(self):
        ear_tag_input = ui.input_text("ear_tag", "Ear Tag")
        return ear_tag_input

    @property
    def genotype_selector(self):
        genotype_selector = ui.input_selectize(
            "genotype", "Genotype", choices=[v.value for v in Genotype])
        return genotype_selector

    @property
    def status_selector(self):
        status_selector = ui.input_switch(
            "status", "Dead")
        return status_selector

    @property
    def sex_radio(self):
        sex_radio = ui.input_radio_buttons(
            "sex", label="Sex", choices=[s.value for s in Sex])
        return sex_radio

    @property
    def zygosity_selector(self):
        selector = ui.input_selectize(
            "zygosity", "Zygosity", choices=[v.value for v in Zygosity])
        return selector

    @property
    def column_layout(self):
        columns = ui.layout_column_wrap(
            (self.status_selector, self.dob_selector,
             self.sex_radio, self.ear_tag_input),
            (self.genotype_selector, self.zygosity_selector),
            width=1/6)

        return columns

    def mouse_input(self):

        mouse_button = ui.input_action_button("mouse_input", "Add Mouse")
        mouse_form = ui.page_fillable(
            self.column_layout,
            ui.markdown("---"),
            NoteInput().display_note_input(),
            mouse_button)

        return mouse_form


class ProcedureInput:
    def __init__(self, num_structures=4):
        self._strucutre_inputs = None
        self._num_structures = num_structures

    @property
    def name_input(self):
        name_input = ui.input_text("name", "Procedure Name")
        return name_input

    @property
    def procedure_meta_input_layout(self):
        columns = ui.layout_column_wrap(
            self.name_input, width=1/6)
        return columns

    @property
    def procedure_structures_columns(self):
        cols = [StructureInput().structure_input_form(i)
                for i in range(self._num_structures)]
        input_cols = ui.layout_columns(*cols)
        return input_cols

    def procedure_input(self):
        procedure_input_form = ui.page_fillable(
            self.procedure_meta_input_layout,
            ui.markdown("---"),
            self.procedure_structures_columns,
            ui.markdown("---"),
            NoteInput().display_note_input()
        )

        return procedure_input_form


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
        columns = ui.column(4,
                            (self.surgery_date_selector, self.drug_selector)
                            )

        return columns

    def surgery_input(self):

        surgery_input_form = ui.page_fillable(
            self.column_layout,
            ui.markdown("---"),
            NoteInput().display_note_input(),
        )

        return surgery_input_form
