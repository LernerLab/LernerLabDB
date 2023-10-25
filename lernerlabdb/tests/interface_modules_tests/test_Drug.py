
import pytest
from lernerlabdb.interface_modules.Drug import Drug


class TestDrug:
    def test_valid_init(self):
        test_drug = Drug("BupeSR", 0.3, 0.2)
        assert test_drug.substance == "BupeSR"
        assert test_drug.dose == 0.3
        assert test_drug.volume_administered == 0.2

        expected_data = {"substance": "BupeSR",
                         "dose (mg/kg)": 0.3,
                         "volume administered (mL)": 0.2}

        assert test_drug.data == expected_data

    def test_invalid_init(self):
        with pytest.raises(ValueError):
            Drug("Invalid", 0.3, 0.2)
