from pyduino import pcduino as pd
from ..basics import BasicRamp as BasicRamp_

__all__ = ('BasicRamp')


class BasicRamp(BasicRamp_):
    """A basic ramp running on pcduino."""

    HIGH = pd.HIGH
    LOW = pd.LOW
    delay = pd.delay
    digital_write = pd.digitalWrite
    
    def __init__(self, *args, **kwargs):
        BasicRamp_.__init__(self, *args, **kwargs)
