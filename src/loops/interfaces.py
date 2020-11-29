from abc import ABC, abstractmethod
from typing import Union


class LoopInterface(ABC):
    device = None

    @abstractmethod
    def run_single_epoch(self) -> Union[None, float]:
        """[summary]
        """

    @abstractmethod
    def run_epochs(self) -> None:
        """[summary]
        """

    # @abstractmethod
    # def execute(self, config=None) -> None:
    #     """[summary]
    #     """
