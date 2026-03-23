import os


def rename_files_in_folder(
    folder_path: str,
    prefix: str = "file_",
    start_number: int = 1,
    keep_extension: bool = True,
) -> None:
    """
    Benennt alle Dateien in einem Ordner automatisch um.

    Beispiel:
    folder_path="C:/Users/du/Bilder",
    prefix="bild_",
    start_number=1
    -> bild_1.jpg, bild_2.jpg, ...

    :param folder_path: Pfad zum Ordner mit den Dateien
    :param prefix: Prefix für die neuen Dateinamen
    :param start_number: Startnummer für die Benennung
    :param keep_extension: Dateiendungen beibehalten (True/False)
    """
    # Alle UNTERORDNER im Ordner auflisten
    files = sorted(
        f
        for f in os.listdir(folder_path)
        if os.path.isdir(os.path.join(folder_path, f))
    )

    counter = start_number

    for filename in files:
        old_path = os.path.join(folder_path, filename)

        if keep_extension:
            _, ext = os.path.splitext(filename)  # trennt Namen und .ext
        else:
            ext = ""

        new_name = f"{prefix}{counter}{ext}"
        new_path = os.path.join(folder_path, new_name)

        # Falls der Name schon existiert, Zahl hochzählen bis frei
        while os.path.exists(new_path):
            counter += 1
            new_name = f"{prefix}{counter}{ext}"
            new_path = os.path.join(folder_path, new_name)

        print(f"Rename: {filename} -> {new_name}")
        os.rename(old_path, new_path)
        counter += 1


if __name__ == "__main__":
    # HIER den Ordnerpfad anpassen!
    FOLDER = r"/home/mwedl95er/testtest/Neuer Ordner"

    # Beispielaufruf:
    rename_files_in_folder(
        folder_path=FOLDER, prefix="Ordnerererer", start_number=1, keep_extension=True
    )
