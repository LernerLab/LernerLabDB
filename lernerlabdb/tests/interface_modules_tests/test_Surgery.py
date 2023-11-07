from datetime import datetime, date, time
from typing import List, Dict, Any

from lernerlabdb.interface_modules.Drug import Drug
from lernerlabdb.interface_modules.Note import Note
from lernerlabdb.interface_modules.Procedure import Procedure
from lernerlabdb.interface_modules.Surgery import Surgery


@pytest.fixture
def surgery():
    return Surgery(1)


class TestSurgery:
    def test_init(self, surgery):
        assert isinstance(surgery.date, date), "Date property is incorrect."
        assert isinstance(surgery.time_of_surgery,
                          time), "Time property is incorrect."
        assert surgery.surgery_number == 1, "Surgery number property is incorrect."
        assert isinstance(surgery.procedures,
                          list), "Procedures property is not a list."
        assert len(surgery.procedures) == 0, "Procedures property is not empty."
        assert isinstance(surgery.drugs, list), "Drugs property is not a list."
        assert len(surgery.drugs) == 0, "Drugs property is not empty."
        assert isinstance(surgery.notes, list), "Notes property is not a list."
        assert len(surgery.notes) == 0, "Notes property is not empty."

    def test_publics(self, surgery):
        assert surgery.date_string == datetime.now().strftime(
            "%m/%d/%Y"), "Date property is incorrect."
        assert surgery.time_of_surgery_string == datetime.now().strftime(
            "%H:%M"), "Time property is incorrect."

    def test_surgery_data(self, surgery):
        assert surgery.data == {
            "Date": surgery.date,
            "Time of surgery": surgery.time_of_surgery,
            "Surgery number": 1,
            "Procedures": [],
            "Drugs": [],
            "Notes": [],
        }
