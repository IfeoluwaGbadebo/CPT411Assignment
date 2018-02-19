import socket


# Create a TCP/IP socket
socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Create server address
server = ('localhost',  15000)
print('Server waiting for connection')

# Bind socket to the server_address
socket.bind(server)

# the math function
def math(message):
    # split message to remove the comms ','
    message = message.split(' ')

    # assign the values of the operation and variables
    operation = message[0]
    input1 = int(message[1])
    input2 = int(message[2])

    # perform operation
    if operation == '1':
        return input1 + input2
    elif operation == '2':
        return input1 - input2
    elif operation == '3':
        return input1 * input2
    elif operation == '4':
        return input1 / input2
    elif operation == '5':
        return input1 % input2
    else:
        print('invalid operation')

# wait for a connection using an infinite loop
while True:
    print('Server is waiting for a connection...')
    # receive message from client and the client address
    message, address = socket.recvfrom(1024*4)
    # compute the result
    result = str(math(message))
    # send result back to client
    socket.sendto(result, address)
