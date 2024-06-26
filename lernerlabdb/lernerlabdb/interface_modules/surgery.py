from datetime import datetime
from typing import List, Dict, Any, NewType

from lernerlabdb.customs.custom_types import Date, Time, NumberOfDays
from lernerlabdb.interface_modules.drug import Drug
from lernerlabdb.interface_modules.note import Note
from lernerlabdb.interface_modules.procedure import Procedure


class Surgery:
    """
    A class representing a surgery.

    Attributes
    ----------
    surgery_number : int
        The unique identifier for the surgery.
    date : datetime
        The date of the surgery.
    time_of_surgery : datetime
        The time when the surgery was conducted.
    _procedures : list of Procedure
        A private list of procedures conducted during the surgery.
    _drugs : list of Drug
        A private list of drugs used during the surgery.
    _notes : list of Note
        A private list of notes related to the surgery.


    Properties
    ----------
    date_ : str
        Returns the string representation of the surgery date.
    time_of_surgery_ : str
        Returns the string representation of the surgery time.
    procedures : list of Procedure
        Returns the list of procedures associated with the surgery.
    drugs : list of Drug
        Returns the list of drugs associated with the surgery.
    notes : list of Note
        Returns the list of notes associated with the surgery.
    surgery_data : dict
        Returns a dictionary containing all associated data for the surgery.
    """

    surgery_number: int

    def __init__(self, surgery_number):
        self.surgery_number = surgery_number

        self._date: Date = datetime.now()
        self._procedures: List[Procedure] = []
        self._drugs: List[Drug] = []
        self._notes: List[Note] = []

    @property
    def date(self) -> datetime:
        '''The date onbject of the surgery'''
        return self._date.date()

    @property
    def date_string(self) -> datetime:
        '''The string date of the surgery'''
        return self.date.strftime("%m/%d/%Y")

    @property
    def time_of_surgery(self) -> datetime:
        '''The string time of the surgery'''
        return self._date.time()

    @property
    def time_of_surgery_string(self):
        return self.time_of_surgery.strftime("%H:%M")

    @property
    def procedures(self) -> List[Procedure]:
        '''A list of procedures associated with the surgery'''
        return self._procedures

    def add_procedure(self, *procedures: Procedure) -> None:
        '''Adds a Procedure object to the list of procedures associated with the surgery'''
        for procedure in procedures:
            if isinstance(procedure, list):
                self._procedures.extend(procedure)
            else:
                self._procedures.append(procedure)

    @property
    def drugs(self) -> List[Drug]:
        '''A list of drugs associated with the surgery'''
        return self._drugs

    def add_drug(self, *drugs: Drug) -> None:
        '''Adds a Drug object to the list of drugs associated with the surgery'''
        for drug in drugs:
            if isinstance(drug, list):
                self._drugs.extend(drug)
            else:
                self._drugs.append(drug)

    @property
    def notes(self) -> List[Note]:
        '''A list of notes associated with the surgery'''
        return self._notes

    def add_note(self, *notes: Note) -> None:
        '''Adds a Note object to the list of notes associated with the surgery'''
        for note in notes:
            if isinstance(note, list):
                self._notes.extend(note)
            else:
                self._notes.append(note)

    @property
    def data(self) -> Dict[str, Any]:
        '''Returns a dictionary containing all associated data for the surgery'''
        data = {
            "Date": self.date,
            "Time of surgery": self.time_of_surgery,
            "Surgery number": self.surgery_number,
            "Procedures": [procedure.data for procedure in self.procedures],
            "Drugs": [drug.data for drug in self.drugs],
            "Notes": [note.data for note in self.notes],
        }
        return data
