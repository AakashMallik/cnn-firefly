from .utils.constant import PipelineType
from .utils.config_parser import ConfigParser
from .utils.seed import seed_all
from .utils.device import get_device
from .loops.train import TrainingLoop


class Pipeline:
    @classmethod
    @seed_all
    @get_device
    def train(config, device):
        loop_instance = TrainingLoop(config)
        loop_instance(device)

    @classmethod
    def execute(cls, config_path, options):
        config = ConfigParser.parse(config_path, options)

        print(config)

        if config.pipeline_type == PipelineType.TRAIN:
            cls.train(config)
        elif config.pipeline_type == PipelineType.TEST:
            pass
