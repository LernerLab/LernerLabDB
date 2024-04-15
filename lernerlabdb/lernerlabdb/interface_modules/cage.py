
import pandas as pd
from datetime import datetime, date, time, timedelta
from typing import Dict, Any, Optional, Literal, NewType

from lernerlabdb.customs.custom_types import Date, Time, NumberOfDays, NumberOfWeeks
from lernerlabdb.interface_modules.enums import CageStatus, Location, Sex, Genotype
# git test for file rename


class Cage:
    # write a docstring for this class

    """
    A class representing a mouse cage within a laboratory environment.

    Parameters
    ----------
    barcode : int
        The unique identifier for the cage.
    cage_nickname : str
        A user-friendly name for the cage.
    num_animals : int
        The number of animals in the cage.
    genotype : Genotype
        The genotype of the mice in the cage, as defined in the Genotype enum.
    sex : Sex
        The sex of the mice in the cage, as defined in the Sex enum.
    date_of_birth : Date
        The date of birth of the mice, wrapped in a NewType of date.
    location : Location
        The current location of the cage, as defined in the Location enum.
    status : CageStatus, optional
        The status of the cage, as defined in the CageStatus enum. Defaults to CageStatus.ACTIVE.
    parent_cage_barcode : int, optional
        The barcode of the parent cage, if applicable. Defaults to None.

    Attributes
    ----------
    barcode : int
        The barcode of the cage.
    cage_nickname : str
        The nickname of the cage.
    parent_cage_barcode : int or None
        The barcode of the parent cage, if any.
    num_animals : int
        The number of animals in the cage.
    genotype : str
        The genotype of the mice, obtained from the Genotype enum.
    sex : str
        The sex of the mice, obtained from the Sex enum.
    date_of_birth : Date
        The date of birth of the mice.
    location : str
        The location of the cage, obtained from the Location enum.
    status : str
        The status of the cage, obtained from the CageStatus enum.

    Methods
    -------
    change_status()
        Toggles the status of the cage between ACTIVE and DEACTIVATED.

    data
        Property that returns a dictionary of the cage's attributes.

    Examples
    --------
    >>> cage = Cage(12345, 'TestCage', 5, Genotype.WildType, Sex.Female, Date(2021, 1, 1), Location.Lab, CageStatus.ACTIVE)
    >>> cage.change_status()
    >>> cage.status
    'DEACTIVATED'
    >>> cage.data
    {'barcode': 12345, 'cage_nickname': 'TestCage', 'parent_cage': None, 'num_animals': 5, 'genotype': 'WildType', 'sex': 'Female', 'age': None, 'location': 'Lab', 'status': 'DEACTIVATED'}
    """

    def __init__(self,
                 barcode: int,
                 cage_nickname: str,
                 num_animals: int,
                 genotype: Genotype,
                 sex: Sex,
                 date_of_birth: Date,
                 location: Location,
                 status: CageStatus,
                 parent_cage_barcode: Optional[int] = None):

        self._barcode = barcode
        self._cage_nickname = cage_nickname
        self._parent_cage_barcode: Optional[int] = None
        self._num_animals = num_animals
        self._genotype = genotype
        self._sex = sex
        self._date_of_birth = date_of_birth
        self._location = location
        self._status = status
        self.parent_cage_barcode = parent_cage_barcode

    @property
    def barcode(self) -> int:
        """
        returns the barcode value.
        """

        return self._barcode

    @property
    def cage_nickname(self) -> str:
        """
        returns the cage_nickname
        """

        return self._cage_nickname

    @property
    def parent_cage(self) -> int:
        """
        reuturns the parent cage barcode
        """

        return self._parent_cage_barcode

    def update_parent_cage(self, new_barcode: int) -> None:
        """
        pseudo setter for the parent cage if it needs to be changed
        """
        self._parent_cage_barcode = new_barcode

    @property
    def num_animals(self) -> int:
        """
        Returns the value of the 'num_animals' property.
        """
        return self._num_animals

    @property
    def genotype(self) -> str:
        """
        returns the Genotype value
        """
        return self._genotype.value

    @property
    def sex(self) -> str:
        """
        returns the Sex value
        """
        return self._sex.value

    # ? not implemented. Do we want this?
    @property
    def age(self):
        """
        this is not implemented currently
        """
        raise NotImplementedError

    @property
    def location(self) -> str:
        """
        returs the Location value
        """
        return self._location.value

    @property
    def status(self) -> str:
        """
        returns the CageStatus value
        """
        return self._status.value

    def change_status(self) -> None:
        """
        Toggles the status of the cage between ACTIVE and DEACTIVATED.

        """
        if self._status == CageStatus.ACTIVE:
            self._status = CageStatus.DEACTIVATED
        else:
            self._status = CageStatus.ACTIVE

    @property
    def data(self) -> Dict[str, Any]:
        """
        returns a dictionary of the Cage's attributes
        """
        data = {
            "barcode": self.barcode,
            "cage_nickname": self.cage_nickname,
            "parent_cage": self.parent_cage,
            "num_animals": self.num_animals,
            'genotype': self.genotype,
            "sex": self.sex,
            # "age": self.age,
            "location": self.location,
            "status": self.status
        }
        return data
