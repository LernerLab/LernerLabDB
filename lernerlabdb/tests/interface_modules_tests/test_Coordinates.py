from lernerlabdb.interface_modules.coordinates import Coordinates


class TestCoordinates:
    def test_default_init(self, default_coordinates):

        assert default_coordinates.ap == 0
        assert default_coordinates.ml == 0
        assert default_coordinates.dv == 0
        assert default_coordinates.angle == 0

    def test_init_(self, coordinates):
        assert coordinates.dv == 3.0
        assert coordinates.ap == 1.0
        assert coordinates.ml == 2.0
        assert coordinates.angle == 0.0

    def test_coordinates_property(self, coordinates):
        assert coordinates.coordinates == {
            "AP": 1.0, "ML": 2.0, "DV": 3.0, "Angle": 0.0}
