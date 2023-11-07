from lernerlabdb.interface_modules.Coordinates import Coordinates


@pytest.fixture
def default_coordinates():
    return Coordinates()


@pytest.fixture
def coordinates():
    return Coordinates(ap=1.0, ml=2.0, dv=3.0)


class TestCoordinates:
    def test_default_init(self, defualt_coordinates):

        assert default_coordinates.ap == 0
        assert default_coordinates.ml == 0
        assert default_coordinates.dv == 0

    def test_init_(self, coordinates):
        assert coordinates.ap == 1.0
        assert coordinates.ml == 2.0
        assert coordinates.dv == 3.0

    def test_coordinates_property(self, coordinates):
        assert coordinates.coordinates == {"AP": 1.0, "ML": 2.0, "DV": 3.0}
