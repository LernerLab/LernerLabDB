from dataclasses import dataclass
from lernerlabdb.interface_modules.Project import Project
from typing import List

#! UNIT TESTS STILL NEED TO BE DONE


class Scientist:
    def __init__(self, first_name: str, last_name: str, email: str, net_id: str):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.net_id = net_id
        self.projects: List[Project] = []

    def add_project(self, project: Project):
        self.projects.append(project)



