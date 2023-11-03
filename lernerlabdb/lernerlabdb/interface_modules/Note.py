from datetime import datetime
from typing import Dict, NewType, Optional, Literal, Any
from lernerlabdb.interface_modules.enums import NoteType


Date = NewType("Date", datetime.date)
Time = NewType("Time", datetime.time)


class Note:
    """
    A class representing a note about a medical procedure or recovery.

    Attributes:
        type (Literal['Surgery', 'Recovery', 'Experimental', 'Other']): The type of the note.
        note (Any): The content of the note.
        date_ (str): The date of the note in the format "MM/DD/YYYY".
        time_ (str): The time of the note in the format "HH:MM".
        note_data (Dict[str, Any]): A dictionary containing the note data, including the date, time, type, and note content.

    Raises:
        ValueError: If the `type` argument is not one of the allowed options.

    """

    def __init__(self,
                 type: NoteType,
                 note):
        self.date: Date = datetime.now().date()
        self.time: Time = datetime.now().time()
        self._type = type
        self.note = note


    @property
    def date_(self) -> str:
        """The date of the note in the format "MM/DD/YYYY"""
        return self.date.strftime("%m/%d/%Y")

    @property
    def time_(self) -> str:
        """The time of the note in the format "HH:MM"."""
        return self.time.strftime("%H:%M")
    @property
    def type(self)->str:
        return self._type.value
    @property
    def data(self) -> Dict[str, Any]:
        """A dictionary containing the note data, including the date, time, type, and note content."""
        data = {"date": self.date_,
                "time": self.time_,
                "type": self.type,
                "note": self.note}
        return data
