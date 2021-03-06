from ..interfaces import FactoryInterface
from cifar10 import Cifar10

class DatasetFactory(FactoryInterface):
    @classmethod
    def generate(cls, name=None, options={}):
        return Cifar10()
