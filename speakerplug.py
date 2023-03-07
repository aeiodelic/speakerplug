import json
import sys
from PyP100 import PyP100

config = json.load(open('config.json'))

plug = PyP100.P100(config['ip'], config['email'], config['password'])

plug.handshake()
plug.login()

if sys.argv[1] == 'on':
    plug.turnOn()
else:
    plug.turnOff()
