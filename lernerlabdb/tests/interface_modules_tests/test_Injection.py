import pytest

from lernerlabdb.interface_modules.Structure import Structure
from lernerlabdb.interface_modules.Coordinates import Coordinates
from lernerlabdb.interface_modules.Injection import Injection
from lernerlabdb.interface_modules.enums import InjectionType


class TestInjection:
    def test_init(self, injection):

        assert injection.substrate == "AAV5-EGFP"
        assert injection.injection_type == "Virus"
        assert injection.volume == 200
        assert injection.flowrate == 100
        assert injection.titer == 1.5
        assert injection.molarity is None

    def test_init_defaults(self):

        defaults = Injection(injection_type=InjectionType.VIRUS)
        assert defaults.substrate is None
        assert defaults.injection_type == "Virus"
        assert defaults.volume == 0
        assert defaults.flowrate == 0
        assert defaults.titer is None
        assert defaults.molarity is None

    def test_adjust_injection_coordinates(self, injection):

        injection.adjust_injection_coordinates(3, 4, 5)
        assert injection.injection_coordinates.coordinates == {
            "AP": 3, "ML": 4, "DV": 5}
        assert isinstance(injection.injection_coordinates, Coordinates)

    def test_injection_data(self, injection):

        injection.adjust_injection_coordinates(1, 2, 3)

        expected = {'substrate': "AAV5-EGFP",
                    'injection_type': 'Virus',
                    'volume(nL)': 200,
                    'flowrate(nL/min)': 100,
                    'titer(e12)': 1.5,
                    'molarity(mM)': None,
                    'injection_coordinates': {'AP': 1, 'ML': 2, 'DV': 3},
                    'injection_angle': 90}
        assert injection.data == expected

    def test_injection_data_no_cords(self):
        injection = Injection(
            substrate="AAV-dLIGHT1.3b",
            injection_type=InjectionType.VIRUS,
            titer=1.0,
            volume=500,
            flowrate=100)

        expected = {'substrate': 'AAV-DLIGHT1.3B',
                    'injection_type': 'Virus',
                    'volume(nL)': 500,
                    'flowrate(nL/min)': 100,
                    'titer(e12)': 1.0,
                    'molarity(mM)': None,
                    'injection_coordinates': None,
                    'injection_angle': 90}
        assert injection.data == expected
