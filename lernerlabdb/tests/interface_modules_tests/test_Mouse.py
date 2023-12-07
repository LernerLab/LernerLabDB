from datetime import datetime, date
import pytest
from unittest.mock import Mock, patch
import uuid

from lernerlabdb.interface_modules.mouse import Mouse
from lernerlabdb.interface_modules.cage import Cage
from lernerlabdb.interface_modules.surgery import Surgery
from lernerlabdb.interface_modules.note import Note
from lernerlabdb.interface_modules.experiment import Experiment
from lernerlabdb.interface_modules.scientist import Scientist
from lernerlabdb.interface_modules.enums import Sex, Zygosity, MouseStatus, Genotype, Location, CageStatus, NoteType

# TODO finish conftests and run tests


class TestMouse:

    def test_init(self, mouse1):
        assert mouse1.age_ == {
            "days": (datetime.now() - mouse1.date_of_birth).days,
            'weeks': ((datetime.now() - mouse1.date_of_birth).days)//7,
            'days since first surgery': 0,
            'weeks since first surgery': 0}
        assert isinstance(mouse1._unique_id, uuid.UUID)
        assert isinstance(mouse1.unique_id, str)
        assert mouse1.sex == 'Female'
        assert mouse1.ear_tag == 2
        assert mouse1.genotype == 'Wildtype'
        assert mouse1.zygosity == 'Homozygous'
        assert mouse1.status == 'Alive'
        assert mouse1.surgeon == mouse1.experiment_owner
        assert mouse1.cage is None
        assert mouse1.surgeries == []
        assert mouse1.notes == []
        assert mouse1.experimental_data == []

    def test_update_zygosity(self, mouse1):
        mouse1.update_zygosity(Zygosity.HETEROZYGOUS)
        assert mouse1.zygosity == 'Heterozygous'

    def test_attach_to_cage(self, mouse1, cage):
        mouse1.attach_to_cage(cage)
        assert mouse1.cage == cage

    def test_add_note(self, mouse1, note1):
        mouse1.add_note(note1)
        assert mouse1.notes == [note1]

    def test_add_surgeries(self, mouse1, surgery1, surgery2):
        mouse1.add_surgeries(surgery1, surgery2)
        assert mouse1.surgeries == [surgery1, surgery2]

    def test_mouse_data_property(self, mouse1):
        data = mouse1.data
        assert isinstance(data, dict)
        assert data['unique id'] == mouse1.unique_id
        assert data['cage'] == mouse1.cage
        assert data['ear tag'] == mouse1.ear_tag
        assert data['sex'] == mouse1.sex
        assert data['genotype'] == mouse1.genotype
        assert data['zygosity'] == mouse1.zygosity
        assert data['date of birth'] == mouse1.date_of_birth
        assert data['status'] == mouse1.status
        assert data['experiment_owner'] == mouse1.experiment_owner
        assert data['surgeon'] == mouse1.surgeon
        assert data['age'] == mouse1.age_
        assert data['surgeries'] == [
            surgery.data for surgery in mouse1.surgeries]
        assert data['notes'] == [note.data for note in mouse1.notes]
