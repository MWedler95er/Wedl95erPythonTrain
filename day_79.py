# pylint: skip-file

import os
import smtplib
from email.message import EmailMessage


def send_email(
    subject: str,
    body: str,
    to_address: str,
    from_address: str | None = None,
    smtp_server: str = "smtp.gmail.com",
    smtp_port: int = 587,
):
    """
    Sendet eine E-Mail mit dem angegebenen Betreff und Text.

    Erwartet folgende Umgebungsvariablen:
    - EMAIL_USER: Absenderadresse (z.B. deine Gmail-Adresse)
    - EMAIL_PASSWORD: App-Passwort oder SMTP-Passwort
    """

    # Hole Zugangsdaten aus Umgebungsvariablen
    email_user = os.environ.get("EMAIL_USER")
    email_password = os.environ.get("EMAIL_PASSWORD")

    if not email_user or not email_password:
        raise RuntimeError(
            "Bitte setze die Umgebungsvariablen EMAIL_USER und EMAIL_PASSWORD."
        )

    if from_address is None:
        from_address = email_user

    # E-Mail zusammenbauen
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = from_address
    msg["To"] = to_address
    msg.set_content(body)

    # Verbindung zum SMTP-Server aufbauen und E-Mail senden
    with smtplib.SMTP(smtp_server, smtp_port) as connection:
        connection.starttls()  # verschlüsselte Verbindung
        connection.login(user=email_user, password=email_password)
        connection.send_message(msg)


if __name__ == "__main__":
    # Debug: Umgebung prüfen
    print("EMAIL_USER:", os.environ.get("EMAIL_USER"))
    print("EMAIL_PASSWORD gesetzt:", bool(os.environ.get("EMAIL_PASSWORD")))

    # Beispiel: E-Mail an eine Schülerin / einen Schüler
    SUBJECT = "Erinnerung an Hausaufgabe"
    BODY = (
        "Hallo,\n\n"
        "dies ist eine automatische Erinnerung: Bitte denke daran, "
        "die Mathe-Hausaufgabe bis morgen mitzubringen.\n\n"
        "Viele Grüße\n"
        "Deine Lehrkraft"
    )
    TO_ADRESS = "michael-wedler95@gmx.de"  # ← hier echte Adresse eintragen

    # E-Mail senden
    send_email(subject=SUBJECT, body=BODY, to_address=TO_ADRESS)
