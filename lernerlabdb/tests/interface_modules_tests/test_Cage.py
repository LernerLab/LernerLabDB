import pytest
from datetime import datetime, date, time, timedelta
from lernerlabdb.interface_modules.enums import CageStatus, Location, Sex, Genotype

from lernerlabdb.interface_modules.cage import Cage


class TestCage:

    def test_init(self, cage):
        assert cage.barcode == 1
        assert cage.cage_nickname == 'cage_fixture'
        assert cage.genotype == 'Wildtype'
        assert cage.sex == 'Female'
        assert cage._date_of_birth == date(2021, 1, 1)
        assert cage.location == 'W15W_019'
        assert cage.status == 'Active'

    def test_data_property(self, cage):
        data = cage.data
        print(data)
        assert isinstance(data, dict)
        assert data["barcode"] == 1
        assert data['cage_nickname'] == cage.cage_nickname
        assert data['parent_cage'] is None
        assert data['num_animals'] == cage.num_animals
        assert data['sex'] == cage.sex
        assert data['genotype'] == cage.genotype
        assert data['location'] == cage.location
        assert data['status'] == cage.status

    def test_change_status(self, cage):
        assert cage.status == 'Active'
        cage.change_status()
        assert cage.status == 'Deactivated'
        cage.change_status()
        assert cage.status == 'Active'
