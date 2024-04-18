
from enum import Enum, auto

# class Enum(StrEnum):
#     """ wrapper for str enums that modifies auto to convert to uppercase """
#     def _generate_next_value_(name, start, count, last_values):
#         return name.upper()


# class Enum(StrEnum):
#     """ wrapper for str enums that modifies auto to convert to uppercase """
#     def _generate_next_value_(name, start, count, last_values):
#         return name.capitalize()


class CageStatus(Enum):
    ACTIVE = 'Active'
    DEACTIVATED = 'Deactivated'


class MouseStatus(Enum):
    ALIVE = "Alive"
    DEAD = "Dead"


class Location(Enum):
    W15W_019 = 'W15W_019'
    W15W_011 = 'W15W_011'
    LSB_403 = 'LSB_403'
    SQB_835 = 'SQB_835'


class Sex(Enum):
    MALE = 'Male'
    FEMALE = "Female"


class Zygosity(Enum):
    WILDTYPE = "Wildtype"
    HOMOZYGOUS = "Homozygous"
    HETEROZYGOUS = "Heterozygous"
    UNKNOWN = "Unknown"


class DrugType(Enum):
    BUPESR = "BupeSR"
    BUPIVICAINE = "Bupivacaine"
    MELOXICAM = "Meloxicam"


class ImplantType(Enum):
    NONE = "None"
    CANNULA = "Cannula"
    ELECTRODE = "Electrode"
    FIBER_OPTIC = "Fiber Optic"
    LENS = "Lens"
    MICRO = "Micro"
    OPTO = "Opto"
    PELLET = "Pellet"


class Hemisphere(Enum):
    LEFT = "Left"
    RIGHT = "Right"
    BILATERAL = "Bilateral"


class InjectionType(Enum):
    NONE = "None"
    CYTOTOXIC = "Cytotoxic"
    DRUG = "Drug"
    DYE = "Dye"
    TRACER = "Tracer"
    VIRUS = "Virus"
    OTHER = "Other"


class NoteType(Enum):
    SURGERY = "Surgery"
    RECOVERY = "Recovery"
    EXPERIMENTAL = "Experimental"
    POSTMORTEM = "Postmortem"
    OTHER = "Other"


class Genotype(Enum):
    WT = 'Wildtype'
    DATCRE = 'DAT_cre'
    THFLPO = 'TH_Flpo'
    VGATCRE = 'VGAT_cre'
    THFLOP_X_VGAT = 'TH_flpo_X VGat'
    DRDA1A_TDTOMATO = 'Drd1a_tdTomato'
    DATCRE_X_VGAT = 'DAT_cre_X_VGat'
    SOX6_FSF_CRE_X_TH_FLPO = 'Sox6_FSF_cre_X_TH-flpo'
    SOX6_FSF_CRE_X_DAT_FLPO = 'Sox6_FSF_cre_X_DAT-flpo'
    DATCRE_X_LSL_CAS9 = 'DAT_cre_X_LSL-Cas9'
    LSL_CAS9 = 'LSL-Cas9'
    VGAT_CRE_X_LSL_CAS9 = 'VGAT_cre_X_LSL_Cas9'
    ELS = 'Early Life Stress'
    ELE = 'Early Life Enrichement'
    ELSDAT = 'Early Life Stress-DAT'
    ELEDAT = 'Early Life Enrichment-DAT'


class BrainStructure(Enum):
    VTA = "VTA"
    LHA = "LHA"
    DLS = "DLS"
    DMS = "DMS"
    OFC = "OFC"
