from abc import ABC, abstractclassmethod
from typing import Union


class LoopInterface(ABC):
    device = None

    @abstractclassmethod
    def run_single_epoch(cls) -> Union[None, float]:
        """[summary]
        """

    @abstractclassmethod
    def run_epochs(cls) -> None:
        """[summary]
        """

    @abstractclassmethod
    def execute(cls, config=None) -> None:
        """[summary]
        """
