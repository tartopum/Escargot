from ..abstracts import BasicRamp as BasicRamp
from pyduino import pcduino as pd

__all__ = ('Ramp')


class Ramp(BasicRamp):
    """A basic ramp running on a pcDuino."""

    def __init__(self, *args, **kwargs):
        BasicRamp.__init__(self, *args, **kwargs)

    def __len__(self):
        pass

    def delay(self, d):
        pass

    def pulse(self, output):
        pass
