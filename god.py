class God(object):
    def __init__(self, numberOfPersons, ratioPersonsDrivers, ratioUberCabs, max_time):
        #init everything
        self._numberOfPersons = numberOfPersons
        self._ratioPersonsDrivers = ratioPersonsDrivers
        self._ratioUberCabs = ratioUberCabs
        self._max_time = max_time

        self._time_next_events = [max_time]*9
        self._type_of_closest_event = 0;
        self._sim_time = 0

        #give a value to the ask driver event to let everything start
        #TODO: Change to a real random number
        self._time_next_events[1] = 0.1
        
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

    #This function will make _type_of_closest_event have the value of the closes event
    def _timer(self):
        self._type_of_closest_event = self._max_time + 1
        for i in range(7):
            if self._time_next_events[i+1] < self._type_of_closest_event:
                self._type_of_closest_event = self._time_next_events[i+1]     
    
    self._eventSelector = {
        0: None, #Neutral
        1: _ask_driver, #Ask for driver
        2: _search_driver, #Search for driver
        3: _asign_driver, #Asign Driver
        4: _driver_arrives_at_initial_point, #Driver arrives at initial point
        5: _person_takes_driver, #Person Takes driver 
        6: _arrives_at_destination, #Driver arrives at destination 
        7: _driver_is_free, #Driver is free
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

        while self._type_of_closest_event != 8:
            #get next event
            _timer()

            #Run closes event
            self._eventSelector[self._type_of_closest_event]()

            #update stats      
