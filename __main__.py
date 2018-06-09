'''
Control the electromag via a slave on localhost:8084. Adapted from https://github.com/Nugget-Industries-2018/depth-slave/blob/master/__main__.py by Bobby Martin
'''

import socket
from gpiozero import LED # The gpiozero library is already around, and it's easiest to call our electromag an LED because we can turn it on and off.

TCP_IP = 'localhost'
TCP_PORT = 8084
BUFFER_SIZE = 2

electromag = LED(37);
if not electromag:
    print('gpio pin ', electromag.pin, ' could not be initialized')
    exit(1)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)
print('PYTHON: listening at {}:{}'.format(TCP_IP, TCP_PORT))

conn, addr = s.accept()
while sensor.read():
    data = conn.recv(BUFFER_SIZE)
    if not data: break
    data = str(data).rstrip('\n')
    print('PYTHON (electromag-slave): received: ', data)
    if data == 'o':
        electromag.on()
        state = 'high' if electromag.is_lit() else 'low'
        response = 'PYTHON (electromag-slave): told to turn on electromag, pin is' + state
    elif data == 'c':
        electromag.off() 
        state = 'high' if electromag.is_lit() else 'low'
        reponse = 'PYTHON (electromag-slave): told to turn off electromag, pin is' + state
    elif data == 't':
        electromag.toggle()
        state = 'high' if electromag.is_lit() else 'low'
        response = 'PYTHON (electromag-slave): told to toggle electromag, pin is' +  state
    else:
        response = 'command not recognized'
    conn.send(str(response))

