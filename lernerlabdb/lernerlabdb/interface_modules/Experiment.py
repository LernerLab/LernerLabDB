
from lernerlabdb.interface_modules.Note import Note
from typing import List, NewType

from lernerlabdb.interface_modules.Mouse import Mouse


class Experiment:
    experiment_name: str
    mice: List[Mouse]
    notes: List[Note]
    
    def __init__(self, experiment_name):
        self.experiment_name = experiment_name
        self._mice = []
        self._notes= []

    @property
    def mice(self):
        return self._mice

    @property
    def notes(self):
        return self._notes

    def add_mice(self, *mice):
        for mouse in mice:
            if isinstance(mouse, list):
                self._mice.extend(mouse)
            else:
                self._mice.append(mouse)

    def add_notes(self, *notes):
        for note in notes:
            if isinstance(note, list):
                self._notes.extend(note)
            else:
                self._notes.append(note)

    @property
    def data(self):
        data = {
            "experiment_name": self.experiment_name,
            "mice": [mouse.data for mouse in self.mice],
            "notes": [note.data for note in self.notes]
        }
        return data
