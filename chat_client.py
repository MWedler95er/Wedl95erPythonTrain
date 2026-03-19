import socket
import threading

HOST = "127.0.0.1"  # gleiche Adresse wie Server
PORT = 5000  # gleicher Port wie Server


def receive_messages(sock: socket.socket):
    """Läuft in einem eigenen Thread und empfängt Nachrichten vom Server."""
    try:
        while True:
            data = sock.recv(1024)
            if not data:
                print("\nVerbindung zum Server verloren.")
                break
            message = data.decode("utf-8", errors="replace")
            print(f"\n{message}")
    except OSError:
        # Socket wurde wahrscheinlich vom Hauptthread geschlossen
        pass
    finally:
        print("Empfangs-Thread beendet.")


def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Mit dem Server verbinden
    client_socket.connect((HOST, PORT))
    print(f"Verbunden mit Server {HOST}:{PORT}")

    # Namen/Nickname abfragen
    name = input("Dein Name: ").strip() or "Unbekannt"

    # Namen an den Server senden (Sonderformat)
    name_message = f"__NAME__:{name}"
    client_socket.sendall(name_message.encode("utf-8"))

    # Thread starten, der Nachrichten vom Server empfängt
    recv_thread = threading.Thread(
        target=receive_messages,
        args=(client_socket,),
        daemon=True,
    )
    recv_thread.start()

    try:
        while True:
            msg = input("> ")
            if msg.lower() in ("quit", "exit"):
                print("Beende Chat.")
                break

            full_message = f"{name}: {msg}"
            client_socket.sendall(full_message.encode("utf-8"))
    finally:
        # Socket schließen -> recv-Thread wird Fehler bekommen und enden
        client_socket.close()
        print("Verbindung geschlossen.")


if __name__ == "__main__":
    start_client()
