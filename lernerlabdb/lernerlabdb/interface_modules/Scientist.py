
from lernerlabdb.interface_modules.Project import Project
from typing import List, Dict, Any


class Scientist:

    def __init__(self,
                 first_name: str,
                 last_name: str,
                 email: str,
                 net_id: str
                 ):
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.email: str = email
        self.net_id: str = net_id
        self._projects = []

    @property
    def projects(self) -> List[Project]:
        """"
        Returns a list of Project objects associated with the scientist.
        """
        return self._projects

    def add_project(self, *projects) -> None:
        """
        Returns a list of Project objects associated with the scientist.
        """
        for project in projects:
            if isinstance(project, list):
                self._projects.extend(project)
            else:
                self._projects.append(project)

    @property
    def data(self) -> Dict[str, Any]:
        """
        Returns a dictionary representation of the scientist data.
        """
        data = {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'net_id': self.net_id,
            'projects': [p.data for p in self.projects]
        }
        return data
