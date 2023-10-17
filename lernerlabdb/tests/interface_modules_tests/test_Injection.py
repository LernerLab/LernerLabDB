import pytest

from lernerlabdb.interface_modules.Structure import Structure
from lernerlabdb.interface_modules.Coordinates import Coordinates
from lernerlabdb.interface_modules.Injection import Injection


class TestInjection:
    def test_init(self):
        injection = Injection(injection_number=1, substrate="aav5-eGFP",
                              type="VIRUS", volume=200, flowrate=100, titer=1.5)
        assert injection.injection_number == 1
        assert injection.substrate == "AAV5-EGFP"
        assert injection.type == "VIRUS"
        assert injection.volume == 200
        assert injection.flowrate == 100
        assert injection.titer == 1.5
        assert injection.molarity is None

    def test_init_defaults(self):

        defaults = Injection()
        assert defaults.injection_number == 1
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

    def test_repr(self):
        injection = Injection(injection_number=1, substrate="aav5-eGFP",
                              type="VIRUS", volume=200, flowrate=100, titer=1.5)
        assumed_repr = "Injection(Injection Number: 1, Subtrate: AAV5-EGFP, Type: VIRUS, Volume: 200nL, Flowrate: 100nL/min, Titer: 1.5e12, Molarity: None mM)"
        assert repr(injection) == assumed_repr

        adjusted_coords = injection.adjust_injection_coordinates(1, 2, 3)
        assert repr(
            injection) == f"{assumed_repr}, Injection Coordinates: Coordinates(AP = 1, ML = 2, DV = 3))"
