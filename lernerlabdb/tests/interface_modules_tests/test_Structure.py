import pytest
from lernerlabdb.interface_modules.Structure import Structure
from lernerlabdb.interface_modules.Implant import Implant
from lernerlabdb.interface_modules.Injection import Injection
from lernerlabdb.interface_modules.Coordinates import Coordinates
from lernerlabdb.interface_modules.enums import ImplantType, Hemisphere, InjectionType


@pytest.fixture
def structure():
    return Structure("Lateral Hypothalamic Area",
                     "LHA", Hemisphere.LEFT, (-1.6, 0.9, -4.9))


@pytest.fixture
def injection():
    return Injection(substrate="AAV-dLIGHT1.3b", type=InjectionType.VIRUS,
                     titer=1.0, volume=500, flowrate=100)


@pytest.fixture
def implant():
    return Implant(type=ImplantType.OPTO)


class TestStructure:
    def test_init(self, structure):
        assert structure.region == "LATERAL HYPOTHALAMIC AREA"
        assert structure.accronym == "LHA"
        assert structure.hemisphere == "Left"
        assert structure.coordinates == {"AP": -1.6, "ML": 0.9, "DV": -4.9}

    def test_valid_instance(self, structure):

        assert isinstance(structure.region, str)
        assert isinstance(structure.accronym, str)
        assert (isinstance(structure._hemisphere, Hemisphere))
        assert isinstance(structure.hemisphere, str)
        assert isinstance(structure, Structure)
        assert isinstance(structure._coordinates, Coordinates)
        assert isinstance(structure.coordinates, dict)
        assert isinstance(structure._coordinates.ap, float)
        assert isinstance(structure._coordinates.ml, float)
        assert isinstance(structure._coordinates.dv, float)

    def test_add_injection(self, structure, injection):

        structure.add_injection(injection)

        assert len(structure.injections) == 1
        assert structure.injections[0] == injection
        assert structure.number_of_injections == 1

    def test_remove_injection(self, structure, injection):

        structure.add_injection(injection)
        assert len(structure.injections) == 1
        structure.remove_injection(injection)
        assert len(structure.injections) == 0

    def test_add_implant(self, structure, implant):
        structure.add_implant(implant)
        assert len(structure.implants) == 1
        assert structure.implants[0] == implant
        assert structure.number_of_implants == 1

    def test_remove_implant(self, structure, implant):
        structure.add_implant(implant)
        assert len(structure.implants) == 1
        structure.remove_implant(implant)
        structure.implants == []
        structure.number_of_implants == 0

    def test_structure_data(self, structure, injection, implant):

        injection.adjust_injection_coordinates(1, 2, 3)
        structure.add_injection(injection)
        implant.adjust_implant_coordinates(1, 2, 3)
        structure.add_implant(implant)

        expected_data = {'region': 'LATERAL HYPOTHALAMIC AREA',
                         'accronym': 'LHA',
                         'hemisphere': 'Left',
                         'coordinates': {'AP': -1.6, 'ML': 0.9, 'DV': -4.9},
                         'injections': {'injection_1': {'substrate': 'AAV-DLIGHT1.3B',
                                                        'type': 'Virus',
                                                        'volume(nL)': 500,
                                                        'flowrate(nL/min)': 100,
                                                        'titer(e12)': 1.0,
                                                        'molarity(mM)': None,
                                                        'injection_coordinates': {'AP': 1, 'ML': 2, 'DV': 3},
                                                        'injection_angle': 90}},
                         'implants': {'implant_1': {'type': 'Opto',
                                                    'angle': 90,
                                                    'coordinates': {'AP': 1, 'ML': 2, 'DV': 3}}}
                         }
        assert structure.data == expected_data
