from lernerlabdb.interface_modules.Structure import Structure


class Procedure:
    def __init__(self, name, id):
        self._name = name
        self._id = id  # ! I think we need a way to auto-generate this and cross reference the db, but placeholder for now
        self._structures = []

    @property
    def name(self):
        return self._name

    @property
    def id(self):
        return self._id

    @property
    def structures(self):
        return self._structures

    def add_structure(self, structure: Structure):
        self._structures.append(structure)

    @property
    def procedure_data(self):
        data = {
            "name": self.name,
            "id": self.id,
            "structures": {f"structure_{i+1}": struct.structure_data for i, struct in enumerate(self.structures)}
        }
        return data
