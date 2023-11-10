from typing import Dict


class Coordinates:
    """
    a class to represent coordinates of a brain structure
    
    Parameters
    ----------
    ap : float default 0.
        Anteroposterior coordinate
    ml : float
        Mediolateral coordinate
    dv : float
        Dorsoventral coordinate
        
    Attributes
    ----------
    ap : float
        Anteroposterior coordinate
    ml : float
        Mediolateral coordinate
    dv : float
        Dorsoventral coordinate
    coordinates : Dict[str, float]
        A dictionary containing the all coordinates of the structure
    
    Examples
    --------
    >>> coordinates = Coordinates(1, 2, 3)
    >>> coordinates.coordinates
    {'AP': 1, 'ML': 2, 'DV': 3}

    """

    def __init__(self, ap=0., ml=0., dv=0.):
        self.ap = ap
        self.ml = ml
        self.dv = dv

    @property
    def coordinates(self) -> Dict[str, float]:
        """
        returns a dictionary of all coordinates
        """
        coordinates = {"AP": self.ap, "ML": self.ml, "DV": self.dv}
        return coordinates
