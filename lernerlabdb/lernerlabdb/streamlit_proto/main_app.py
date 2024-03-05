import streamlit as st
import datetime
import numpy as np
import pandas as pd
from lernerlabdb.interface_modules.enums import *

import streamlit.components.v1 as components


class MainApp:
    def __init__(self, title):
        self.title = 'test'
        self.date = datetime.datetime.now().date()
        self.time = datetime.datetime.now().time()

    def side_bar(self):
        st.sidebar.date_input("Date", self.date)

        with st.sidebar.expander("User info"):
            st.text_input("Name", "First Last")
            st.text_input("Email", )
            st.text_input("NetID", )

    def main_tabs(self):

        mouse_tab, surgery_tab, procedure_tab = st.tabs(
            ["Mouse", "Surgery", "Procedure"])

        with mouse_tab:
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                in_co1_1, in_col1_2 = st.columns(2)
                in_co1_1.radio("Sex", [s.value for s in Sex])
                in_col1_2.radio("Location", [l.value for l in Location])
                col1.radio("Zygosity", [s.value for s in Zygosity])
            col2.selectbox('Genotype', [g.value for g in Genotype])

            col3.markdown("""Drugs Administered""")
            for drugs in DrugType:
                col3.checkbox(drugs.value)

        with procedure_tab:
            # STRUCTURE COLUMNS
            structure_col, injection_col, implant_col = st.columns(3)
            with structure_col:
                structure_col.markdown("""
                          ### Structure
                          ____
                           """)
                structure_col.text_input("Structure Name")

                strucutre_cord_columns = st.columns(3)
                structure_cords_text = ("AP", "ML", "DV")

                for s_col, s_text in zip(strucutre_cord_columns, structure_cords_text):
                    s_col.text_input(s_text)

            structure_col.radio("Hemisphere", [h.value for h in Hemisphere])

            # INJECTION COLUMNS
            with injection_col:
                injection_col.markdown("""
                          ### Injection
                          ____
                           """)
                injection_col.selectbox("Injection Type", [
                    i.value for i in InjectionType])

                text_inputs = ["Substrate Name",
                               "Titer (E12)", "Volume (nL)", "Flow Rate (nL/min)"]
                for text in text_inputs:
                    injection_col.text_input(text)

            # IMPLANT COLUMNS
            with implant_col:
                implant_col.markdown("""
                          ### Implant
                          ____
                           """)
                implant_col.selectbox(
                    "Implant Type", [i.value for i in ImplantType])
                implant_col.text_input("Angle")
                implant_col.markdown("""adjusted coordinates""")

                implant_cord_columns = st.columns(3)
                implant_cord_text = ("implant AP", "implant ML", "implant DV")

                for i_col, i_text in zip(implant_cord_columns, implant_cord_text):
                    i_col.text_input(i_text)

        # with tab4:

    def second_row_tabs(self):
        st.header("Notes")
        notes_tab, collaps_notes_tab, = st.tabs(["Notes", "Hide"])

        with notes_tab:
            col2_2_1, col2_1_2 = st.columns(2)

            col2_2_1.radio("Note Type", [n.value for n in NoteType])
            col2_1_2.radio("Add note to:", [
                "Mouse", "Surgery", "Procedure", "Cage"])

            st.text_area('Note: ',)
            st.button("Add Note")

    def app(self):
        self.side_bar()
        self.main_tabs()
        self.second_row_tabs()


if __name__ == '__main__':
    app = MainApp("title")
    app.app()
