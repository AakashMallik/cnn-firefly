from torch.nn import (CrossEntropyLoss, NLLLoss, MSELoss,
                      BCEWithLogitsLoss, BCELoss)
from ..interfaces import FactoryInterface


class LossFactory(FactoryInterface):
    lookup_table = {
        "CrossEntropyLoss": CrossEntropyLoss,
        "NLLLoss": NLLLoss,
        "BCELoss": BCELoss
    }

    @classmethod
    def generate(cls, config, options):
        name = config.loss.name
        params = config.loss.params

        if name in cls.lookup_table.keys():
            return cls.lookup_table[name](**params)
        else:
            raise Exception(f"[{name} not found in loss lookup table]")
