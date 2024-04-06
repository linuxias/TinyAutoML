import json
import jsonschema
from dataclasses import dataclass
from enum import Enum

class TunerType(str, Enum):
    ALL = "ALL"
    RandomSearch = "RandomSearch"
    BO = "BayesianOptimization"
    HB = "HyperBand"

@dataclass
class TunerConfiguration:
    tuner: TunerType

    def __init__(self,
                 tuner: TunerType):
        self.tuner = tuner

if __name__ == "__main__":
    pass