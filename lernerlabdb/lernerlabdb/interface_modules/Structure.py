from lernerlabdb.interface_modules.coordinates import Coordinates
from lernerlabdb.interface_modules.injection import Injection
from lernerlabdb.interface_modules.implant import Implant
from lernerlabdb.interface_modules.enums import ImplantType, Hemisphere

from typing import Optional, List, Tuple


class Structure:
    """
    Represents a brain structure and its associated coordinates.

    Attributes:
        region (str): The region of the brain structure.
        acronym (str): The acronym of the brain structure.
        hemisphere (str): The hemisphere of the brain structure.
        coordinates (dict): The coordinates of the brain structure.

    Example Usage:
        # Create a structure object with coordinates
        structure1 = Structure("Hippocampus", "HIP", "Left", (2.5, 1.0, -3.0))
        print(structure1)
        # Output: region = Hippocampus, accronym = HIP, hemisphere = Left, coordinates = Coordinates(AP = 2.5, ML = 1.0, DV = -3.0)

        # Create a structure object without coordinates
        structure2 = Structure("Cortex", "CTX", "Right")
        print(structure2)
        # Output: region = Cortex, accronym = CTX, hemisphere = Right, coordinates = Coordinates not logged. Please log coordinates.
    """
    accronym: str
    hemisphere: Hemisphere
    corrdiates: Tuple[float]

    def __init__(self, region,
                 accronym,
                 hemisphere,
                 coordinates):
        """
        Initializes a structure object with the given region, acronym, hemisphere, and coordinates.

        Args:
            region (str): The region of the brain structure.
            accronym (str): The acronym of the brain structure.
            hemisphere (str): The hemisphere of the brain structure.
            coordinates (tuple, optional): The coordinates of the brain structure. Defaults to (None, None, None).
        """
        self.region = region.upper()
        self.accronym = accronym.upper()
        self._hemisphere = hemisphere
        self._coordinates = Coordinates(
            coordinates[0], coordinates[1], coordinates[2])
        self._injections = []
        self._implants = []

    @property
    def hemisphere(self):
        return self._hemisphere.value

    @property
    def coordinates(self):
        return self._coordinates.coordinates

    @property
    def injections(self):
        return self._injections

    @property
    def number_of_injections(self):
        return len(self._injections)

    def add_injections(self, *injections: Injection):

        for injection in injections:
            if isinstance(injection, list):
                self._injections.extend(injection)
            else:
                self._injections.append(injection)

    def remove_injection(self, injection: Injection):
        self._injections.remove(injection)

    @property
    def implants(self):
        return self._implants

    @property
    def number_of_implants(self):
        return len(self._implants)

    def add_implants(self, *implants: Implant):
        for implant in implants:
            if isinstance(implant, list):
                self._implants.extend(implant)
            else:
                self._implants.append(implant)

    def remove_implant(self, implant: Implant):
        self._implants.remove(implant)

    @property
    def data(self):
        '''serves as a substitute for __repr__ for the purpose of json serialization without overriding __dir__ or __repr__
            Parameters
            ----------
            self : Structure
                The current instance of the Structure class.
            Returns
            -------
            dict
                A dictionary containing the structure data with all attached class data.

        '''
        data = {
            "region": self.region,
            "accronym": self.accronym,
            "hemisphere": self.hemisphere,
            "coordinates": self.coordinates,
            "injections": {f"injection_{i+1}": inj.data for i, inj in enumerate(self.injections)},
            "implants": {f"implant_{i+1}": imp.data for i, imp in enumerate(self.implants) if imp is not None},
        }
        return data
