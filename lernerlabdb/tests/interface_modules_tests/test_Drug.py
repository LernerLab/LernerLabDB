
import pytest
from lernerlabdb.interface_modules.Drug import Drug
from lernerlabdb.interface_modules.enums import DrugType


@pytest.fixture
def drug():
    return Drug(DrugType.BUPESR, 0.3, 0.2)


class TestDrug:
    def test_valid_init(self, drug):

        assert isinstance(drug._substance, DrugType)
        assert drug.substance == "BupeSR"
        assert drug.dose == 0.3
        assert drug.volume_administered == 0.2

        expected_data = {"substance": "BupeSR",
                         "dose (mg/kg)": 0.3,
                         "volume administered (mL)": 0.2}

        assert drug.data == expected_data
