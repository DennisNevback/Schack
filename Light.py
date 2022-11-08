from random import random
from browser import window
j = window.jQuery

class Light:

    # constructor
    def __init__(self, color, my_traffic_light):
        # create a unique id 
        # (that is also an allowed id in html)
        self.id = 'id' + str(random()).split('.')[1]
        # transfer arguments to attributes
        self.color = color
        self.my_traffic_light = my_traffic_light
        # bind events
        self.bind_events()

    def bind_events(self):
        # Ask jQuery to listen to clicks on the body
        # (the whole content of the window)
        # if a click is on something with my id (self.id)
        # then run my click method
        j('body').on('click', f'#{self.id}', self.click)

    # note all event handlers must accept the event object
    # (even if the don't use it)
    def click(self, event):
        # Dim all lights in my traffic light
        j(f'#{self.my_traffic_light.id} .light').css('opacity', 0.3)
        # Undim me
        j(f'#{self.id}').css('opacity', 1)

    # use __str__ to create
    # a html representation of a TrafficLight instance
    def __str__(self):
        return f"""
            <div class="light {self.color}-color" id="{self.id}">
            </div>
        """
