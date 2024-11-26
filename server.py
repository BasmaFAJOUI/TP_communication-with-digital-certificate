import ssl
import socket

# Chemins vers les fichiers PEM
CERTFILE = "serverCertificate.pem"  # Certificat au format PEM
KEYFILE = "serverKey.pem"           # Clé privée au format PEM

# Configuration SSL
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile=CERTFILE, keyfile=KEYFILE)

# Création du socket serveur
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind(('localhost', 8443))
    server_socket.listen(5)
    print("Serveur en attente de connexions...")

    # Wrapping SSL autour du socket
    with context.wrap_socket(server_socket, server_side=True) as secure_socket:
        client_socket, addr = secure_socket.accept()
        print(f"Connexion acceptée depuis {addr}")
        data = client_socket.recv(1024).decode('utf-8')
        print(f"Reçu : {data}")
        client_socket.sendall(b"Message received!")
