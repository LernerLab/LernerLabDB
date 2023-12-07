import pytest

from lernerlabdb.interface_modules.scientist import Scientist


class TestScientist:
    def test__init(self, scientist):
        assert scientist.first_name == 'scientist'
        assert scientist.last_name == 'fixture'
        assert scientist.email == 'test'
        assert scientist.net_id == 'test'
        assert not scientist.projects

    def test_add_project(self, scientist, project1, project2):
        scientist.add_project([project1, project2])
        assert scientist.projects == [project1, project2]
        assert scientist.projects[0] == project1
        assert scientist.projects[1] == project2

    def test_data_property(self, scientist, project1):
        scientist.add_project(project1)
        data = scientist.data
        assert isinstance(data, dict)
        assert data['first_name'] == scientist.first_name
        assert data['last_name'] == scientist.last_name
        assert data['email'] == scientist.email
        assert data['net_id'] == scientist.net_id
        assert data['projects'] == [project1.data]
