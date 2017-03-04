class God(object):
    def __init__(self, numberOfPersons, ratioPersonsDrivers, ratioUberCabs, cycles):
        self._numberOfPersons = numberOfPersons
        self._ratioPersonsDrivers = ratioPersonsDrivers
        self._ratioUberCabs = ratioUberCabs
        self._cycles = cycles
        self._next_event = 0;

        #init everthing
        
    def _ask_uber(self):
        #1. add Person to a list of watingListOfPersons
        #2. if are Drivers free then
        #2.1 if are Drivers free in less then 5km and are Uber or/and Taxis
        #2.2 create an event of type 2 for the same time of simulation
        #3. Create the next event of this type (1)
        pass

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

        while next_event != 8:
            #run next event
            #update stats
            #get next event
            pass
