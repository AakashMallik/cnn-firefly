from enum import Enum

class PipelineType(Enum):
        TRAIN = 1
        TEST = 2
    
class PredictionType(Enum):
        CLASSIFICATION = 1
        REGRESSION = 2

class TuningType(Enum):
        FINE_TUNING = 1
        FEATURE_EXTRACTION = 2