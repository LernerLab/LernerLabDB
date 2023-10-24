from datetime import datetime
from typing import List, Dict, Any

from lernerlabdb.interface_modules.Drug import Drug
from lernerlabdb.interface_modules.Note import Note
from lernerlabdb.interface_modules.Procedure import Procedure


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
    def __init__(self, surgery_number: int):
        self.date: datetime = datetime.now().date()
        self.time_of_surgery: datetime = datetime.now().time()
        self.surgery_number = surgery_number
        self._procedures: List[Procedure] = []
        self._drugs: List[Drug] = []
        self._notes: List[Note] = []

    @property
    def date_(self) -> datetime:
        '''The string date of the surgery'''
        return self.date.strftime("%m/%d/%Y")

    @property
    def time_of_surgery_(self) -> datetime:
        '''The string time of the surgery'''
        return self.time_of_surgery.strftime("%H:%M")

    @property
    def procedures(self) -> List[Procedure]:
        '''A list of procedures associated with the surgery'''
        return self._procedures

    def add_procedure(self, procedure: Procedure) -> None:
        '''Adds a Procedure object to the list of procedures associated with the surgery'''
        self._procedures.append(procedure)

    @property
    def drugs(self) -> List[Drug]:
        '''A list of drugs associated with the surgery'''
        return self._drugs

    def add_drug(self, drug: Drug) -> None:
        '''Adds a Drug object to the list of drugs associated with the surgery'''
        self._drugs.append(drug)

    @property
    def notes(self) -> List[Note]:
        '''A list of notes associated with the surgery'''
        return self._notes

    def add_note(self, note: Note) -> None:
        '''Adds a Note object to the list of notes associated with the surgery'''
        self._notes.append(note)

    @property
    def surgery_data(self) -> Dict[str, Any]:
        '''Returns a dictionary containing all associated data for the surgery'''
        data = {
            "Date": self.date,
            "Time of surgery": self.time_of_surgery,
            "Surgery number": self.surgery_number,
            "Procedures": [procedure.procedure_data for procedure in self.procedures],
            "Drugs": [drug.drug_data for drug in self.drugs],
            "Notes": [note.note_data for note in self.notes],
        }
        return data
