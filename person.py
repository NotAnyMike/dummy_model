class Person(object):
    def __init__(self):
        self._id = None
        self._hperiods = None
        self._coordinates_sp = None
        self._coordinates_fp = None
        self._driver = None
        self._state = 0

    @property
    def id(self):
        return self._id

    @id.getter
    def id(self):
        return self._id

    @id.setter
    def id(self,value):
        self._id = value

    @property
    def hperiods(self):
        return self._hperiods

    @hperiods.getter
    def hperiods(self):
        return self._hperiods

    @hperiods.setter
    def hperiods(self,value):
        self._hperiods = value

    @property
    def coordinates_sp(self):
        return self._coordinates_sp

    @coordinates_sp.getter
    def coordinates_sp(self):
        return self._coordinates_sp

    @coordinates_sp.setter
    def coordinates_sp(self,value):
        self._coordinates_sp = value

    @property
    def coordinates_fp(self):
        return self._coordinates_fp

    @coordinates_fp.getter
    def coordinates_fp(self):
        return self._coordinates_fp

    @coordinates_fp.setter
    def coordinates_fp(self,value):
        self._coordinates_fp = value

    @property
    def driver(self):
        return self._driver

    @driver.getter
    def driver(self):
        return self._driver

    @driver.setter
    def driver(self,value):
        self._driver = value

    @property
    def state(self):
        return self._state

    @state.getter
    def state(self):
        return self._state

    @state.setter
    def state(self,value):
        self._state = value    

    def cabFunction():
        return None

    def uberFunction():
        return None

    def isActive():
        #if not active then
        #look at distribution
        #if dist == true
        #asign all varaibles
        #if false return false
        return false
