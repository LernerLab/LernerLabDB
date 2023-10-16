

class Implant:
    def __init__(self, type: str, angle: int):
        self.type = type
        self.angle = angle

    def __repr__(self):
        return f"Implant(type = {self.type}, angle = {self.angle})"


implant = Implant(type="Cannula", angle=10)
print(implant)
