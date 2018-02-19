import socket


# create client socket
socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# initialize and empty list to hold the message (an array of strings)
message = []

# ask user for the operation they want to perform
operation = input(
    """
        CPT411 Math Server
        
        Please select an operation to perform:
        1 - Addition
        2 - Subtraction
        3 - Multiplication
        4 - Division    5 - Modulus
    """
)

# add operation to message
message.append(str(operation))

# ask user for the two values on which the operation is performed
input1 = input('enter the first value: >_ ')
input2 = input('enter the second value: >_ ')

# add the values to the message
message.append(str(input1))
message.append(str(input2))

# format message into [operation,first_varible,second_variable]
message = ' '.join(message)

# send message to client-side
socket.sendto(message, ('localhost', 15000))

# receive result from server
result, server = socket.recvfrom(1024*4)
print('server result: ' + result)

# close connection between client and server
socket.close();
