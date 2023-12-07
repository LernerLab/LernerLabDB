import pytest
from lernerlabdb.interface_modules.structure import Structure
from lernerlabdb.interface_modules.implant import Implant
from lernerlabdb.interface_modules.injection import Injection
from lernerlabdb.interface_modules.coordinates import Coordinates
from lernerlabdb.interface_modules.enums import ImplantType, Hemisphere, InjectionType


class TestStructure:
    def test_init(self, structure):
        assert structure.region == "LATERAL HYPOTHALAMIC AREA"
        assert structure.accronym == "LHA"
        assert structure.hemisphere == "Left"
        assert structure.coordinates == {"AP": -1.6, "ML": 0.9, "DV": -4.9}

    def test_valid_instance(self, structure):

        assert isinstance(structure.region, str)
        assert isinstance(structure.accronym, str)
        assert isinstance(structure.hemisphere, str)
        assert isinstance(structure, Structure)
        assert isinstance(structure._coordinates, Coordinates)
        assert isinstance(structure.coordinates, dict)
        assert isinstance(structure._coordinates.ap, float)
        assert isinstance(structure._coordinates.ml, float)
        assert isinstance(structure._coordinates.dv, float)

    def test_add_injection(self, structure, injection):

        structure.add_injections(injection)

        assert len(structure.injections) == 1
        assert structure.injections[0] == injection
        assert structure.number_of_injections == 1

    def test_remove_injection(self, structure, injection):

        structure.add_injections(injection)
        assert len(structure.injections) == 1
        structure.remove_injection(injection)
        assert len(structure.injections) == 0

    def test_add_implant(self, structure, implant):
        structure.add_implants(implant)
        assert len(structure.implants) == 1
        assert structure.implants[0] == implant
        assert structure.number_of_implants == 1

    def test_remove_implant(self, structure, implant):
        structure.add_implants(implant)
        assert len(structure.implants) == 1
        structure.remove_implant(implant)
        structure.implants == []
        structure.number_of_implants == 0

    def test_structure_data(self, structure, injection, injection2, implant):

        injection.adjust_injection_coordinates(1, 2, 3)
        structure.add_injections(injection, injection2)
        implant.adjust_implant_coordinates(1, 2, 3)
        structure.add_implants(implant)
        data = structure.data
        assert data["region"] == "LATERAL HYPOTHALAMIC AREA"
        assert data["accronym"] == "LHA"
        assert data["hemisphere"] == "Left"
        assert data["coordinates"] == {"AP": -1.6, "ML": 0.9, "DV": -4.9}
        assert isinstance(data["injections"], dict)
        assert isinstance(data["implants"], dict)
