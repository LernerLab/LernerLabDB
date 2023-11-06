from datetime import datetime, date, time, timedelta
from typing import List, Dict, Any, Optional, Literal, NewType
from uuid import uuid4

from lernerlabdb.interface_modules.Cage import Cage
from lernerlabdb.interface_modules.Surgery import Surgery
from lernerlabdb.interface_modules.Note import Note
from lernerlabdb.interface_modules.Experiment import Experiment
from lernerlabdb.interface_modules.Scientist import Scientist
from lernerlabdb.interface_modules.enums import Sex, Zygosity, MouseStatus, Genotype

Date = NewType('Date', date)
Time = NewType('Time', time)
NumberOfDays = NewType('NumberOfDays', int)
NumberOfWeeks = NewType('NumberOfWeeks', int)


class Mouse:

    def __init__(self,
                 date_of_birth: datetime,
                 sex: Sex,
                 ear_tag: int,
                 genotype: Genotype,
                 zygosity: Zygosity,
                 experiment_owner: Scientist,
                 surgeon: Optional[Scientist] = None,
                 cage: Optional[Cage] = None,
                 status: MouseStatus = MouseStatus.ALIVE
                 ):
        self._unique_id = uuid4()
        self._date_of_birth = date_of_birth

        self._sex = sex
        self._ear_tag = ear_tag
        self._genotype = genotype

        self._zygosity = zygosity

        if surgeon is None:
            self._surgeon = experiment_owner
        else:
            self._surgeon = surgeon
        self._experiment_owner = experiment_owner
        self._cage = cage
        self._status: MouseStatus = MouseStatus.ALIVE
        self._surgeries: List[Surgery] = []
        self._notes: List[Note] = []
        self._experiments: List[Experiment] = []

    # Public methods and updaters
    @property
    def unique_id(self) -> str:
        return self._unique_id.hex

    @property
    def date_of_birth(self) -> Date:
        return self._date_of_birth

    #! age attributes will need a way to be refreshed.  once per day?
    @property
    def age_days(self) -> NumberOfDays:
        delta_days = datetime.now() - self.date_of_birth
        return delta_days.days

    @property
    def age_weeks(self) -> NumberOfWeeks:
        return self.age_days // 7

    @property
    def age_(self) -> Dict[str, int]:
        return {
            "days": self.age_days,
            'weeks': self.age_weeks,
            'day since first surgery': self.days_since_first_surgery,
            'weeks since first surgery': self.weeks_since_first_surgery
        }

    @property
    def days_since_first_surgery(self) -> NumberOfDays:
        if len(self.surgeries) == 0:
            return 0
        first_surgery_date = self.surgeries[0]._date
        delta_days = datetime.now() - first_surgery_date
        return delta_days.days

    @property
    def weeks_since_first_surgery(self) -> NumberOfWeeks:
        return self.days_since_first_surgery // 7

    @property
    def sex(self) -> Literal['male', 'female']:
        return self._sex.value

    @property
    def ear_tag(self) -> int:
        return self._ear_tag

    @property
    def genotype(self) -> str:
        return self._genotype.value

    def update_genotype(self, genotype):
        self._genotype = genotype

    @property
    def zygosity(self) -> str:
        return self._zygosity.value

    def update_zygosity(self, zygosity):
        self._zygosity = zygosity

    @property
    def cage(self) -> Cage:
        return self._cage

    def attach_to_cage(self, cage: Cage) -> None:
        self._cage = cage

    @property
    def status(self) -> str:
        return self._status.value

    @status.setter
    def update_status(self) -> None:
        if self._status.value == MouseStatus.ALIVE:
            self._status = MouseStatus.DEAD
        else:
            self._status = MouseStatus.ALIVE

    @property
    def surgeon(self) -> Scientist:
        if self._surgeon is None:
            return self._experiment_owner
        else:
            return self._surgeon

    @property
    def experiment_owner(self) -> Scientist:
        return self._experiment_owner

    def update_experiment_owner(self, scientist: Scientist) -> None:
        self._experiment_owner = scientist

    @property
    def surgeries(self) -> List[Surgery]:
        return self._surgeries

    def add_surgeries(self, *surgeries: Surgery) -> None:
        for surgery in surgeries:
            if isinstance(surgery, list):
                self._surgeries.extend(surgery)
            else:
                self._surgeries.append(surgery)

    @property
    def notes(self) -> List[Note]:
        return self._notes

    def add_note(self, *notes: Note) -> None:
        for note in notes:
            if isinstance(note, list):
                self._notes.extend(note)
            else:
                self._notes.append(note)

    @property
    def experiments(self) -> List[Experiment]:
        return self._experiments

    def add_experiment(self, *experiments: Experiment) -> None:
        for exp in experiments:
            if isinstance(exp, list):
                self._experiments.extend(exp)
            else:
                self._experiments.append(exp)

    @property
    def data(self) -> Dict[str, Any]:
        data = {
            'unique identifier': self.unique_identifier,
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
            "notes": [note.data for note in self.notes],
            "experiments": [experiment.experiment_data for experiment in self.experiments],

        }
        return data
