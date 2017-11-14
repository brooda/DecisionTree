from enum import Enum

class Fuzziness(Enum):
    LEAF = 1
    NO = 2
    LINEAR = 3
    SIGMOIDAL = 4