import time

import schedule


# Wrapper Variablen für Zähler und Job
def mittag_call(job):
    # eigenen Zähler am Job hochzählen
    job.call_count += 1
    print("\\//" * 20)
    print("Essen's Zeit!")
    print(f"Guten Mittag Michael, Aufruf Nr. {job.call_count}")

    # nach 5 Aufrufen: Job beenden
    if job.call_count >= 5:
        print("Genug erinnert, beende den 5-Sekunden-Job.")
        print("\\//" * 20)
        schedule.cancel_job(job)


def _mittag_wrapper():
    """Funktion, die vom Scheduler aufgerufen wird."""
    job = _mittag_wrapper.job  # Job-Objekt aus der Funktion holen
    mittag_call(job)  # eigentliche Logik ausführen


def start_5s_reminder_job():
    print("Starte 5-Sekunden-Reminder-Job.")
    job = schedule.every(5).seconds.do(_mittag_wrapper)
    job.call_count = 0  # Zähler an den Job „dranhängen“
    _mittag_wrapper.job = job  # Job in der Wrapper-Funktion merken


# ende Variante Wrapper


# # globale Variablen für Zähler und Job
#
# call_count = 0
# mittag_job = None
#
# def mittag_call():
#     global call_count, mittag_job
#     call_count += 1
#     print("\\//" * 20)
#     print("Essen's Zeit!")
#     print(f"Guten Mittag Michael, Aufruf Nr. {call_count}")
#
#     # nach 5 Aufrufen: Job beenden
#     if call_count >= 5:
#         print("Genug erinnert, beende den 5-Sekunden-Job.")
#         print("\\//" * 20)
#         schedule.cancel_job(mittag_job)
#
# def start_5s_reminder_job():
#     global mittag_job, call_count
#     print("Starte 5-Sekunden-Reminder-Job.")
#     call_count = 0  # Zähler zurücksetzen, wenn der Job neu gestartet wird
#     mittag_job = schedule.every(5).seconds.do(mittag_call)
#
# Ende Variante Global

# Jeden Tag um 12:00 den 5-Sekunden-Job starten
schedule.every().day.at("12:26:30").do(start_5s_reminder_job)

# !Endlosschleife!, die die geplanten Jobs ausführt
while True:
    schedule.run_pending()
    time.sleep(1)
