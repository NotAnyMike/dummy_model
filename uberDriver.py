from driver import Driver

class UberDriver(Driver):
    def __init__(self):
        super(UberDriver,self).__init__()
        self._comfortability = 1
