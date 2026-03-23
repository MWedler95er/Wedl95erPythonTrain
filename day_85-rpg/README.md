# Internet-Rettungs-RPG

Ein rundenbasiertes Terminal-RPG in Python. Deutschland hat kein Internet mehr — ein Drache hat die Hauptzentrale besetzt. Du bist die letzte Hoffnung.

## Starten

```bash
cd day_85-rpg
python main.py
```

## Spielprinzip

6 Ebenen, 2 Wege pro Ebene → auf jeder Ebene wartet ein Ereignis (Kampf, Händler, Heilung oder Relikt). Auf Ebene 6 wartet der **Internet-Drache** als Endboss.

## Charaktererstellung

### Rassen

| Rasse  | Stärke              | Rassen-Fähigkeit                          |
|--------|---------------------|-------------------------------------------|
| Mensch | Allrounder          | Befreiung — entfernt alle Debuffs + Konter|
| Elf    | Hoher ATK & SPD     | Besinnung — ATK dauerhaft +8              |
| Zwerg  | Viel HP & DEF       | Zwergentrunk — heilt 40% HP + 28 Rüstung  |
| Ork    | Brutaler Angreifer  | Raserei — Schaden auf 1 + 80% ATK-Boost   |
| Gnom   | Maximale Speed      | Weile — 3 Runden absolut unverwundbar     |

### Klassen

| Klasse       | Rolle                         |
|--------------|-------------------------------|
| Krieger      | Tank & Frontlinie             |
| Magier       | Hoher Schaden, wenig HP       |
| Priester     | Heiler & Support              |
| Schurke      | Schnell, Gift, hinterlistig   |
| Mönch        | Balance aus Angriff & Defense |
| Hexenmeister | Flüche & Seelenentzug         |

> Nicht alle Klassen sind für jede Rasse verfügbar.

## Kampfsystem

Rundenbasiert (Pokemon-Style):

1. Statuseffekte werden verarbeitet (Gift, Feuer, Regen...)
2. Spieler wählt Skill (+ optional Trank oder Rassen-Fähigkeit)
3. NPC-Begleiter agiert automatisch
4. Gegner führen ihre vorher telegraphierten Aktionen aus

Gegner telegraphieren ihre nächste Aktion — du siehst was kommt und kannst reagieren.

## Statuseffekte

| Effekt     | Wirkung                          |
|------------|----------------------------------|
| Gift       | Schaden pro Runde (ignoriert DEF)|
| Feuer      | Schaden pro Runde (ignoriert DEF)|
| Betäubung  | Runde aussetzen (30% Chance)     |
| Schild     | Absorbiert eingehenden Schaden   |
| Stärkung   | ATK-Boost für X Runden           |
| Schwächung | ATK-Malus für X Runden           |
| Regen      | HP-Heilung pro Runde             |

## Gegner

| Gegner             | Besonderheit                  |
|--------------------|-------------------------------|
| Wireguard-Goblin   | Schwach, guter Einstieg       |
| Router-Troll       | Brückenverteidiger            |
| Firewall-Ritter    | Hohe Verteidigung             |
| Malware-Magier     | Wirft Schadcode               |
| DDoS-Dämon         | Mehrfachtreffer               |
| Phishing-Specter   | Schnell & hinterlistig        |
| Trickster-Fee      | Klein aber gefährlich         |
| **Internet-Drache**| **Endboss — 250 HP**          |

## Projektstruktur

```
day_85-rpg/
├── main.py        # Einstiegspunkt & Spielschleife
├── character.py   # Spieler, Gegner, Rassen, Klassen, Companion
├── combat.py      # Rundenbasiertes Kampfsystem
├── skills.py      # Alle Skills & Statuseffekte
├── items.py       # Waffen, Rüstungen, Tränke, Relikte
├── path.py        # Karte, Ereignisse, Pfad-Generierung
└── display.py     # ASCII-Art, Farben, UI-Hilfsfunktionen
```
