__all__ = ('AbstractRamp')


class AbstractRamp:
    
    def __init__(self, lengthen_args, shorten_args, len_accu):
        self.len_accu = len_accu
        self.lengthen_args = lengthen_args
        self.shorten_args = shorten_args

    def get_len(self):
        """Return the length of the ramp."""
        
        raise NotImplementedError("The 'get_len' method must be implemented.")

    def lengthen(self):
        self.move(**self.lengthen_args)

    def move(self, **kwargs):
        raise NotImplementedError("The 'move' method must be implemented.")

    def set_len(self, l):
        """Set the length of the ramp."""

        dist = l - self.get_len()

        if dist < 0:
            move = self.shorten
        elif dist > 0:
            move = self.lengthen
        else:
            return

        while abs(self.get_len() - l) > self.len_accu:
            move()

    def shorten(self):
        self.move(**self.shorten_args)
