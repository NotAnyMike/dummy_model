from driver import Driver

class CabDriver(Driver):
    def __init__(self):
        super(CabDriver,self).__init__()
        self._comfortability = 0
