from . import AbstractRamp 

__all__ = ('AbstractAngleValveRamp')


class AbstractAngleValveRamp(AbstractRamp):
    """An abstract ramp with an angle sensor and two solenoid valves.""" 
    
    def __init__(self, len_args, short_args, *args, **kwargs):
        AbstractRamp.__init__(self, *args, **kwargs)

        self.len_args = len_args
        self.short_args = short_args

    def __len__(self):
        angle = self.get_angle()

        return angle/360.0 * self.max_len

    def delay(self, delay):
        raise NotImplementedError

    def get_angle(self):
        raise NotImplementedError

    def lengthen(self):
        self.move(*self.len_args) 

    def move(self, output, delay):
        self.pulse(output)
        self.delay(delay)

    def pulse(self, output):
        raise NotImplementedError

    def shorten(self):
        self.move(*self.short_args) 
