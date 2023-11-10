from typing import Dict, Any
from lernerlabdb.interface_modules.enums import DrugType


class Drug:
    """
    A class representing a drug.

    Parameters
    ----------
    substance : str
        The name of the drug substance.
    dose : float
        The dose of the drug in milligrams per kilogram of body weight.
    volume_administered : float
        The volume of the drug administered in milliliters.

    Raises
    ------
    ValueError
        If the substance is not one of the approved substances.

    Attributes
    ----------
    substance : LiteralString
        returns "BupeSR", "Bupivicaine", or "Meloxicam".
    dose : float
        The dose of the drug in milligrams per kilogram of body weight.
    volume_administered : float
        The volume of the drug administered in milliliters.

    Methods
    -------
    drug_data()
        Returns a dictionary containing the drug's substance, dose, and volume administered.
    """

    def __init__(self,
                 substance: DrugType,
                 dose: float,
                 volume_administered: float):

        self._substance = substance
        self.dose = dose
        self.volume_administered = volume_administered

    @property
    def substance(self) -> str:
        """
        returns the substance of the drug : BupeSR, Bupivicaine, or Meloxicam
        """
        return self._substance.value

    @property
    def data(self) -> Dict[str, Any]:
        """
        Returns a dictionary containing the drug's substance, dose, and volume administered.

        """
        data = {
            "substance": self.substance,
            "dose (mg/kg)": self.dose,
            "volume administered (mL)": self.volume_administered,
        }
        return data
