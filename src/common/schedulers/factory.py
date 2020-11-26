from torch.optim.lr_scheduler import (
    StepLR, CosineAnnealingLR, ReduceLROnPlateau)
from ..interfaces import FactoryInterface


class SchedulerFactory(FactoryInterface):
    lookup_table = {
        "StepLR": StepLR,
        "CosineAnnealingLR": CosineAnnealingLR,
        "ReduceLROnPlateau": ReduceLROnPlateau
    }

    @classmethod
    def generate(cls, config, options):
        name = config.scheduler.name
        params = config.scheduler.params
        optimizer = options["optimizer"]

        if name in cls.lookup_table.keys():
            return cls.lookup_table[name](optimizer, **params)
        else:
            raise Exception(f"[{name} not found in scheduler lookup table]")
