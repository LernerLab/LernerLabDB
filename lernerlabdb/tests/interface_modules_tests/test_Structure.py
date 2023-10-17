import pytest
from lernerlabdb.interface_modules.Structure import Structure
from lernerlabdb.interface_modules.Coordinates import Coordinates


class TestStructure:

    def test_init(self):

        structure = Structure("Lateral Hypothalamic Area",
                              "LHA", "Left", (-1.6, 0.9, -4.9))
        assert structure.region == "LATERAL HYPOTHALAMIC AREA"
        assert structure.accronym == "LHA"
        assert structure.hemisphere == "LEFT"
        assert structure.coordinates == {"AP": -1.6, "ML": 0.9, "DV": -4.9}

    def test_invalid_hemisphere(self, capsys):
        s = Structure("Lateral Hypothalamic Area", "LHA",
                      "InvalidInput", (-1.6, 0.9, -4.9))
        captured = capsys.readouterr()
        assert captured.out == "Invalid hemisphere input. Please enter 'Left', 'Right', 'Bilateral', or None.\n"

    def test_valid_instance(self):
        structure = Structure("Lateral Hypothalamic Area",
                              "LHA", "Left", (-1.6, 0.9, -4.9))

        assert isinstance(structure.region, str)
        assert isinstance(structure.accronym, str)
        assert isinstance(structure.hemisphere, str)
        assert isinstance(structure, Structure)
        assert isinstance(structure._coordinates, Coordinates)
        assert isinstance(structure.coordinates, dict)
        assert isinstance(structure._coordinates.ap, float)
        assert isinstance(structure._coordinates.ml, float)
        assert isinstance(structure._coordinates.dv, float)

        structure = Structure("Lateral Hypothalamic Area",
                              "LHA", "Left", (-1.6, 0.9, -4.9))
        assert structure.__repr__(
        ) == "Structure(region = LATERAL HYPOTHALAMIC AREA, accronym = LHA, hemisphere = LEFT, coordinates = {'AP': -1.6, 'ML': 0.9, 'DV': -4.9})"
