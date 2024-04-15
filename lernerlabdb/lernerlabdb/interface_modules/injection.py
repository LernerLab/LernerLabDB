from lernerlabdb.interface_modules.coordinates import Coordinates
from typing import List, Optional
from lernerlabdb.interface_modules.enums import InjectionType


class Injection:
    """
    A class used to represent an Injection, encompassing details such as 
    substrate, type, volume, flowrate, titer, and molarity of the injection.

    Attributes
    ----------
    injection_number : int, optional
        Unique identifier for the injection, by default 1
    substrate : str, optional
        Substrate where the injection is applied, by default None
    injection_type : str, optional
        Type of injection (e.g., "virus", "tracer", "dye", "cytotoxic", "drug", "other"), 
        by default None
    volume : int, optional
        Volume of the injection in nL, by default 0
    flowrate : int, optional
        Flowrate of the injection in nL/min, by default 0
    titer : float, optional
        Titer of the injection, by default None
    molarity : float, optional
        Molarity of the injection, by default None
    injection_coordinates : Coordinates, optional
        Coordinates where the injection is applied, by default None
    injection_angle : int, optional
        Angle of the injection, by default 90 degress

    Methods
    -------
    adjust_injection_coordinates(ap, ml, dv)
        Adjusts the coordinates of the injection.

    Examples
    --------
    >>> injection1 = Injection(injection_number=1, substrate="aav5-eGFP", type="virus", volume=200, flowrate=100, titer=1.5)
    >>> print(injection1)
    Injection(Injection Number: 1, Subtrate: eGFP, Type: virus, Volume: 200nL, Flowrate: 100nL/min, Titer: 1.5e12, Molarity: None mM)

    >>> injection1.adjust_injection_coordinates(1, 2, 3)
    >>> print(injection1)
    Injection(Injection Number: 1, Subtrate: avv5-eGFP, Type: virus, Volume: 200nL, Flowrate: 100nL/min, Titer: 1.5e12, Molarity: None mM, Injection Coordinates: Coordinates(AP: 1, ML: 2, DV: 3))
    """

    def __init__(self,
                 injection_type: InjectionType,
                 substrate: Optional[str] = None,
                 volume: int = 0,
                 flowrate: int = 0,
                 titer: Optional[float] = None,
                 molarity: Optional[float] = None):

        self._injection_type = injection_type
        self.substrate = None if substrate is None else substrate.upper()
        self.volume = volume
        self.flowrate = flowrate
        self.titer = titer
        self.molarity = molarity
        self.injection_coordinates = None
        self.injection_angle = 90

    @property
    def injection_type(self) -> str:
        """
        Returns the type of injection

        """
        return self._injection_type.value

    def adjust_injection_coordinates(self, ap, ml, dv):
        """
        Pseodo setter for injection_coordinates. Adjusts the coordinates where the injection is applied.

        """
        self.injection_coordinates = Coordinates(
            ap, ml, dv)  # ! TODO this should be injected, not created here

    @property
    def data(self) -> dict:
        """
        Returns a dictionary representation of the injection data.

        """
        data = {
            "substrate": self.substrate,
            "injection_type": self.injection_type,
            "volume(nL)": self.volume,
            "flowrate(nL/min)": self.flowrate,
            "titer(e12)": self.titer,
            "molarity(mM)": self.molarity,
            "injection_coordinates": None if self.injection_coordinates is None else self.injection_coordinates.coordinates,
            "injection_angle": self.injection_angle
        }
        return data
