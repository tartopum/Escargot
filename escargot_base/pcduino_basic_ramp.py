from pyduino import pcduino as pd
from abstract_ramp import AbstractRamp

__all__ = ('PCDuinoBasicRamp')


class PCDuinoBasicRamp(AbstractRamp):
    """A basic ramp with an angle sensor and two solenoid valves. It runs on 
    a pcduino.
    """
    
    def __init__(self, ):
        AbstractRamp.__init__(self, )
        """
        angle_sensor: int
        lengthen: (output, delay)
        shorten: (output, delay)
        len_accu
        """

    def get_len(self):
        """Return the length of the ramp."""
        pass

    def move(self, output, delay):
        """Move the ramp. TODO: 1 incr"""

        pd.digitalWrite(output, pd.HIGH)
        pd.digitalWrite(output, pd.LOW)
        pd.delay(delay)
