from ..abstracts import BasicRamp as BasicRamp
from pyduino import pcduino as pd

__all__ = ('Ramp')


class Ramp(BasicRamp):
    """A basic ramp running on a pcDuino."""

    def delay(self, d):
        pd.delay(d)

    def pulse(self, output):
        pd.digitalWrite(output, pd.HIGH)
        pd.digitalWrite(output, pd.LOW)
