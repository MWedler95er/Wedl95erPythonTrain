import os

import requests


def download_file(
    _url: str, save_folder: str = ".", filename: str | None = None
) -> str:
    """
    Lädt eine Datei von einer URL herunter und speichert sie lokal.

    :param url: URL zur Datei (z.B. https://example.com/file.jpg)
    :param save_folder: Ordner, in dem gespeichert wird
    :param filename: Optionaler Dateiname; wenn None, wird der Name aus der URL genommen
    :return: Voller Pfad der gespeicherten Datei
    """
    os.makedirs(save_folder, exist_ok=True)

    # Wenn kein Dateiname angegeben ist, nimm den letzten Teil der URL
    if filename is None:
        filename = _url.split("/")[-1] or "downloaded_file"

    save_path = os.path.join(save_folder, filename)

    print(f"Lade herunter: {_url}")
    response = requests.get(_url, stream=True, timeout=10)
    response.raise_for_status()  # Fehler werfen, wenn Status != 200

    # Datei in Binärmodus schreiben (funktioniert für Bilder, PDFs, etc.)
    with open(save_path, "wb") as f:
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:  # Filtert leere Chunks
                f.write(chunk)

    print(f"Gespeichert als: {save_path}")
    return save_path


if __name__ == "__main__":
    # BEISPIEL: URL und Download-Ordner anpassen
    URL = "https://kasner.org/wp-content/uploads/2025/01/Lorem_ipsum.pdf"  # <- hier deine URL eintragen
    DOWNLOAD_FOLDER = "/home/mwedl95er/testtest/Neuer Ordner"  # <- z.B. dieser Ordner

    download_file(URL, save_folder=DOWNLOAD_FOLDER)
