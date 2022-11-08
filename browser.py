# Keep this file as it is, it exists so that pylance/VSC
# refrain from complaining about missing dependencies
# when importing browser / using Brython.

# when we use Brython this file will be ignored
# and Brython objects will be imported instead

# if window == None -> we are not in a browser
window = None

# provide aio/asyncio in for programs that
# can run both with and without Brython
import asyncio as aio 