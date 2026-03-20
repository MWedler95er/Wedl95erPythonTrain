"""
Day 90: Concurrency and Parallelism
-----------------------------------

Dieses Skript zeigt:

1. Concurrency mit Threads (I/O-bound Beispiel mit time.sleep)
2. Parallelism mit Prozessen (CPU-bound Beispiel mit einer rechenintensiven Funktion)
3. Vergleich mit einer einfachen, seriellen Variante

Starte das Skript und beobachte die Laufzeiten der einzelnen Varianten.
"""

import threading
import time
from multiprocessing import Pool, cpu_count
from typing import List

# ============================================================
# 1. I/O-bound Beispiel: time.sleep simulierter Netzwerk-Request
# ============================================================


def fake_io_operation(duration: float, index: int) -> None:
    """Simuliert eine langsame I/O-Operation (z. B. HTTP-Request)."""
    print(f"[IO {index}] Start (sleep {duration}s)")
    time.sleep(duration)
    print(f"[IO {index}] Ende")


def io_serial(n: int = 5, duration: float = 1.0) -> None:
    """Führt n I/O-Operationen nacheinander aus (seriell)."""
    print("\n--- I/O Serial ---")
    start = time.perf_counter()
    for i in range(n):
        fake_io_operation(duration, i)
    end = time.perf_counter()
    print(f"Serielle I/O-Zeit: {end - start:.2f} Sekunden\n")


def io_with_threads(n: int = 5, duration: float = 1.0) -> None:
    """
    Führt n I/O-Operationen mit Threads aus.

    Idee:
    - I/O-Operationen warten viel (sleep, Netzwerk, Festplatte).
    - Während ein Thread wartet, kann ein anderer Thread laufen.
    - Daher bringen Threads bei I/O-bound meist echten Speedup,
      trotz GIL.
    """
    print("\n--- I/O mit Threads ---")
    start = time.perf_counter()

    threads: List[threading.Thread] = []

    for i in range(n):
        t = threading.Thread(target=fake_io_operation, args=(duration, i))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    end = time.perf_counter()
    print(f"Threaded I/O-Zeit: {end - start:.2f} Sekunden\n")


# ============================================================
# 2. CPU-bound Beispiel: naive Primzahlprüfung
# ============================================================


def is_prime(n: int) -> bool:
    """Einfache (ineffiziente) Primzahlprüfung, CPU-bound."""
    if n < 2:
        return False
    # absichtlich nicht optimiert, damit es rechenintensiv bleibt
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def count_primes_serial(numbers: List[int]) -> int:
    """Zählt Primzahlen seriell."""
    print("\n--- CPU Serial ---")
    start = time.perf_counter()
    count = sum(1 for n in numbers if is_prime(n))
    end = time.perf_counter()
    print(f"Serielle CPU-Zeit: {end - start:.2f} Sekunden")
    return count


def _is_prime_wrapper(n: int) -> int:
    """Wrapper für multiprocessing.Pool (1 oder 0 zurückgeben)."""
    return 1 if is_prime(n) else 0


def count_primes_multiprocessing(numbers: List[int]) -> int:
    """
    Zählt Primzahlen mit multiprocessing.Pool.

    Idee:
    - CPU-bound Aufgabe (viel Rechnen).
    - Threads bringen wegen GIL wenig / keinen Speedup.
    - Prozesse (multiprocessing) umgehen das GIL, mehrere Kerne
      können gleichzeitig rechnen.
    """
    print("\n--- CPU mit multiprocessing ---")
    start = time.perf_counter()
    with Pool(processes=cpu_count()) as pool:
        results = pool.map(_is_prime_wrapper, numbers)
    count = sum(results)
    end = time.perf_counter()
    print(f"Multiprocessing CPU-Zeit: {end - start:.2f} Sekunden")
    return count


# ============================================================
# 3. Mini-Demo im Hauptblock
# ============================================================


def demo_io():
    """
    Demonstriert Concurrency (Threads) mit I/O-bound Arbeit.
    """
    print("### I/O-bound Demo (Concurrency mit Threads) ###")
    # 5 Tasks à 1 Sekunde
    io_serial(n=5, duration=1.0)
    io_with_threads(n=5, duration=1.0)
    print("Erwartung: Thread-Version sollte deutlich schneller sein.\n")


def demo_cpu():
    """
    Demonstriert Parallelism (multiprocessing) mit CPU-bound Arbeit.
    """
    print("### CPU-bound Demo (Parallelism mit multiprocessing) ###")
    # Liste von Zahlen, die relativ groß sind, damit es etwas dauert
    numbers = [200_000 + i for i in range(50)]  # 20 Zahlen

    count1 = count_primes_serial(numbers)
    count2 = count_primes_multiprocessing(numbers)

    print(f"Primzahlen seriell:         {count1}")
    print(f"Primzahlen multiprocessing: {count2}")
    print("Erwartung: Multiprocessing sollte schneller sein (Mehrkern-CPU).\n")


if __name__ == "__main__":
    # Du kannst die Demos einzeln oder gemeinsam laufen lassen:
    demo_io()
    demo_cpu()
