from .utils.constant import PipelineType
from .utils.config_parser import ConfigParser
from .utils.seed import seed_all
from .utils.device import get_device
from .loops.train import TrainingLoop


class Pipeline:
    @classmethod
    def train(cls, config, device=None):
        seed_all(config.seed)
        loop_instance = TrainingLoop(config, device=get_device())
        loop_instance()

    @classmethod
    def execute(cls, config_path, options):
        config = ConfigParser.parse(config_path, options)
        
        if config.pipeline_type == PipelineType.TRAIN:
            cls.train(config)
        elif config.pipeline_type == PipelineType.TEST:
            pass
