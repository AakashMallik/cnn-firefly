import abc


class LoopInterface(abc.ABC):
    device = None

    @abc.abstractclassmethod
    def run_single_epoch(cls) -> None:
        """[summary]
        """

    @abc.abstractclassmethod
    def run_epochs(cls) -> None:
        """[summary]
        """

    @abc.abstractclassmethod
    def execute(cls, config=None) -> None:
        """[summary]
        """
