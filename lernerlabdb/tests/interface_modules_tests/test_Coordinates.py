from lernerlabdb.interface_modules.Coordinates import Coordinates


class TestCoordinates:
    def test_init(self):
        coordinates = Coordinates(ap=1.0, ml=2.0, dv=3.0)
        none_coordinates = Coordinates()
        assert coordinates.ap == 1.0
        assert coordinates.ml == 2.0
        assert coordinates.dv == 3.0
        assert none_coordinates.ap is None
        assert none_coordinates.ml is None
        assert none_coordinates.dv is None

    def test_repr(self):
        coordinates = Coordinates(ap=1.0, ml=2.0, dv=3.0)
        assert repr(coordinates) == "Coordinates(AP = 1.0, ML = 2.0, DV = 3.0)"

    def test_coordinates(self):
        coordinates = Coordinates(ap=1.0, ml=2.0, dv=3.0)
        assert coordinates.coordinates == {"AP": 1.0, "ML": 2.0, "DV": 3.0}

    def test_reper_none(self):
        coordinates = Coordinates()
        assert repr(
            coordinates) == "Coordinates not logged. Please log coordinates."

    def test_coordinates_none(self):
        coordinates = Coordinates()
        assert coordinates.coordinates == "Coordinates not logged. Please log coordinates."
