import escargot as es

__all__ = ('AbstractRamp')


class AbstractRamp(es.AbstractRamp):
    """An abstract ramp with an angle sensor and two solenoid valves.""" 
    
    def __init__(self, len_args, short_args, max_angle, accuracy, max_len):
        super().__init__(accuracy, max_len)

        self.len_args = len_args
        self.short_args = short_args
        self.max_angle = max_angle

    def __len__(self):
        angle = self.get_angle()

        return angle/self.max_angle * self.max_len

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
