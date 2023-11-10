
from typing import List, Dict, Any
from lernerlabdb.interface_modules.Mouse import Mouse
from lernerlabdb.interface_modules.Note import Note


class Experiment:

    """
    Represents an experiment conducted in the lab.

    Parameters
    ----------
    experiment_name : str
        The name of the experiment.

    Attributes
    ----------
    experiment_name : str
        The name of the experiment.
    _mice : List[Mouse]
        A list of Mouse objects associated with the experiment.
    _notes : List[Note]
        A list of Note objects associated with the experiment.

    Methods
    -------
    mice() -> List[Mouse]
        Returns a list of Mouse objects associated with the experiment.
    notes() -> List[Note]
        Returns a list of Note objects associated with the experiment.
    add_mice(*mice) -> None
        Adds one or more Mouse objects to the experiment.
    add_notes(*notes) -> None
        Adds one or more Note objects to the experiment.
    data() -> dict
        Returns a dictionary representation of the experiment data.
    """

    def __init__(self, experiment_name):
        self.experiment_name:str = experiment_name
        self._mice:List[Mouse] = []
        self._notes:List[Note] = []

    @property
    def mice(self)-> List[Mouse]:
        """
        Returns a list of Mouse objects associated with the experiment.
        """
        return self._mice

    @property
    def notes(self) -> List[Note]:
        """
        Returns a list of Note objects associated with the experiment.
        """
        
        return self._notes

    def add_mice(self, *mice)-> None:
        """
        Adds one or more Mouse objects to the experiment.
        """
        for mouse in mice:
            if isinstance(mouse, list):
                self._mice.extend(mouse)
            else:
                self._mice.append(mouse)

    def add_notes(self, *notes):
        """
        Adds one or more Note objects to the experiment.
        """
        for note in notes:
            if isinstance(note, list):
                self._notes.extend(note)
            else:
                self._notes.append(note)

    @property
    def data(self)->Dict[str, Any]:
        """Returns a dictionary representation of the experiment data."""
        data = {
            "experiment_name": self.experiment_name,
            "mice": [mouse.data for mouse in self.mice],
            "notes": [note.data for note in self.notes]
        }
        return data
