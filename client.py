import ssl
import socket

# Chemin vers le fichier de certificat du serveur
SERVER_CERTFILE = "serverCertificate.pem"

# Configuration SSL
context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
context.load_verify_locations(SERVER_CERTFILE)

# Création du socket client
with socket.create_connection(('localhost', 8443)) as client_socket:
    with context.wrap_socket(client_socket, server_hostname='localhost') as secure_socket:
        secure_socket.sendall(b"Bonjour, serveur!")
        response = secure_socket.recv(1024).decode('utf-8')
        print(f"Réponse du serveur : {response}")
