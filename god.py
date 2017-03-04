class God(object):
    def __init__(self, numberOfPersons, ratioPersonsDrivers, ratioUberCabs, cycles):
        self._numberOfPersons = numberOfPersons
        self._ratioPersonsDrivers = ratioPersonsDrivers
        self._ratioUberCabs = ratioUberCabs
        self._cycles = cycles
        self._next_event = 0;

        #init everthing

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

        while next_event != 5:
            #run next event
            #update stats
            #get next event
            pass
