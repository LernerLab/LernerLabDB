from lernerlabdb.interface_modules.Coordinates import Coordinates
from lernerlabdb.interface_modules.Injection import Injection
from lernerlabdb.interface_modules.Implant import Implant

from typing import Optional, List




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

    def __init__(self, region: str,
                 accronym: str,
                 hemisphere: str,
                 coordinates: tuple = (None, None, None)):
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
        try:

            ''' This block checks for valid hemisphere input. 
            It is contrained to left, right bilateral, or none.
            It will take in any case and convert it to upper case full word.'''
            if hemisphere is not None:
                hemisphere = hemisphere.upper()
            if hemisphere == 'L':
                hemisphere = 'LEFT'
            elif hemisphere == 'R':
                hemisphere = 'RIGHT'
            elif hemisphere == 'B':
                hemisphere = 'BILATERAL'

            assert hemisphere in ["LEFT", "RIGHT", 'BILATERAL', None]
            self.hemisphere = hemisphere
        except AssertionError as e:
            print(
                "Invalid hemisphere input. Please enter 'Left', 'Right', 'Bilateral', or None.")

        self._coordinates = Coordinates(
            coordinates[0], coordinates[1], coordinates[2])

        self._injections = []
        self._implants = []

    @property
    def coordinates(self):
        return self._coordinates.coordinates

    @property
    def injections(self):
        return self._injections

    @property
    def number_of_injections(self):
        return len(self._injections)

    def add_injection(self, injection: Injection):
        self._injections.append(injection)

    def remove_injection(self, injection: Injection):
        self._injections.remove(injection)

    @property
    def implants(self):
        return self._implants

    @property
    def number_of_implants(self):
        return len(self._implants)

    def add_implant(self, implant: Implant):
        self._implants.append(implant)

    def remove_implant(self, implant: Implant):
        self._implants.remove(implant)

    @property
    def structure_data(self):
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
            "injections": {f"injection_{i+1}": inj.injection_data for i, inj in enumerate(self.injections)},
            "implants": {f"implant_{i+1}": imp.implant_data for i, imp in enumerate(self.implants) if imp is not None},
        }
        return data
