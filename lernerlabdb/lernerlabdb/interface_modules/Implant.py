from typing import Optional
from lernerlabdb.interface_modules.Coordinates import Coordinates
from lernerlabdb.interface_modules.enums import ImplantType


class Implant:
    """
        A class to represent a brain implant with specified characteristics.

        ...

        Attributes
        ----------
        type : str
            Type of the implant. Must be one of ['CANNULA', 'OPTO', 'ELECTRODE', 'LENS', 'FIBER_OPTIC', "PELLET"].
        angle : int, optional
            Angle of the implant, by default 90.
        implant_coordinates : Coordinates
            Coordinates of the implant, default is None.

        Methods
        -------
        adjust_implant_coordinates(ap, ml, dv)
            Adjusts the coordinates of the implant.
        __repr__()
            Returns a string representation of the Implant object.

        Examples
        --------
        >>> implant = Implant(type="OPTO")
        >>> print(implant)
        Implant(type = OPTO, angle = 90)

        >>> implant.adjust_implant_coordinates(1, 2, 3)
        >>> print(implant)
        Implant(type = OPTO, angle = 90), Implant Coordinates: Coordinates(ap=1, ml=2, dv=3)
    """

    def __init__(self, type: ImplantType, angle: Optional[int] = 90):

        # ? do we add metrics for the type: ie length, diameter, NA, etc?
        self._type = type
        self.angle = angle
        self.implant_coordinates = None

    @property
    def type(self) -> str:
        return self._type.value

    def adjust_implant_coordinates(self, ap, ml, dv,coordinates = Coordinates):
        """
        Adjusts the coordinates of the implant.

        Parameters
        ----------
        ap : float
            Anteroposterior coordinate.
        ml : float
            Mediolateral coordinate.
        dv : float
            Dorsoventral coordinate.
        """
        self.implant_coordinates = coordinates(ap, ml, dv)

    @property
    def data(self):
        """serves as a substitute for __repr__ for the purpose of json serialization without overriding __dir__ or __repr__

        Returns
        -------
        dict
            dictionary of implant data
        """
        data = {
            "type": self.type,
            "angle": self.angle,
            "coordinates": self.implant_coordinates.coordinates if self.implant_coordinates is not None else None
        }
        return data
