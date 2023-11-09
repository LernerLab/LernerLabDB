import pytest

from lernerlabdb.interface_modules.Project import Project


class TestProject:
    
    def test_init(self, project1):
        assert project1.project_title == 'project1'
        assert not project1.experiments
        
    def test_add_experiment(self, project1, experiment, experiment2):
        project1.add_experiments(experiment, experiment2)
        assert project1.experiments
        assert project1.experiments == [experiment, experiment2]
        
    def test_data_propety(self, project1, experiment, experiment2):
        project1.add_experiments(experiment, experiment2)
        data = project1.data
        assert isinstance(data, dict)
        assert data['project_title'] == project1.project_title
        assert data['experiments'] == [experiment.data, experiment2.data]
        
