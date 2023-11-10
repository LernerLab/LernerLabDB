import pytest
from lernerlabdb.interface_modules.Implant import Implant
from lernerlabdb.interface_modules.Coordinates import Coordinates
from lernerlabdb.interface_modules.enums import ImplantType


class TestImplant:

    def test_init(self, implant):
        assert implant.implant_type == 'Opto'
        assert implant.angle == 90
        assert implant.implant_coordinates is None

    def test_adjust_implant_coordinates(self, implant):
        implant.adjust_implant_coordinates(ap=2, ml=3, dv=4)
        expected = Coordinates(2, 3, 4)

        assert implant.implant_coordinates.coordinates == expected.coordinates
        assert isinstance(implant.implant_coordinates, Coordinates)

    def test_implant_data(self, implant):
        implant.adjust_implant_coordinates(ap=1, ml=2, dv=3)
        expected = {"implant_type": "Opto", "angle": 90,
                    "coordinates": {"AP": 1, "ML": 2, "DV": 3}}

        assert implant.data == expected

    def test_implant_data_no_coordinates(self, implant):
        expected = {"implant_type": implant.implant_type, "angle": 90,
                    "coordinates": None}

        assert implant.data == expected
