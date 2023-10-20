from lernerlabdb.interface_modules.Coordinates import Coordinates
from typing import List, Optional


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
    type : str, optional
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
                 substrate: Optional[str] = None,
                 type: Optional[str] = None,
                 volume: int = 0,
                 flowrate: int = 0,
                 titer: Optional[float] = None,
                 molarity: Optional[float] = None):
        # ? do we want the options to be enforced from internal data or user input?
        self.substrate = None if substrate is None else substrate.upper()

        # ? we could have this just be a dropdown selecteion in the UI
        possible_types = ["VIRUS", "TRACER",
                          "DYE", 'CYTOTOXIC', "DRUG", "OTHER"]

        if type not in possible_types and type is not None:
            raise ValueError(
                f"Invalid type. Please enter one of the following: {possible_types}")

        self.type = type
        self.volume = volume
        self.flowrate = flowrate
        self.titer = titer
        self.molarity = molarity
        self.injection_coordinates = None
        self.injection_angle = 90  # TODO update unit testing

    def adjust_injection_coordinates(self, ap, ml, dv):
        """
        Adjusts the coordinates where the injection is applied.

        Parameters
        ----------
        ap : float
            Anteroposterior coordinate
        ml : float
            Mediolateral coordinate
        dv : float
            Dorsoventral coordinate
        """
        self.injection_coordinates = Coordinates(ap, ml, dv)



    @property
    def injection_data(self) -> dict:
        """
        ### Returns the injection data as a dictionary.
        serves as a substitute for __repr__ for the purpose of json serialization without overriding __dir__ or __repr__

        Parameters
        ----------
        self : Injection
            The current instance of the Injection class.

        Returns
        -------
        dict
            A dictionary containing the injection data.
        """
        data = {
            "substrate": self.substrate,
            "type": self.type,
            "volume(nL)": self.volume,
            "flowrate(nL/min)": self.flowrate,
            "titer(e12)": self.titer,
            "molarity(mM)": self.molarity,
            "injection_coordinates": None if self.injection_coordinates is None else self.injection_coordinates.coordinates,
            "injection_angle": self.injection_angle
        }
        return data
