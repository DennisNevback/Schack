from Board import Board
from browser import window
j = window.jQuery


# Create a new application
j('body').html(str(Board(8, 8)))
