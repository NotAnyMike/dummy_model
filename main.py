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

class UberDriver(Driver):
    def __init__(self):
        super(UberDriver,self).__init__()
        self._comfortability = 1

class CabDriver(Driver):
    def __init__(self):
        super(CabDriver,self).__init__()
        self._comfortability = 0

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

class City(object):
    def __init__(self):
        return None

class God(object):
    def __init__(self, numberOfPersons, ratioPersonsDrivers, ratioUberCabs, cycles):
        self._numberOfPersons = numberOfPersons
        self._ratioPersonsDrivers = ratioPersonsDrivers
        self._ratioUberCabs = ratioUberCabs
        self._cycles = cycles

    def startEverything(self):
        numberOfUbers = self._numberOfPersons/self._ratioPersonsDrivers*self._ratioUberCabs
        numberOfCabs = numberOfUbers/self._ratioUberCabs
        persons = []
        ubers = []
        cabs = []

        for n in range(self._numberOfPersons):
            p = Person()
            persons.append(p)

        for n in range(numberOfUbers):
            u = UberDriver()
            ubers.append(u)

        for n in range(numberOfCabs):
            c = CabDriver()
            cabs.append(c)

        for cycle in range(self._cycles):
            #here will be all the simulation
            #what to do at the beginnig? 
            #1. Ask every agent if is active (only to off agents) (when this happens every agent creates its finish coordinates and its distributions
            #2. Add the active agents to a list of active agents
            #3. Update list of agents being transported
            #
            #4. Get all request from agents and save them into a list
            #5. Do a permutation of that list
            #6. Start asigning taxis by its position in the list
            # 
            # Finish cycle
            print "hello, world"

god = God(1,1,1,1)
god.startEverything()
