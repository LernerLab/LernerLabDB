class Drug:
    def __init__(self, substance, dose,  volume_administered):
        approved_substances = ["BupeSR", "Bupivicaine", "Meloxicam"]
        if substance not in approved_substances:
            raise ValueError(
                f"Substance not approved, must be one of {approved_substances}")
        self.substance = substance
        self.dose = dose
        self.volume_administered = volume_administered

    @property
    def drug_data(self):
        data = {
            "substance": self.substance,
            "dose (mg/kg)": self.dose,
            "volume administered (mL)": self.volume_administered,
        }
        return data
