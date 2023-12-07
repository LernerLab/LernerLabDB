from datetime import datetime, date, time
from typing import List, Dict, Any

from lernerlabdb.interface_modules.drug import Drug
from lernerlabdb.interface_modules.note import Note
from lernerlabdb.interface_modules.procedure import Procedure
from lernerlabdb.interface_modules.surgery import Surgery


class TestSurgery:
    def test_init(self, surgery1):
        assert isinstance(surgery1.date, date), "Date property is incorrect."
        assert isinstance(surgery1.time_of_surgery,
                          time), "Time property is incorrect."
        assert surgery1.surgery_number == 1, "Surgery number property is incorrect."
        assert isinstance(surgery1.procedures,
                          list), "Procedures property is not a list."
        assert len(surgery1.procedures) == 0, "Procedures property is not empty."
        assert isinstance(
            surgery1.drugs, list), "Drugs property is not a list."
        assert len(surgery1.drugs) == 0, "Drugs property is not empty."
        assert isinstance(
            surgery1.notes, list), "Notes property is not a list."
        assert len(surgery1.notes) == 0, "Notes property is not empty."

    def test_publics(self, surgery1):
        assert surgery1.date_string == datetime.now().strftime(
            "%m/%d/%Y"), "Date property is incorrect."
        assert surgery1.time_of_surgery_string == datetime.now().strftime(
            "%H:%M"), "Time property is incorrect."

    def test_surgery_data(self, surgery1):
        assert surgery1.data == {
            "Date": surgery1.date,
            "Time of surgery": surgery1.time_of_surgery,
            "Surgery number": 1,
            "Procedures": [],
            "Drugs": [],
            "Notes": [],
        }
