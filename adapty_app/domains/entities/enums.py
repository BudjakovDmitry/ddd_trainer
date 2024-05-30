from enum import Enum

class Gender(Enum):
    MALE = 'm'
    FEMALE = 'f'
    OTHER = 'o'

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]


class Platform(Enum):
    iOS = 'iOS'
    macOS = 'macOS'
    iPadOS = 'iPadOS'
    visionOS = 'visionOS'
    Android = 'Android'

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]
