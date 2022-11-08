from Application import Application
from browser import window
j = window.jQuery

# Create a new application
j('body').html(str(Application()))
