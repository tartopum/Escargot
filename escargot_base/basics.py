from pyduino import pcduino as pd
from abstracts import AbstractRamp

__all__ = ('BasicRamp')


class BasicRamp(AbstractRamp):
    """A basic ramp with an angle sensor and two solenoid valves.""" 
    
    HIGH = None
    LOW = None
    digital_write = None
    delay = None

    def __init__(self, angle_input, len_output, short_output, len_delay, 
                 short_delay, len_accu):

        lengthen_args = {
            'output': len_output,
            'delay': len_delay,
        }
        shorten_args = {
            'output': short_output,
            'delay': short_delay,
        }
        self.angle_input = angle_input

        AbstractRamp.__init__(self, lengthen_args, shorten_args, len_accu)

    def get_len(self):
        """Return the length of the ramp."""
        # TODO
        pass

    def move(self, output, delay):
        self.digital_write(output, self.HIGH)
        self.digital_write(output, self.LOW)
        self.delay(delay)
