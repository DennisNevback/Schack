from random import random
from Light import Light

class TrafficLight:
    
    # constructor
    def __init__(self):
        # create a unique id 
        # (that is also an allowed id in html)
        self.id = 'id' + str(random()).split('.')[1]
        # create three different lights
        self.red_light = Light('red', self)
        self.yellow_light = Light('yellow', self)
        self.green_light = Light('green', self)

    # use __str__ to create
    # a html representation of a TrafficLight instance
    def __str__(self):
        return f"""
            <div class="traffic-light" id="{self.id}">
                {self.red_light}
                {self.yellow_light}
                {self.green_light}
            </div>
        """