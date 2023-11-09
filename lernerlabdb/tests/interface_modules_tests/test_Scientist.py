import pytest

from lernerlabdb.interface_modules.Scientist import Scientist


class TestScientist:
    def test__init(self, scientist):
        assert scientist.first_name == 'scientist'
        assert scientist.last_name == 'fixture'
        assert scientist.email == 'test'
        assert scientist.net_id == 'test'
        assert not scientist.projects
        
    def test_add_project(self, scientist, project1, project2):
        scientist.add_project(project1, project2)
        assert scientist.projects 
        assert scientist.projects[0] == project1
        assert scientist.projects[1] == project2

