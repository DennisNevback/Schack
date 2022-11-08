from random import random
from browser import window
j = window.jQuery
from TrafficLight import TrafficLight

class Application:

    def __init__(self):
        # create a unique id 
        # (that is also an allowed id in html)
        self.id = 'id' + str(random()).split('.')[1]
        # create 4 traffic lights
        self.traffic_lights = []
        for i in range(1,5):
            self.traffic_lights.append(TrafficLight())

    def __str__(self):
        return f"""
            <div class="application" id={self.id}>
              {''.join([str(item) for item in self.traffic_lights])}
            </div>
        """
