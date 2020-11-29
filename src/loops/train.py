from .interfaces import LoopInterface

class TrainingLoop(LoopInterface):
    def __init__(self, config):
        pass

    def run_single_epoch(self):
        pass

    def run_epochs(self):
        pass

    def __call__(self, device):
        print(device)