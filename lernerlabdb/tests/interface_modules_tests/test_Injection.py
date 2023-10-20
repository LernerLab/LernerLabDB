import pytest

from lernerlabdb.interface_modules.Structure import Structure
from lernerlabdb.interface_modules.Coordinates import Coordinates
from lernerlabdb.interface_modules.Injection import Injection


class TestInjection:
    def test_init(self):
        injection = Injection(substrate="aav5-eGFP",
                              type="VIRUS", volume=200, flowrate=100, titer=1.5)
        assert injection.substrate == "AAV5-EGFP"
        assert injection.type == "VIRUS"
        assert injection.volume == 200
        assert injection.flowrate == 100
        assert injection.titer == 1.5
        assert injection.molarity is None

    def test_init_defaults(self):

        defaults = Injection()
        assert defaults.substrate is None
        assert defaults.type is None
        assert defaults.volume == 0
        assert defaults.flowrate == 0
        assert defaults.titer is None
        assert defaults.molarity is None

    def test_invalid_type_init(self):
        with pytest.raises(ValueError):
            invalid = Injection(type="invalid")

    def test_adjust_injection_coordinates(self):
        inj = Injection()
        inj.adjust_injection_coordinates(1, 2, 3)
        inj.injection_coordinates.coordinates == {"AP": 1, "ML": 2, "DV": 3}
        assert isinstance(inj.injection_coordinates, Coordinates)

    def test_injection_data(self):
        inj = Injection(
            substrate = "AAV-dLIGHT1.3b",
            type = 'VIRUS',
            titer = 1.0,
            volume = 500, 
            flowrate = 100)
        inj.adjust_injection_coordinates(1, 2, 3)
        
        expected = {'substrate': 'AAV-DLIGHT1.3B',
        'type': 'VIRUS',
        'volume(nL)': 500,
        'flowrate(nL/min)': 100,
        'titer(e12)': 1.0,
        'molarity(mM)': None,
        'injection_coordinates': {'AP': 1, 'ML': 2, 'DV': 3},
        'injection_angle': 90}
        assert inj.injection_data == expected
        
    def test_injection_data_no_cords(self):
        inj = Injection(
            substrate = "AAV-dLIGHT1.3b",
            type = 'VIRUS',
            titer = 1.0,
            volume = 500, 
            flowrate = 100)
        
        expected = {'substrate': 'AAV-DLIGHT1.3B',
        'type': 'VIRUS',
        'volume(nL)': 500,
        'flowrate(nL/min)': 100,
        'titer(e12)': 1.0,
        'molarity(mM)': None,
        'injection_coordinates': None,
        'injection_angle': 90}
        assert inj.injection_data == expected