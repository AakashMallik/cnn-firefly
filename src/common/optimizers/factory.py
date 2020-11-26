from torch.optim import (RMSprop, Adam, AdamW)
from ..interfaces import FactoryInterface


class OptimizerFactory(FactoryInterface):
    lookup_table = {
        "RMSprop": RMSprop,
        "Adam": Adam,
        "AdamW": AdamW
    }

    @classmethod
    def generate(cls, config, options):
        name = config.optimizer.name
        params = config.optimizer.params
        model_params = options["model_params"]

        if name in cls.lookup_table.keys():
            return cls.lookup_table[name](model_params, **params)
        else:
            raise Exception(f"[{name} not found in optimizer lookup table]")
