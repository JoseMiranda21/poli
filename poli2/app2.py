import socket
# Crear un socket TCP/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Vincular el socket a un puerto conocido
server_address = ('', 12345)
sock.bind(server_address)

# Escuchar conexiones entrantes
sock.listen(1)

while True:
    connection, client_address = sock.accept()
    # Recibir el mensaje del contenedor1
    data = connection.recv(1024)
    # Responder al contenedor1
    response = "Su solicitud de visculación ha sido ingresada con exito"
    connection.sendall(response.encode())
    # Cerrar la conexión
    connection.close()

        
