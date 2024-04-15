from lernerlabdb.interface_modules.structure import Structure
from typing import List, Dict, Any
from uuid import uuid4

class Procedure:
    """
    A class representing an isolated prodcedure during a surgery. Includes structures, injections, implants and associated coordintes.

    Parameters
    ----------
    name : str
        The name of the procedure.
    id : int
        The ID of the procedure.

    Attributes
    ----------
    name : str
        The name of the procedure.
    id : int
        The ID of the procedure.
    structures : list
        A list of structures associated with the procedure.

    Methods
    -------
    add_structure(structure: Structure)
        Adds a structure to the list of structures associated with the procedure.
    procedure_data()
        Returns a dictionary containing the procedure's name, ID, and associated structures.
    """
    name: str
    id: int

    def __init__(self,
                 name: str):

        self._name = name
        self._id = uuid4()
        self._structures: List = []

    @property
    def name(self) -> str:
        '''The name of the procedure'''
        return self._name

    @property
    def id(self) -> int:
        '''returns then inti ID of the procedure'''
        return self._id.int

    @property
    def structures(self):
        '''A list of structures associated with the procedure'''
        return self._structures

    def add_structure(self, structure: Structure) -> None:
        '''Adds a Structure object to the list of structures associated with the procedure'''
        self._structures.append(structure)

    @property
    def data(self) -> Dict[str, Any]:
        '''Returns a dictionary containing all associated data for the procedure'''
        data = {
            "name": self.name,
            "id": self.id,
            "structures": {f"structure_{i+1}": struct.data for i, struct in enumerate(self.structures)}
        }
        return data
