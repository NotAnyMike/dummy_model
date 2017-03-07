from person import Person 

class God(object):
    def __init__(self, number_of_persons, ratio_persons_drivers, ratio_uber_cabs, max_time):
        #init everything
        self._number_of_persons = number_of_persons
        self._ratio_persons_drivers = ratio_persons_drivers
        self._ratio_uber_cabs = ratio_uber_cabs
        self._max_time = max_time

        self._time_next_events = [max_time]*9
        self._type_of_closest_event = 0;
        self._sim_time = 0

        #give a value to the ask driver event to let everything start
        self._time_next_events[1] = self._sim_time

        self._number_of_ubers = self._number_of_persons/self._ratio_persons_drivers*self._ratio_uber_cabs
        self._number_of_cabs = number_of_ubers/self._ratio_uber_cabs
        self._persons = []
        self._ubers = []
        self._cabs = []

        for n in range(self._number_of_persons):
            p = Person()
            self._persons.append(p)

        for n in range(self._number_of_ubers):
            u = UberDriver()
            self._ubers.append(u)

        for n in range(self._number_of_cabs):
            c = CabDriver()
            self._cabs.append(c)
        
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
        while self._type_of_closest_event != 8:
            #get next event
            self._timer()

            #Run closes event
            self._eventSelector[self._type_of_closest_event]()

            #update stats      
