import torch


def get_device(fn):
    def wrapper(*args, **kwargs):
        if torch.cuda.is_available():
            device = torch.device("cuda:0")
            print("[ GPU: {} (1/{}) ]".format(
                torch.cuda.get_device_name(0),
                torch.cuda.device_count())
            )
        else:
            device = torch.device("cpu")
            print("[ Running on the CPU ]")

        args = args + (device,)

        return fn(*args, **kwargs)

    return wrapper
