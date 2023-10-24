from typing import List, Dict, Any


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
    substance : str
        The name of the drug substance.
    dose : float
        The dose of the drug in milligrams per kilogram of body weight.
    volume_administered : float
        The volume of the drug administered in milliliters.

    Methods
    -------
    drug_data()
        Returns a dictionary containing the drug's substance, dose, and volume administered.
    """

    def __init__(self, substance: str, dose: float, volume_administered: float):
        approved_substances = ["BupeSR", "Bupivicaine", "Meloxicam"]
        if substance not in approved_substances:
            raise ValueError(
                f"Substance not approved, must be one of {approved_substances}")
        self.substance = substance
        self.dose = dose
        self.volume_administered = volume_administered

    @property
    def drug_data(self) -> Dict[str, Any]:
        """
        Returns a dictionary containing the drug's substance, dose, and volume administered.

        Returns
        -------
        dict
            A dictionary containing the drug's substance, dose, and volume administered.
        """
        data = {
            "substance": self.substance,
            "dose (mg/kg)": self.dose,
            "volume administered (mL)": self.volume_administered,
        }
        return data
