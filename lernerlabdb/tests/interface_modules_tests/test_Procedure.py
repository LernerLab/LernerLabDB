from lernerlabdb.interface_modules.Structure import Structure
from lernerlabdb.interface_modules.Implant import Implant
from lernerlabdb.interface_modules.Injection import Injection
from lernerlabdb.interface_modules.Coordinates import Coordinates
from lernerlabdb.interface_modules.Procedure import Procedure

# Test Procedure class


class TestProcedure:

    def test_init(self):
        test_procedure = Procedure("test_procedure", 1)
        assert test_procedure.name == "test_procedure"
        assert test_procedure.id == 1
        assert test_procedure.structures == []

    def test_add_structure(self):
        test_procedure = Procedure("test_procedure", 1)
        test_structure = Structure("Lateral Hypothalamic Area",
                                   "LHA", "Left", (-1.6, 0.9, -4.9))
        test_procedure.add_structure(test_structure)
        assert test_procedure.structures == [test_structure]
        assert isinstance(test_procedure.structures[0], Structure)

    def test_procedure_data(self):
        test_procedure = Procedure("test_procedure", 1)
        test_structure = Structure("Lateral Hypothalamic Area",
                                   "LHA", "Left", (-1.6, 0.9, -4.9))
        test_procedure.add_structure(test_structure)

        expected_data = {
            "name": "test_procedure",
            "id": 1,
            "structures": {"structure_1": test_structure.structure_data}
        }
        assert test_procedure.data == expected_data
