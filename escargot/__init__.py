
__version__ = ''

class AbstractRamp:
    """An abstract interface for all ramps."""
    
    def __init__(self, accuracy, max_len):
        self.accuracy = accuracy
        self.max_len = max_len

    def __len__(self):
        raise NotImplementedError

    def __repr__(self):
        return 'Length: {}/{}'.format(len(self), self.max_len)

    def lengthen(self):
        raise NotImplementedError

    def set_len(self, l):
        dist = l - len(self)

        if dist < 0:
            move = self.shorten
        elif dist > 0:
            move = self.lengthen
        else:
            return

        while (0 < len(self) < self.max_len and
              abs(len(self) - l) > self.accuracy):
            move()

    def shorten(self):
        raise NotImplementedError


from . import angle_valve
