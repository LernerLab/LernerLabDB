import pytest
from lernerlabdb.interface_modules.Implant import Implant
from lernerlabdb.interface_modules.Coordinates import Coordinates


class TestImplant:

    def test_init(self):
        implant = Implant(type="OPTO", angle=45)
        assert implant.type == "OPTO"
        assert implant.angle == 45
        assert implant.implant_coordinates is None

    def test_init_defaults(self):
        defaults = Implant(type="OPTO")
        assert defaults.type == "OPTO"
        assert defaults.angle == 90
        assert defaults.implant_coordinates is None

    def test_invalid_type_init(self):
        with pytest.raises(ValueError):
            invalid = Implant(type="invalid")

    def test_adjust_implant_coordinates(self):
        implant = Implant(type="OPTO")
        implant.adjust_implant_coordinates(1, 2, 3)
        expected = Coordinates(1, 2, 3)

        assert implant.implant_coordinates.coordinates == expected.coordinates
        assert isinstance(implant.implant_coordinates, Coordinates)

    def test_repr(self):
        implant = Implant(type="OPTO")
        assert repr(implant) == "Implant(type = OPTO, angle = 90)"
        added_coordinates = implant.adjust_implant_coordinates(1, 2, 3)
        assert repr(
            implant) == "Implant(type = OPTO, angle = 90), Implant Coordinates: Coordinates(AP = 1, ML = 2, DV = 3))"
