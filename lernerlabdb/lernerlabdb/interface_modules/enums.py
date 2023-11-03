
from enum import Enum


class CagStatus(Enum):
    ACTIVE = 'Active'
    DEACTIVATED = 'Deactivated'
    
class MouseStatus(Enum):
    ALIVE = 'Alive'
    DEAD = 'Dead'
    
class Location(Enum):
    W15W_019 = 'W15W_019'
    W15W_011 = 'W15W_011'
    LSB_403 = 'LSB_403'
    SQB_835 = 'SQB_835'
    
class Sex(Enum):
    MALE = 'male'
    FEMALE = 'female'
    
class Zygosity(Enum):
    WILDTYPE = 'Wildtype'
    HOMOZYGOUS = 'Homozygous'
    HETEROZYGOUS = 'Heterozygous'
    UNKNOWN = 'Unknown'
    
class DrugType(Enum):
    BUPESR = 'BupeSR'
    BUPIVICIANE = 'Bupivicaine'
    MELOXICAM = 'Meloxicam'
    
class ImplantType(Enum):
    CANNULA = 'Cannula'
    OPTO = 'Opto'
    ELECTRODE = 'Electrode'
    LENS = 'Lens'
    FIBER_OPTIC = 'Fiber Optic'
    PELLET = 'Pellet'
    
class Hemisphere(Enum):
    LEFT = 'Left'
    RIGHT = 'Right'
    BILATERAL = 'Bilateral'
    
class InjectionType(Enum):
    VIRUS = 'Virus'
    TRACER = 'Tracer'
    DYE = 'Dye'
    CYTOTOXIC = 'Cytotoxic'
    DRUG = 'Drug'
    OTHER = 'Other'
    
class NoteType(Enum):
    SURGERY = 'Surgery'
    RECOVERY = 'Recovery'
    EXPERIMENTAL = 'Experimental'
    OTHER = 'Other'