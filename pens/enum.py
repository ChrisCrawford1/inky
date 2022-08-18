from enum import Enum


class NibSize(Enum):
    EF = "Extra Fine"
    F = "Fine"
    M = "Medium"
    B = "Broad"
    DB = "Double Broad"
    STB = "Stub"

    @classmethod
    def to_tuple(cls):
        return tuple((size.name, size.value) for size in cls)


class NibMaterial(Enum):
    STEEL = "Steel"
    GOLD12 = "Gold (12k)"
    GOLD14 = "Gold (14k)"
    GOLD18 = "Gold (18k)"
    GOLD21 = "Gold (21k)"
    PLATINUM = "Platinum"
    PALLADIUM = "Palladium"

    @classmethod
    def to_tuple(cls):
        return tuple((mat.name, mat.value) for mat in cls)
