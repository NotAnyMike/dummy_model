class God(object):
    def __init__(self, numberOfPersons, ratioPersonsDrivers, ratioUberCabs, cycles):
        #here it will initialize everthing
        self._numberOfPersons = numberOfPersons
        self._ratioPersonsDrivers = ratioPersonsDrivers
        self._ratioUberCabs = ratioUberCabs
        self._cycles = cycles
        self._next_event = 0;

        #init everthing
        
    #Event 1
    def _ask_driver(self):
        #1. add Person to a FIFO list of watingListOfPersons
        #2. Create the event of type 2, its time should be sim_time (actual time)
        #3. Create the next event of this type (1)
        pass

    #Event 2
    def _search_driver(self):
        #1. get list of drivers which match the filters
        #2. if empty do nothing
        #3. else: get the closes driver to it and asign it
        #4. Create time of event of type 3 with t=sim_time
        pass

    #Event 3
    def _asign_driver(self):
        #1. Remove driver from list of free drivers
        #2. Create the event for the next event of type 4 base on coordinates (i.e. time)
        pass

    #Event 4
    def _driver_arrives_at_initial_point(self):
        # this method is just in order to update statics (?)
        #1. Create the event of type 5 for the same time as sim_time
        pass

    #Event 5
    def _person_takes_driver(self):
        #1. Create the event of type 6 based on coordinates
        pass

    #Event 6
    def _arrives_at_destination(self):
        #1. Create the event of type 7 with t=sim_time
        #2. And desactivate person
        pass

    #Event 7
    def _driver_is_free(self):
        #1. Create time for event of type 3 with t=sim_time
        #2. Add driver to list of free drivers
        pass
    
    self._eventSelector = {
        0: None, #Neutral
        1: None, #Ask for driver
        2: None, #Search for driver
        3: None, #Asign Driver
        4: None, #Driver arrives at initial point
        5: None, #Person Takes driver 
        6: None, #Driver arrives at destination 
        7: None, #Driver is free
        8: None, #Finish simulation
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

        while next_event != 8:
            #run next event
            #update stats
            #get next event
            pass
