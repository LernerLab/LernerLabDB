

class Coordinates:
    def __init__(self, ap: float = None, ml: float = None, dv: float = None):
        self.ap = ap
        self.ml = ml
        self.dv = dv

    def __repr__(self):
        if self.ap is None or self.ml is None or self.dv is None:
            return "Coordinates not logged. Please log coordinates."
        return f"Coordinates(AP = {self.ap}, ML = {self.ml}, DV = {self.dv})"

    @property
    def coordinates(self) -> dict:
        if self.ap is None or self.ml is None or self.dv is None:
            return "Coordinates not logged. Please log coordinates."
        coordinates = {"AP": self.ap, "ML": self.ml, "DV": self.dv}
        return coordinates

