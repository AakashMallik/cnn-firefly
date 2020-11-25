import abc


class FactoryInterface(abc.ABC):
    @abc.abstractclassmethod
    def generate(cls, name=None, options={}):
        """generate the required pytorch object

        Args:
            name (string, optional): name of the required object. Defaults to None.
            options (dict, optional): additional params needed for initialization. Defaults to {}.
        """
