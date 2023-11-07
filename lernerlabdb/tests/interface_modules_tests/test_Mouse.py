from datetime import datetime
import pytest
from unittest.mock import Mock, patch
import uuid

from lernerlabdb.interface_modules.Mouse import Mouse
from lernerlabdb.interface_modules.Cage import Cage
from lernerlabdb.interface_modules.Surgery import Surgery
from lernerlabdb.interface_modules.Note import Note
from lernerlabdb.interface_modules.Experiment import Experiment
from lernerlabdb.interface_modules.Scientist import Scientist
from lernerlabdb.interface_modules.enums import Sex, Zygosity, MouseStatus, Genotype, Location, CageStatus, NoteType


@pytest.fixture
def cage():
    return Cage(
        barcode=1,
        cage_nickname='cage_fixture',
        num_animals=3,
        genotype=Genotype.WT,
        sex=Sex.FEMALE,
        date_of_birth=datetime(2020, 1, 1),
        location=Location.W15W_019,
        status=CageStatus.ACTIVE
    )


@pytest.fixture
def experiment():
    return Experiment(
    )


@pytest.fixture
def note():
    return Note(
        type=NoteType.SURGERY,
        note='test'
    )


@pytest.fixture
def scientist1():
    return Scientist(
        first_name='test',
        last_name='test',
        email='test',
        net_id='test'
    )


@pytest.fixture
def scientist2():
    return Scientist(
        first_name='new',
        last_name='scientist',
        email='other test',
        net_id='test'
    )


@pytest.fixture
def surgery1():
    return Surgery(surgery_number=1)


@pytest.fixture
def surgery2():
    return Surgery(surgery_number=2)


class TestMouse:

    @pytest.fixture
    def default_mouse(self, scientist1):
        mouse = Mouse(
            date_of_birth=datetime(2020, 1, 1),
            sex=Sex.FEMALE,
            ear_tag=1,
            genotype=Genotype.WT,
            zygosity=Zygosity.HOMOZYGOUS,
            experiment_owner=scientist1
        )
        return mouse

    def test_init(self, default_mouse):
        assert default_mouse.age_ == {
            "days": (datetime.now() - default_mouse.date_of_birth).days,
            'weeks': ((datetime.now() - default_mouse.date_of_birth).days)//7,
            'days since first surgery': 0,
            'weeks since first surgery': 0}
        assert isinstance(default_mouse._unique_id, uuid.UUID)
        assert isinstance(default_mouse.unique_id, str)
        assert default_mouse.sex == 'Female'
        assert default_mouse.ear_tag == 1
        assert default_mouse.genotype == 'Wildtype'
        assert default_mouse.zygosity == 'Homozygous'
        assert default_mouse.status == 'Alive'
        assert default_mouse.surgeon == default_mouse.experiment_owner
        assert default_mouse.cage is None
        assert default_mouse.surgeries == []
        assert default_mouse.notes == []
        assert default_mouse.experiments == []

    def test_update_zygosity(self, default_mouse):
        default_mouse.update_zygosity(Zygosity.HETEROZYGOUS)
        assert default_mouse.zygosity == 'Heterozygous'

    def test_attach_to_cage(self, default_mouse, cage):
        default_mouse.attach_to_cage(cage)
        assert default_mouse.cage == cage

    def test_add_note(self, default_mouse, note):
        default_mouse.add_note(note)
        assert default_mouse.notes == [note]

    def test_add_surgeries(self, default_mouse, surgery1, surgery2):
        default_mouse.add_surgeries(surgery1, surgery2)
        assert default_mouse.surgeries == [surgery1, surgery2]

    def test_add_experiment(self, default_mouse, experiment):
        default_mouse.add_experiment(experiment)
        assert default_mouse.experiments == [experiment]

    def test_mouse_data_property(self, default_mouse):
        data = default_mouse.data
        assert isinstance(data, dict)
        assert data['unique id'] == default_mouse.unique_id
        assert data['cage'] == default_mouse.cage
        assert data['ear tag'] == default_mouse.ear_tag
        assert data['sex'] == default_mouse.sex
        assert data['genotype'] == default_mouse.genotype
        assert data['zygosity'] == default_mouse.zygosity
        assert data['date of birth'] == default_mouse.date_of_birth
        assert data['status'] == default_mouse.status
        assert data['experiment_owner'] == default_mouse.experiment_owner
        assert data['surgeon'] == default_mouse.surgeon
        assert data['age'] == default_mouse.age_
        assert data['surgeries'] == [
            surgery.data for surgery in default_mouse.surgeries]
        assert data['notes'] == [note.data for note in default_mouse.notes]
        assert data['experiments'] == [
            experiment.experiment_data for experiment in default_mouse.experiments]
