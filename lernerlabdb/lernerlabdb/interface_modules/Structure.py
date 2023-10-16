from lernerlabdb.interface_modules.Coordinates import Coordinates
from pprint import pprint


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

    def __init__(self, region: str, accronym: str, hemisphere: str, coordinates: tuple = (None, None, None)):
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

    @property
    def coordinates(self):
        return self._coordinates.coordinates

    def __repr__(self):
        """
        Returns a string representation of the structure object.

        Returns:
            str: A string representation of the structure object.
        """

        return f"region = {self.region}, accronym = {self.accronym}, hemisphere = {self.hemisphere}, coordinates = {self.coordinates}"
