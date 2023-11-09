from typing import List, NewType




class Project:
    project_tile: str

    def __init__(self, project_title):
        self.project_title = project_title
        self._experiments = []

    @property
    def experiments(self):
        return self._experiments

    def add_experiments(self, *experiments: List):
        for exp in experiments:
            if isinstance(exp, list):
                self._experiments.extend(exp)
            else:
                self._experiments.append(exp)

    @property
    def data(self):
        data = {
            'project_title': self.project_title,
            'experiments': [exp.data for exp in self.experiments]
        }
        return data