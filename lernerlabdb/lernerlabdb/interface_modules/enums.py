
from enum import Enum, StrEnum, auto


class UpperStrEnum(StrEnum):
    """ wrapper for str enums that modifies auto to convert to uppercase """
    def _generate_next_value_(name, start, count, last_values):
        return name.upper()


class CaptitalStrEnum(StrEnum):
    """ wrapper for str enums that modifies auto to convert to uppercase """
    def _generate_next_value_(name, start, count, last_values):
        return name.capitalize()


class CageStatus(Enum):
    ACTIVE = auto()
    DEACTIVATED = auto()


class MouseStatus(CaptitalStrEnum):
    ALIVE = auto()
    DEAD = auto()


class Location(Enum):
    W15W_019 = 'W15W_019'
    W15W_011 = 'W15W_011'
    LSB_403 = 'LSB_403'
    SQB_835 = 'SQB_835'


class Sex(CaptitalStrEnum):
    MALE = auto()
    FEMALE = auto()


class Zygosity(CaptitalStrEnum):
    WILDTYPE = auto()
    HOMOZYGOUS = auto()
    HETEROZYGOUS = auto()
    UNKNOWN = auto()


class DrugType(UpperStrEnum):
    BUPESR = auto()
    BUPIVICIANE = auto()
    MELOXICAM = auto()


class ImplantType(CaptitalStrEnum):
    CANNULA = auto()
    OPTO = auto()
    ELECTRODE = auto()
    LENS = auto()
    FIBER_OPTIC = auto()
    PELLET = auto()
    MICRO = auto()


class Hemisphere(CaptitalStrEnum):
    LEFT = auto()
    RIGHT = auto()
    BILATERAL = auto()


class InjectionType(CaptitalStrEnum):
    VIRUS = auto()
    TRACER = auto()
    DYE = auto()
    CYTOTOXIC = auto()
    DRUG = auto()
    OTHER = auto()


class NoteType(CaptitalStrEnum):
    SURGERY = auto()
    RECOVERY = auto()
    EXPERIMENTAL = auto()
    POSTMORTEM = auto()
    OTHER = auto()


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


class BrainStructure(UpperStrEnum):
    VTA = auto()
    LHA = auto()
    DLS = auto()
    DMS = auto()
    OFC = auto()
