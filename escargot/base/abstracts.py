__all__ = ('AbstractRamp', 'BasicRamp')


class AbstractRamp:
    
    def __init__(self, accuracy):
        self.accuracy = accuracy

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

        while abs(len(self) - l) > self.accuracy:
            move()

    def shorten(self):
        self.move(**self.short_args)


class BasicRamp(AbstractRamp):
    """A basic ramp with an angle sensor and two solenoid valves.""" 
    
    def __init__(self, angle_input, len_args, short_args, accuracy):

        self.len_args = len_args
        self.short_args = short_args
        self.angle_input = angle_input

        AbstractRamp.__init__(self, accuracy)

    def move(self, output, delay):
        self.pulse(output)
        self.delay(delay)
