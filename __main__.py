'''
Control the electromag via a slave on localhost:8084. Adapted from https://github.com/Nugget-Industries-2018/depth-slave/blob/master/__main__.py by Bobby Martin
'''

import socket
import RPi.GPIO as GPIO

TCP_IP = 'localhost'
TCP_PORT = 8084
BUFFER_SIZE = 2

PIN = 26
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.OUT)


def process_cmd(cmd):
    if cmd == '1':
        GPIO.output(PIN, GPIO.HIGH)
    elif cmd == '0':
        GPIO.output(PIN, GPIO.LOW)
    else:
        return 'command not recognized: {}'.format(cmd)

while 1:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((TCP_IP, TCP_PORT))
    s.listen(1)
    print('PYTHON: listening at {}:{}'.format(TCP_IP, TCP_PORT))

    conn, addr = s.accept()
    while 1:
        data = conn.recv(BUFFER_SIZE)
        if not data: break
        data = str(data).rstrip('\n')
        print('PYTHON: received: ', data)
        conn.send(str(process_cmd(data)))
