
import pytest
from datetime import date

from lernerlabdb.interface_modules.Experiment import Experiment
from lernerlabdb.interface_modules.Scientist import Scientist
from lernerlabdb.interface_modules.Mouse import Mouse
from lernerlabdb.interface_modules.Note import Note

from lernerlabdb.interface_modules.enums import Sex, Genotype, Zygosity, NoteType


class TestExperiment:
    """
    A class that tests the functionality of the Experiment class.

    Methods
    -------
    scientist()
        Returns a Scientist object for testing purposes.
    mouse1(scientist)
        Returns a Mouse object with specific attributes for testing purposes.
    mouse2(scientist)
        Returns another Mouse object with specific attributes for testing purposes.
    note1()
        Returns a Note object with specific attributes for testing purposes.
    note2()
        Returns another Note object with specific attributes for testing purposes.
    experiment()
        Returns an Experiment object with a specific experiment name for testing purposes.
    test_defaults(experiment)
        Tests the default attributes of an Experiment object.
    test_add_mice(experiment, mouse1, mouse2)
        Tests the functionality of adding mice to an Experiment object.
    test_add_notes(experiment, note1, note2)
        Tests the functionality of adding notes to an Experiment object.
    """

    def test_defaults(self, experiment):
        """
        Tests the default attributes of an Experiment object.

        Parameters
        ----------
        experiment : Experiment
            An Experiment object.

        Returns
        -------
        None
        """
        assert experiment.experiment_name == 'experiment_fixture'
        assert not experiment.mice
        assert not experiment.notes

    def test_add_mice(self, experiment, mouse1, mouse2):
        """
        Tests the functionality of adding mice to an Experiment object.

        Parameters
        ----------
        experiment : Experiment
            An Experiment object.
        mouse1 : Mouse
            A Mouse object.
        mouse2 : Mouse
            Another Mouse object.

        Returns
        -------
        None
        """
        experiment.add_mice(mouse1, mouse2)
        assert experiment.mice
        assert len(experiment.mice) == 2
        assert mouse1 in experiment.mice
        assert mouse2 in experiment.mice

    def test_add_notes(self, experiment, note1, note2):
        """
        Tests the functionality of adding notes to an Experiment object.

        Parameters
        ----------
        experiment : Experiment
            An Experiment object.
        note1 : Note
            A Note object.
        note2 : Note
            Another Note object.

        Returns
        -------
        None
        """
        experiment.add_notes(note1, note2)
        assert experiment.notes
        assert len(experiment.notes) == 2
        assert note1 in experiment.notes
        assert note2 in experiment.notes

    # TODO test data property
