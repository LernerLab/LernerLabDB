
from enum import Enum
import pandas as pd
import gspread
from datetime import datetime, date, time, timedelta
from typing import Dict, Any, Optional, Literal, NewType
from lernerlabdb.interface_modules.enums import CageStatus, Location, Sex


Date = NewType('Date', date)
Time = NewType('Time', time)
NumberOfDays = NewType('NumberOfDays', int)
NumberOfWeeks = NewType('NumberOfWeeks', int)


#!TODO Unit testing


class Cage:
    def __init__(self,
                 barcode: int,
                 cage_nickname: str,
                 num_animals: int,
                 sex: Sex,
                 date_of_birth: Date,
                 location: Location,
                 status: CageStatus = CageStatus.ACTIVE,
                 parent_cage_barcode: int = None):
        self._barcode = barcode
        self._cage_nickname = cage_nickname
        self._parent_cage_barcode: Optional[int] = None
        self._num_animals = num_animals
        self._sex = sex
        self._date_of_birth = date_of_birth
        self._location = location
        self._status = status

    @property
    def barcode(self):
        return self._barcode

    @property
    def cage_nickname(self):
        return self._cage_nickname

    @property
    def parent_cage(self):
        return self._parent_cage_barcode

    @parent_cage.setter
    def parent_cage(self, parent_cage):
        self._parent_cage_barcode = parent_cage

    @property
    def num_animals(self):
        return self._num_animals

    @property
    def sex(self):
        return self._sex.value

    @property
    def age(self):
        pass

    @property
    def location(self):
        return self._location.value

    @property
    def status(self):
        return self._status.value

    def change_status(self):
        if self._status == CageStatus.ACTIVE:
            self._status = CageStatus.DEACTIVATED
        else:
            self._status = CageStatus.ACTIVE

    @property
    def data(self):
        data = {
            "barcode'": self.barcode,
            "cage_nickname": self.cage_nickname,
            "parent_cage": self.parent_cage,
            "num_animals": self.num_animals,
            "sex": self.sex,
            "age": self.age,
            "location": self.location,
            "status": self.status
        }
        return data
