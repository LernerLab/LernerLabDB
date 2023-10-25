from datetime import datetime
from typing import Dict, NewType, Optional, Literal, Any


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
                 type: Literal['Surgery', 'Recovery', 'Experimental', 'Other'],
                 note):
        self.date: Date = datetime.now().date()
        self.time: Time = datetime.now().time()

        if type not in ['Surgery', 'Recovery', 'Experimental', 'Other']:
            raise ValueError(
                "Note type must be one of: 'Surgery', 'Recovery', 'Experimental', 'Other'")
        self.type = type
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
    def data(self) -> Dict[str, Any]:
        """A dictionary containing the note data, including the date, time, type, and note content."""
        data = {"date": self.date_,
                "time": self.time_,
                "type": self.type,
                "note": self.note}
        return data
