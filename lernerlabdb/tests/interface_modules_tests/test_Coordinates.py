from lernerlabdb.interface_modules.Coordinates import Coordinates


class TestCoordinates:
    def test_init(self):
        coordinates = Coordinates(ap=1.0, ml=2.0, dv=3.0)
        zero_coordinates = Coordinates()
        assert coordinates.ap == 1.0
        assert coordinates.ml == 2.0
        assert coordinates.dv == 3.0
        assert zero_coordinates.ap == 0
        assert zero_coordinates.ml == 0
        assert zero_coordinates.dv == 0

    def test_coordinates(self):
        coordinates = Coordinates(ap=1.0, ml=2.0, dv=3.0)
        assert coordinates.coordinates == {"AP": 1.0, "ML": 2.0, "DV": 3.0}
