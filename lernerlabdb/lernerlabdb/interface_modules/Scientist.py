
from lernerlabdb.interface_modules.Project import Project
from typing import List


class Scientist:
    first_name: str
    last_name: str
    email: str
    net_id: str
    projects: List[Project]

    def __init__(self, first_name, last_name, email, net_id):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.net_id = net_id
        self.projects = []

    def add_project(self, *projects):
        for project in projects:
            if isinstance(project, list):
                self.projects.extend(project)
            else:
                self.projects.append(project)

    @property
    def data(self):
        data = {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'net_id': self.net_id,
            'projects': [p.data for p in self.projects]
        }
        return data
