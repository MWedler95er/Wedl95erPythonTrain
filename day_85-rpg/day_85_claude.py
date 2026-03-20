"""
Day 85 — Hausaufgabe: Text-Based RPG
Einstiegspunkt → startet das Spiel aus dem day_85-rpg Ordner
"""

import os
import sys

from main import run_game

# Ordner zum Suchpfad hinzufügen damit Python die Module findet
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "day_85-rpg"))


if __name__ == "__main__":
    run_game()
