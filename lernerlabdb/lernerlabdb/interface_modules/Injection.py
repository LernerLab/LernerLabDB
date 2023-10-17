from lernerlabdb.interface_modules.Structure import Structure
from lernerlabdb.interface_modules.Coordinates import Coordinates


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
                 injection_number=1,
                 substrate: str = None,
                 type: str = None,
                 volume: int = 0,
                 flowrate: int = 0,
                 titer: float = None,
                 molarity: float = None):
        self.injection_number = injection_number
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

    def __repr__(self):

        repr = f"Injection(Injection Number: {self.injection_number}, Subtrate: {self.substrate}, Type: {self.type}, Volume: {self.volume}nL, Flowrate: {self.flowrate}nL/min, Titer: {self.titer}e12, Molarity: {self.molarity} mM)"
        if self.injection_coordinates is None:
            return repr
        else:
            return f"{repr}, Injection Coordinates: {self.injection_coordinates})"
