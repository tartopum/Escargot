__all__ = ('AbstractRamp', 'BasicRamp')


class AbstractRamp:
    
    def __init__(self, max_len, accuracy):
        self.accuracy = accuracy
        self.max_len = max_len

    def lengthen(self):
        self.move(**self.len_args)

    def set_len(self, l):
        dist = l - len(self)

        if dist < 0:
            move = self.shorten
        elif dist > 0:
            move = self.lengthen
        else:
            return

        while 0 <= len(self) <= self.max_len and abs(len(self) - l) > self.accuracy:
            move()

    def shorten(self):
        self.move(**self.short_args)


class BasicRamp(AbstractRamp):
    """A basic ramp with an angle sensor and two solenoid valves.""" 
    
    def __init__(self, max_len, angle_input, len_args, short_args, accuracy):

        self.len_args = len_args
        self.short_args = short_args
        self.angle_input = angle_input

        AbstractRamp.__init__(self, max_len, accuracy)

    def __len__(self):
        angle = self.get_angle()

        return angle/360.0 * self.max_len

    def move(self, output, delay):
        self.pulse(output)
        self.delay(delay)
