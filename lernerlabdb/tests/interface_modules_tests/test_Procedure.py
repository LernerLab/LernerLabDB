from lernerlabdb.interface_modules.Structure import Structure
from lernerlabdb.interface_modules.Implant import Implant
from lernerlabdb.interface_modules.Injection import Injection
from lernerlabdb.interface_modules.Coordinates import Coordinates
from lernerlabdb.interface_modules.Procedure import Procedure

from lernerlabdb.interface_modules.enums import ImplantType, Hemisphere

# Test Procedure class


@pytest.fixture
def procedure():
    return Procedure("test_procedure", 1)


@pytest.fixture
def structure():
    return Structure("Lateral Hypothalamic Area",
                     "LHA", Hemisphere.LEFT, (-1.6, 0.9, -4.9))


class TestProcedure:

    def test_init(self, procedure):

        assert procedure.name == "test_procedure"
        assert procedure.id == 1
        assert procedure.structures == []

    def test_add_structure(self, procedure, structure):

        procedure.add_structure(structure)
        assert procedure.structures == [structure]
        assert isinstance(procedure.structures[0], Structure)

    def test_procedure_data(self, procedure, structure):

        procedure.add_structure(structure)

        expected_data = {
            "name": "test_procedure",
            "id": 1,
            "structures": {"structure_1": structure.data}
        }
        assert procedure.data == expected_data
