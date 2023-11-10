from datetime import datetime, date, time, timedelta
from typing import List, Dict, Any, Optional, Literal, NewType
from uuid import uuid4

from lernerlabdb.interface_modules.Cage import Cage
from lernerlabdb.interface_modules.Surgery import Surgery
from lernerlabdb.interface_modules.Note import Note
from lernerlabdb.interface_modules.ExperimentalData import ExperimentalData
from lernerlabdb.interface_modules.Scientist import Scientist
from lernerlabdb.interface_modules.enums import Sex, Zygosity, MouseStatus, Genotype

Date = NewType('Date', date)
Time = NewType('Time', time)
NumberOfDays = NewType('NumberOfDays', int)
NumberOfWeeks = NewType('NumberOfWeeks', int)


class Mouse:

    def __init__(self,
                 date_of_birth: Date,
                 sex: Sex,
                 ear_tag: int,
                 genotype: Genotype,
                 zygosity: Zygosity,
                 experiment_owner: Scientist,
                 status: MouseStatus = MouseStatus.ALIVE,
                 surgeon: Optional[Scientist] = None,
                 cage: Optional[Cage] = None
                 ):
        self._unique_id = uuid4()
        self._date_of_birth = date_of_birth
        self._sex = sex
        self._ear_tag = ear_tag
        self._genotype = genotype
        self._zygosity = zygosity
        self._surgeon = surgeon
        self._experiment_owner = experiment_owner
        self._cage = cage
        self._status = status
        self._surgeries: List[Surgery] = []
        self._notes: List[Note] = []
        self._experimental_data: List[ExperimentalData] = []

    # Public methods and updaters
    @property
    def unique_id(self) -> str:
        """
        Returns the unique identifier for the mouse.
        """
        return self._unique_id.hex

    @property
    def date_of_birth(self) -> Date:
        """
        Returns the date of birth of the mouse.
        """
        return self._date_of_birth

    #! age attributes will need a way to be refreshed.  once per day?
    @property
    def age_days(self) -> NumberOfDays:
        """
        Returns the age of the mouse in days.
        """
        delta_days = datetime.now() - self.date_of_birth
        return delta_days.days

    @property
    def age_weeks(self) -> NumberOfWeeks:
        """
        Returns the age of the mouse in weeks.
        """

        return self.age_days // 7

    @property
    def age_(self) -> Dict[str, int]:
        """
        Returns a dictionary of all age attributes
        """

        return {
            "days": self.age_days,
            'weeks': self.age_weeks,
            'days since first surgery': self.days_since_first_surgery,
            'weeks since first surgery': self.weeks_since_first_surgery
        }

    @property
    def days_since_first_surgery(self) -> NumberOfDays:
        """
        Returns the number of days since the first surgery.
        """

        if len(self.surgeries) == 0:
            return 0
        first_surgery_date = self.surgeries[0]._date
        delta_days = datetime.now() - first_surgery_date
        return delta_days.days

    @property
    def weeks_since_first_surgery(self) -> NumberOfWeeks:
        """
        Returns the weeks of days since the first surgery.
        """

        return self.days_since_first_surgery // 7

    @property
    def sex(self) -> Literal['male', 'female']:
        """
        Returns the sex of the mouse.
        """
        return self._sex.value

    @property
    def ear_tag(self) -> int:
        """
        Returns the ear tag of the mouse.
        """
        return self._ear_tag

    @property
    def genotype(self) -> str:
        """
        Returns the genotype of the mouse.
        """
        return self._genotype.value

    def update_genotype(self, genotype):
        """
        Pseudo setter for genotype. Updates the genotype of the mouse.
        """
        self._genotype = genotype

    @property
    def zygosity(self) -> str:
        """
        Returns the zygosity of the mouse.
        """
        return self._zygosity.value

    def update_zygosity(self, zygosity):
        """
        Pseudo setter for zygosity. Updates the zygosity of the mouse.
        """
        self._zygosity = zygosity

    @property
    def cage(self) -> Cage:
        """
        Returns the Cage object associated with the mouse.

        """
        return self._cage

    def attach_to_cage(self, cage: Cage) -> None:
        """
        Attaches the mouse to a Cage object
        """

        self._cage = cage

    @property
    def status(self) -> str:
        """
        Returns the status of the mouse: 'Alive' or 'Dead'.
        """
        return self._status.value

    def update_status(self) -> None:
        """
        Toggles the status of the mouse between 'Alive' and 'Dead'.
        """
        if self._status.value == MouseStatus.ALIVE:
            self._status = MouseStatus.DEAD
        else:
            self._status = MouseStatus.ALIVE

    @property
    def surgeon(self) -> Scientist:
        """
        Returns the Scientist object assigned to the surgery of the mouse. If no surgeon is assigned, returns the Scientist object assigned to the experiment.
        """
        if self._surgeon is None:
            return self._experiment_owner
        else:
            return self._surgeon

    @property
    def experiment_owner(self) -> Scientist:
        """
        Returns the Scientist object assigned to the experiment of the mouse.
        """
        return self._experiment_owner

    def update_experiment_owner(self, scientist: Scientist) -> None:
        """
        Pseudo setter for experiment_owner. Updates the experiment_owner of the mouse
        """
        self._experiment_owner = scientist

    @property
    def surgeries(self) -> List[Surgery]:
        """
        Returns a list of Surgery objects associated with the mouse.
        """
        return self._surgeries

    def add_surgeries(self, *surgeries: Surgery) -> None:
        """
        Adds a list of Surgery objects to the list of surgeries associated with the mouse.
        """
        for surgery in surgeries:
            if isinstance(surgery, list):
                self._surgeries.extend(surgery)
            else:
                self._surgeries.append(surgery)

    @property
    def notes(self) -> List[Note]:
        """
        Adds a list of Surgery objects to the list of surgeries associated with the mouse.
        """
        return self._notes

    def add_note(self, *notes: Note) -> None:
        """
        Adds a list of Surgery objects to the list of surgeries associated with the mouse.
        """
        for note in notes:
            if isinstance(note, list):
                self._notes.extend(note)
            else:
                self._notes.append(note)

    @property
    def experimental_data(self) -> List[ExperimentalData]:
        """
        Returns a list of ExperimentalData objects associated with the mouse.
        """
        return self._experimental_data

    def add_experiment(self, *experiments: ExperimentalData) -> None:
        """
        Adds a list of ExperimentalData objects to the list of experimental data associated with the mouse.
        """
        for exp in experiments:
            if isinstance(exp, list):
                self._experimental_data.extend(exp)
            else:
                self._experimental_data.append(exp)

    @property
    def data(self) -> Dict[str, Any]:
        """
        Returns a dictionary representation of the mouse data.
        """
        data = {
            'unique id': self.unique_id,
            'cage': self.cage,
            'ear tag': self.ear_tag,
            'sex': self.sex,
            'genotype': self.genotype,
            'zygosity': self.zygosity,
            'date of birth': self.date_of_birth,
            'status': self.status,
            'experiment_owner': self.experiment_owner,
            'surgeon': self.surgeon,
            'age': self.age_,
            "surgeries": [surgery.data for surgery in self.surgeries],
            "notes": [note.data for note in self.notes]
            #! Add experimental data links, references, or paths to files

        }
        return data
