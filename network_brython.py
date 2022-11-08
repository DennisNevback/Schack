# SSE system for direct messaging
# [sends messages via sse.nodehill.com]
# (Brython version, works in a browser)

# Usage:
# from network_brython import connect, send, close

# connect(channel, user, event_handler)
#
#  Opens the network connection
#  - creates a channel if it doesn't exists
#  - joins the channel
#  - registers a function that will get all messages
#
#  Arguments:
#  * channel        string
#  * user           string
#  * handler        function that will receive
#				    (timestamp, user_name, message)
#                   * timestamp = milliseconds 
#                      since new years eve 1970 GMT
#                   * user_name - string
#                   * message - any 
#                      JSON serializable data type
#

# send(message) 
#    
#  Sends a message
#
#  Argument:
#  * message 	    any JSON serializable data type

# close()
# 
#  Closes the network connection

import json
import urllib.parse
from browser import window
fetch = window.fetch
EventSource = window.EventSource

channel_name = None
user_name = None 
token = None
message_handler = None
evt_src = None
last_message_time = 0
serverURL = 'https://sse.nodehill.com'

def on_token(e):
	global token
	token = json.loads(e.data)

def on_message(e):
	d = json.loads(e.data)
	global last_message_time
	timestamp = d['timestamp']
	last_message_time = timestamp
	user = d['user']
	message = d['data']
	message_handler(timestamp, user, message)

def on_error(e):
	window.console.log('error', e.data)

def connect(channel, user, handler):
	global channel_name, user_name, message_handler, evt_src
	message_handler = handler
	channel_name = urllib.parse.quote(channel)
	user_name = urllib.parse.quote(user)
	evt_src = EventSource.new(f'{serverURL}' +
		f'/api/listen/{channel_name}/' +
		f'{user_name}/{last_message_time}')
	evt_src.addEventListener('message', on_message)
	evt_src.addEventListener('error', on_error)
	evt_src.addEventListener('token', on_token)

def send(message):
	fetch(f'{serverURL}/api/send/{token}', {
		'headers': { 'Content-Type': 'application/json' },
		'method': 'POST',
		'body': json.dumps({'message': message})
	})

def close():
	send('Bye!')
	evt_src.close()