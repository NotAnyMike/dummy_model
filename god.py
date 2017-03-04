class God(object):
    def __init__(self, numberOfPersons, ratioPersonsDrivers, ratioUberCabs, cycles):
        #here it will initialize everthing
        self._numberOfPersons = numberOfPersons
        self._ratioPersonsDrivers = ratioPersonsDrivers
        self._ratioUberCabs = ratioUberCabs
        self._cycles = cycles
        self._next_event = 0;

        self._eventSelector = {
            0: None, #Neutral
            1: None, #Ask for driver
            2: None, #Asign Driver
            3: None, #Enter Driver
            4: None, #Leave Driver
            5: None, #Finish simulation
        }

    def startEverything(self):
        numberOfUbers = self._numberOfPersons/self._ratioPersonsDrivers*self._ratioUberCabs
        numberOfCabs = numberOfUbers/self._ratioUberCabs
        persons = []
        ubers = []
        cabs = []

        for n in range(self._numberOfPersons):
            p = Person()
            persons.append(p)

        for n in range(self._numberOfUbers):
            u = UberDriver()
            ubers.append(u)

        for n in range(self._numberOfCabs):
            c = CabDriver()
            cabs.append(c)

        while self._next_event != 5:
            #run next event
            #update stats
            #get next event
            pass
