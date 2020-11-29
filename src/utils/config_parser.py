from easydict import EasyDict as edict
from yaml import safe_load
from functools import reduce
from .path import DEFAULT_CONFIG_ROOT
from .constant import PipelineType, PredictionType, TuningType


class ConfigParser:
    @classmethod
    def change_case(cls, str):
        return reduce(lambda x, y: x + ('_' if y.isupper() else '') + y, str).upper()

    @classmethod
    def read_yaml(cls, config_path):
        with open(config_path, 'r') as fid:
            config = edict(safe_load(fid))
        return config

    @classmethod
    def get_pipeline_type(cls, config_path):
        try:
            strType = config_path.name.split('.')[1]
            key = cls.change_case(strType)
            return PipelineType[key]
        except:
            raise Exception(f"pipeline type [{key}] not defined")

    @classmethod
    def get_config_name(cls, config_path):
        config_name = config_path.name.split('.')[0]

        return config_name

    @classmethod
    def get_default_config(cls, pipeline_type):
        if pipeline_type == PipelineType.TRAIN:
            return cls.read_yaml(DEFAULT_CONFIG_ROOT / 'train.yaml')
        else:
            raise Exception(
                f"No default config available for pipeline_type [{pipeline_type}]")

    @classmethod
    def merge(cls, default_config, user_config):
        if not isinstance(user_config, edict):
            return

        for key, value in user_config.items():
            if isinstance(value, edict):
                cls.merge(default_config[key], user_config[key])
            else:
                try:
                    default_config[key] = value
                except:
                    default_config = edict()
                    default_config[key] = value

        return default_config

    @classmethod
    def generate(cls, pipeline_type):
        pass

    @classmethod
    def parse(cls, config_path, options={}):
        config_name = cls.get_config_name(config_path)
        pipeline_type = cls.get_pipeline_type(config_path)
        default_config = cls.get_default_config(pipeline_type)
        user_config = cls.read_yaml(config_path)

        return ConfigSanity.check(
            cls.merge(default_config, user_config),
            options={
                "pipeline_type": pipeline_type,
                "config_path": config_path,
                "config_name": config_name
            }
        )


class ConfigSanity:
    @classmethod
    def check(cls, config, options):
        config.pipeline_type = options["pipeline_type"]
        config.config_path = options["config_path"]
        config.config_name = options["config_name"]

        check_list = [
            cls.train_data,
            cls.validation_data,
            cls.model,
            cls.optimizer,
            cls.loss
        ]
        cls.check_chain(config, check_list)

        return config

    @classmethod
    def check_chain(cls, config, check_list):
        for fn in check_list:
            fn(config)

    @classmethod
    def train_data(cls, config):
        config = config.train_data
        if config.name is None:
            raise Exception('train_data.name cannot be None')

    @classmethod
    def validation_data(cls, config):
        config = config.validation_data
        if config.name is None:
            raise Exception('validation_data.name cannot be None')

    @classmethod
    def model(cls, config):
        config = config.model
        if config.name is None:
            raise Exception('model.name cannot be None')

        try:
            strType = config.prediction_type
            key = ConfigParser.change_case(strType)
            config.prediction_type = PredictionType[key]
        except:
            raise Exception(f"[{key}] is not a valid prediction type")

        try:
            strType = config.tune_type
            key = ConfigParser.change_case(strType)
            config.tune_type = TuningType[key]
        except:
            raise Exception(f"[{key}] is not a valid tuning type")

    @classmethod
    def optimizer(cls, config):
        config = config.optimizer
        if config.name is None:
            raise Exception('optimizer.name cannot be None')

    @classmethod
    def loss(cls, config):
        config = config.loss
        if config.name is None:
            raise Exception('loss.name cannot be None')
