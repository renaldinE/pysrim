### PYSRIM : Python wrapper for SRIM calculation
### Project initiated by : Christopher Ostrouchov
### Modified by : Victor Garric : victor.garric@gmail.com, 2018


class Target(object):
    """ Target that Ion impacts

    """
    def __init__(self, layers):
        self.layers = layers

    @property
    def width(self):
        """ total width of target """
        return sum(layer.width for layer in self.layers)
