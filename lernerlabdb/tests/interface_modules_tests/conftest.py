
import pytest
from datetime import datetime, date, time, timedelta

from lernerlabdb.interface_modules.Cage import Cage
from lernerlabdb.interface_modules.Coordinates import Coordinates
from lernerlabdb.interface_modules.Drug import Drug
from lernerlabdb.interface_modules.Experiment import Experiment
from lernerlabdb.interface_modules.Implant import Implant
from lernerlabdb.interface_modules.Mouse import Mouse
from lernerlabdb.interface_modules.Note import Note
from lernerlabdb.interface_modules.Scientist import Scientist
from lernerlabdb.interface_modules.Surgery import Surgery
from lernerlabdb.interface_modules.Injection import Injection

from lernerlabdb.interface_modules.enums import ImplantType, DrugType, CageStatus, Location, Sex, Genotype, Zygosity, NoteType, InjectionType


@pytest.fixture
def implant():
    return Implant(implant_type=ImplantType.OPTO)


@pytest.fixture
def coordinates():
    return Coordinates(ap=1, ml=2, dv=3)


@pytest.fixture
def default_coordinates():
    return Coordinates()


@pytest.fixture
def cage():
    return Cage(barcode=1,
                cage_nickname='cage_fixture',
                num_animals=3,
                genotype=Genotype.WT,
                sex=Sex.FEMALE,
                date_of_birth=date(2021, 1, 1),
                location=Location.W15W_019,
                status=CageStatus.ACTIVE)


@pytest.fixture
def drug():
    return Drug(DrugType.BUPESR, 0.3, 0.2)


@pytest.fixture
def scientist():
    """
    Returns a Scientist object for testing purposes.

    Returns
    -------
    Scientist
        A Scientist object with specific attributes.
    """
    scientist = Scientist(
        first_name='scientist',
        last_name='fixture',
        email='test',
        net_id='test'
    )
    return scientist


@pytest.fixture
def mouse1(scientist):
    """
    Returns a Mouse object with specific attributes for testing purposes.

    Parameters
    ----------
    scientist : Scientist
        A Scientist object.

    Returns
    -------
    Mouse
        A Mouse object with specific attributes.
    """
    mouse = Mouse(
        date_of_birth=date(2020, 1, 1),
        sex=Sex.FEMALE,
        ear_tag=2,
        genotype=Genotype.WT,
        zygosity=Zygosity.HOMOZYGOUS,
        experiment_owner=scientist
    )
    return mouse


@pytest.fixture
def mouse2(scientist):
    """
    Returns another Mouse object with specific attributes for testing purposes.

    Parameters
    ----------
    scientist : Scientist
        A Scientist object.

    Returns
    -------
    Mouse
        Another Mouse object with specific attributes.
    """
    mouse = Mouse(
        date_of_birth=date(2020, 1, 1),
        sex=Sex.MALE,
        ear_tag=1,
        genotype=Genotype.WT,
        zygosity=Zygosity.HOMOZYGOUS,
        experiment_owner=scientist
    )
    return mouse


@pytest.fixture
def note1():
    """
    Returns a Note object with specific attributes for testing purposes.

    Returns
    -------
    Note
        A Note object with specific attributes.
    """
    return Note(
        type=NoteType.SURGERY,
        note='test1'
    )


@pytest.fixture
def note2():
    """
    Returns another Note object with specific attributes for testing purposes.

    Returns
    -------
    Note
        Another Note object with specific attributes.
    """
    return Note(
        type=NoteType.RECOVERY,
        note='test2'
    )


@pytest.fixture
def experiment():
    """
    Returns an Experiment object with a specific experiment name for testing purposes.

    Returns
    -------
    Experiment
        An Experiment object with a specific experiment name.
    """
    return Experiment(
        experiment_name='experiment_fixture'
    )


@pytest.fixture
def injection():
    return Injection(substrate="aav5-eGFP",
                     type=InjectionType.VIRUS, volume=200, flowrate=100, titer=1.5)
