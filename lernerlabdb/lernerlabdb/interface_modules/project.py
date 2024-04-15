from typing import List, Dict, Any


class Project:
    """A class representing a project.

    Attributes:
        project_title (str): The title of the project.
        _experiments (List): A list of experiments associated with the project.

    Methods:
        add_experiments: Add one or more experiments to the project.
        data: Get a dictionary representation of the project data.

    Examples:
        >>> project = Project("My Project")
        >>> experiment1 = Experiment("Experiment 1")
        >>> experiment2 = Experiment("Experiment 2")
        >>> project.add_experiments(experiment1, experiment2)
        >>> project.data
        {
            'project_title': 'My Project',
            'experiments': [
                {'experiment_title': 'Experiment 1'},
                {'experiment_title': 'Experiment 2'}
            ]
        }
    """
    def __init__(self, project_title):
        self.project_title:str = project_title
        self._experiments:List = []

    @property
    def experiments(self)->List:
        """
        Returns a list of Experiment objects associated with the project.
        """
        return self._experiments

    def add_experiments(self, *experiments: List)-> None:
        """Add one or more experiments to the project."""
        for exp in experiments:
            if isinstance(exp, list):
                self._experiments.extend(exp)
            else:
                self._experiments.append(exp)

    @property
    def data(self)->Dict[str, Any]:
        """
        Returns a dictionary representation of the project data.
        """
        data = {
            'project_title': self.project_title,
            'experiments': [exp.data for exp in self.experiments]
        }
        return data
