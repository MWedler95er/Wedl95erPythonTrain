import socket
import threading

HOST = "127.0.0.1"  # localhost
PORT = 5000  # beliebiger freier Port (>=1024)

# Liste aller verbundenen Clients (Sockets)
clients: list[socket.socket] = []

# Zuordnung: Client-Socket -> Name
client_names: dict[socket.socket, str] = {}


def broadcast(message: bytes, sender_socket: socket.socket | None = None):
    """Sende eine Nachricht an alle verbundenen Clients.
    Wenn sender_socket angegeben ist, wird dieser übersprungen
    (damit man z.B. keine Echos zurück an den Sender schickt)."""
    for client in clients:
        if client is sender_socket:
            continue
        try:
            client.sendall(message)
        except OSError:
            # Falls ein Client-Socket kaputt ist, ignorieren
            pass


def handle_client(conn: socket.socket, addr):
    """Wird in einem eigenen Thread für jeden Client ausgeführt."""
    print(f"Neuer Client verbunden: {addr}")
    clients.append(conn)

    try:
        while True:
            data = conn.recv(1024)
            if not data:
                print(f"Client {addr} hat getrennt.")
                break

            # Zur Kontrolle auf dem Server ausgeben
            message = data.decode("utf-8", errors="replace")
            print(f"Von {addr}: {message}")

            # An alle anderen Clients weiterleiten
            broadcast(data, sender_socket=conn)
    finally:
        # Client sauber aus Liste entfernen und Socket schließen
        if conn in clients:
            clients.remove(conn)
        conn.close()
        print(f"Verbindung zu {addr} geschlossen.")


def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))

    # WICHTIG: jetzt mehr als 1 Verbindung zulassen, z.B. 5
    server_socket.listen(5)
    print(f"Server läuft auf {HOST}:{PORT}, warte auf Verbindungen...")

    try:
        while True:
            conn, addr = server_socket.accept()
            # Für jeden Client einen neuen Thread starten
            client_thread = threading.Thread(
                target=handle_client,
                args=(conn, addr),
                daemon=True,
            )
            client_thread.start()
    finally:
        server_socket.close()


if __name__ == "__main__":
    start_server()
