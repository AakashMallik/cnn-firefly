from .utils.constant import PipelineType
from .utils.config_parser import ConfigParser

# TODO wrap seed and device here itself


class Pipeline:
    @classmethod
    def train(cls, config):
        pass

    @classmethod
    def execute(cls, config_path, options):
        print(config_path)
        config = ConfigParser.parse(config_path, options)

        print(config)

        if config.pipeline_type == PipelineType.TRAIN:
            cls.train(config)
        elif config.pipeline_type == PipelineType.TEST:
            pass
