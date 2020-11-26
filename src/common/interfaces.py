from abc import ABC, abstractclassmethod


class FactoryInterface(ABC):
    lookup_table = {}

    @abstractclassmethod
    def generate(cls, config={}, options={}):
        """generate the required pytorch object

        Args:
            config (dict, optional): config object. Defaults to {}.
            options (dict, optional): additional params needed for initialization. Defaults to {}.
        """
