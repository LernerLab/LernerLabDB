
import pytest
from lernerlabdb.interface_modules.structure import Structure
from lernerlabdb.interface_modules.implant import Implant
from lernerlabdb.interface_modules.injection import Injection
from lernerlabdb.interface_modules.coordinates import Coordinates
from lernerlabdb.interface_modules.procedure import Procedure

from lernerlabdb.interface_modules.enums import ImplantType, Hemisphere

# Test Procedure class


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
