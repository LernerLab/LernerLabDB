import pytest
from datetime import datetime

from lernerlabdb.interface_modules.note import Note
from lernerlabdb.interface_modules.enums import NoteType


class TestNote:

    def test_note_initialization(self):
        note = Note(type=NoteType.SURGERY, note='This is a test note.')
        assert isinstance(
            note, Note), "Note object was not created successfully."

    def test_note_date_property(self):
        note = Note(NoteType.RECOVERY, note='Testing date property.')
        assert note.date_ == datetime.now().strftime(
            "%m/%d/%Y"), "Date property is incorrect."

    def test_note_time_property(self):
        note = Note(NoteType.RECOVERY, note='Testing time property.')
        current_time = datetime.now().strftime("%H:%M")
        assert note.time_ == current_time, "Time property is incorrect."

    def test_note_data_property(self):
        note = Note(type=NoteType.OTHER, note='Testing note_data property.')
        expected_data = {
            "date": note.date_,
            "time": note.time_,
            "type": 'Other',
            "note": 'Testing note_data property.'
        }
        assert note.data == expected_data, "note_data property is incorrect."
