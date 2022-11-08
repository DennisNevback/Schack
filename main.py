from browser import window
j = window.jQuery
from Application import Application

# Create a new application
j('body').html(str(Application()))