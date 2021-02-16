import socket                   # Import socket module
import time

s = socket.socket()             # Create a socket object
host = socket.gethostname()     # Get local machine name
port = 60000                    # Reserve a port for your service.

connected = False
while not connected:
    try:
        s.connect((host,port))
        connected = True
        print('Connection established!')
    except Exception as e:
        print('Waiting for Server...')
        time.sleep(0.5)
        pass #Do nothing, just try again

#s.connect((host, port))
#s.send("Hello server!")

with open('parameters.json', 'wb') as f:
    print ('file opened')
    while True:
        print('receiving data...')
        data = s.recv(1024)
        print('data=%s', (data))
        if not data:
            break
        # write data to a file
        f.write(data)

f.close()
print('Successfully received the configuration file!')
s.close()
print('connection closed')
time.sleep(5)

# import socket

# TCP_IP = 'localhost'
# TCP_PORT = 9001
# BUFFER_SIZE = 1024

# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.connect((TCP_IP, TCP_PORT))
# with open('received_file', 'wb') as f:
#     print 'file opened'
#     while True:
#         #print('receiving data...')
#         data = s.recv(BUFFER_SIZE)
#         print('data=%s', (data))
#         if not data:
#             f.close()
#             print 'file close()'
#             break
#         # write data to a file
#         f.write(data)

# print('Successfully got the file')
# s.close()
# print('connection closed')
