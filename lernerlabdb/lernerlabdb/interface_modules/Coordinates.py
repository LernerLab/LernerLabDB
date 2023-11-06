from typing import Dict


class Coordinates:
    def __init__(self, ap: float = 0., ml: float = 0., dv: float = 0.):
        self.ap: float = ap
        self.ml: float = ml
        self.dv: float = dv

    @property
    def coordinates(self) -> Dict[str, float]:
        # if self.ap is None or self.ml is None or self.dv is None:
        #     return "Coordinates not logged. Please log coordinates."
        coordinates = {"AP": self.ap, "ML": self.ml, "DV": self.dv}
        return coordinates
