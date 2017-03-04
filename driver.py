class Driver(object):
    def __init__(self):
        self._person = None
        self._coordinates = None
        self._state = 0
        self._comfortability = 0

    @property
    def person(self):
        return self._person

    @person.getter
    def person(self): return self._person

    @person.setter
    def person(self,value):
        self._coordinates = value

    @property
    def coordinates(self):
        return self._coordinates 

    @coordinates.getter
    def coordinates(self):
        return self._coordinates

    @coordinates.setter
    def coordinates(self,value):
        self._coordinates = value

    @property 
    def state(self): 
        return self._state

    @state.getter
    def state(self):
        return self._state

    @state.setter
    def state(self,value):
        self._state = value

    @property
    def comfortability(self):
        return self._comfortability

    @comfortability.getter
    def comfortability(self):
        return self._comfortability

    @comfortability.setter
    def comfortability(self,value):
        self._comfortability = value
