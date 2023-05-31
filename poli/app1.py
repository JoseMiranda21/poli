import socket

# Crear un socket TCP/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Obtener la dirección IP del contenedor2
container2_ip = socket.gethostbyname('container2')

# Conectar al contenedor2
server_address = (container2_ip, 12345)
sock.connect(server_address)

# Enviar un mensaje al contenedor2
message = "Solicitud de vinculación"
sock.sendall(message.encode())

# Recibir la respuesta del contenedor2
data = sock.recv(1024)
print("Respuesta del contenedor 2:", data.decode())

# Cerrar el socket
sock.close()
