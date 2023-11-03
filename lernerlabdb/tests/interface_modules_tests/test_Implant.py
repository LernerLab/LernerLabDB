import pytest
from lernerlabdb.interface_modules.Implant import Implant
from lernerlabdb.interface_modules.Coordinates import Coordinates
from lernerlabdb.interface_modules.enums import ImplantType


class TestImplant:

    def test_init(self):
        implant = Implant(type=ImplantType.OPTO, angle=45)
        assert implant.type == "Opto"
        assert implant.angle == 45
        assert implant.implant_coordinates is None

    def test_init_defaults(self):
        defaults = Implant(type=ImplantType.OPTO)
        assert defaults.type == "Opto"
        assert defaults.angle == 90
        assert defaults.implant_coordinates is None

    def test_adjust_implant_coordinates(self):
        implant = Implant(type=ImplantType.OPTO)
        implant.adjust_implant_coordinates(ap=1, ml=2, dv=3)
        expected = Coordinates(1, 2, 3)

        assert implant.implant_coordinates.coordinates == expected.coordinates
        assert isinstance(implant.implant_coordinates, Coordinates)

    def test_implant_data(self):
        implant = Implant(type=ImplantType.OPTO)
        implant.adjust_implant_coordinates(ap=1, ml=2, dv=3)
        expected = {"type": "Opto", "angle": 90,
                    "coordinates": {"AP": 1, "ML": 2, "DV": 3}}

        assert implant.data == expected

    def test_implant_data_no_coordinates(self):
        implant = Implant(type=ImplantType.OPTO)
        expected = {"type": implant.type, "angle": 90,
                    "coordinates": None}

        assert implant.data == expected
