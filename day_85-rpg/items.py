"""
items.py — Gegenstände: Waffen, Rüstungen, Tränke, Relikte

Loot-Wahrscheinlichkeiten pro Drop:
  - Verflucht:  5%  (negativer Effekt)
  - Relikt:     4%  (seltener, dauerhafter Buff)
  - Waffe:     26%
  - Rüstung:   25%
  - Trank:     15%
  - Nichts:    25%
"""

from __future__ import annotations

import random
from dataclasses import dataclass
from enum import Enum
from typing import Optional


class ItemType(Enum):
    WEAPON = "Waffe"
    ARMOR = "Rüstung"
    POTION = "Trank"
    RELIC = "Relikt"
    CURSED = "Verflucht"


class Rarity(Enum):
    COMMON = "Gewöhnlich"
    UNCOMMON = "Ungewöhnlich"
    RARE = "Selten"
    CURSED = "Verflucht"


@dataclass
class Item:  # pylint: disable=too-many-instance-attributes
    """
    Repräsentiert einen Gegenstand.

    Flache Boni (+N) werden direkt auf den Stat addiert.
    Prozentuale Boni (pct) werden als Multiplikator angewendet.
    Negative pct = Malus (für verfluchte Items).
    """

    name: str
    item_type: ItemType
    rarity: Rarity
    description: str
    # Flache Boni
    atk_bonus: int = 0
    def_bonus: int = 0
    spd_bonus: int = 0
    hp_bonus: int = 0
    # Prozentuale Boni (0.15 = +15%)
    atk_pct: float = 0.0
    def_pct: float = 0.0
    spd_pct: float = 0.0
    hp_pct: float = 0.0
    # Tränke
    heal_amount: int = 0

    def __str__(self) -> str:
        bonuses = []
        if self.atk_bonus:
            bonuses.append(f"ATK+{self.atk_bonus}")
        if self.def_bonus:
            bonuses.append(f"DEF+{self.def_bonus}")
        if self.spd_bonus:
            bonuses.append(f"SPD+{self.spd_bonus}")
        if self.hp_bonus:
            bonuses.append(f"HP+{self.hp_bonus}")
        if self.atk_pct:
            bonuses.append(
                f"ATK{'+' if self.atk_pct > 0 else ''}{int(self.atk_pct * 100)}%"
            )
        if self.def_pct:
            bonuses.append(
                f"DEF{'+' if self.def_pct > 0 else ''}{int(self.def_pct * 100)}%"
            )
        if self.spd_pct:
            bonuses.append(
                f"SPD{'+' if self.spd_pct > 0 else ''}{int(self.spd_pct * 100)}%"
            )
        if self.hp_pct:
            bonuses.append(
                f"HP{'+' if self.hp_pct > 0 else ''}{int(self.hp_pct * 100)}%"
            )
        if self.heal_amount:
            bonuses.append(f"Heilt {self.heal_amount} HP")
        bonus_str = ", ".join(bonuses) if bonuses else "keine Boni"
        return f"{self.name} [{self.rarity.value}] — {bonus_str}"


# ─── Item-Tabellen ───────────────────────────────────────────────────────────

WEAPONS: list[Item] = [
    Item(
        "Rostiges Schwert",
        ItemType.WEAPON,
        Rarity.COMMON,
        "Ein altes, rostiges Schwert.",
        atk_bonus=5,
    ),
    Item(
        "Eisenschwert",
        ItemType.WEAPON,
        Rarity.COMMON,
        "Ein solides Eisenschwert.",
        atk_bonus=10,
    ),
    Item(
        "Elfenbogen",
        ItemType.WEAPON,
        Rarity.UNCOMMON,
        "Leichter Bogen der Waldlinge.",
        atk_bonus=8,
        spd_bonus=3,
    ),
    Item(
        "Zwergenaxt",
        ItemType.WEAPON,
        Rarity.UNCOMMON,
        "Schwere Axt aus Zwergenschmiede.",
        atk_bonus=15,
        spd_bonus=-2,
    ),
    Item(
        "Verseuchter Stab",
        ItemType.WEAPON,
        Rarity.UNCOMMON,
        "Gift tropft von der Klinge.",
        atk_bonus=12,
    ),
    Item(
        "Heiliger Hammer",
        ItemType.WEAPON,
        Rarity.RARE,
        "Vom Licht gesegnet.",
        atk_bonus=18,
    ),
    Item(
        "Drachentöter",
        ItemType.WEAPON,
        Rarity.RARE,
        "Eigentlich das, was wir suchen...",
        atk_bonus=25,
    ),
]

ARMORS: list[Item] = [
    Item(
        "Lederrüstung", ItemType.ARMOR, Rarity.COMMON, "Leichter Schutz.", def_bonus=5
    ),
    Item(
        "Kettenhemd", ItemType.ARMOR, Rarity.COMMON, "Mittlerer Schutz.", def_bonus=10
    ),
    Item(
        "Plattenrüstung",
        ItemType.ARMOR,
        Rarity.UNCOMMON,
        "Schwerer Schutz, macht dich langsamer.",
        def_bonus=15,
        spd_bonus=-2,
    ),
    Item(
        "Elfengewand",
        ItemType.ARMOR,
        Rarity.UNCOMMON,
        "Leicht und schützend.",
        def_bonus=8,
        spd_bonus=2,
    ),
    Item(
        "Mönchsgewand",
        ItemType.ARMOR,
        Rarity.UNCOMMON,
        "Stärkt Körper und Geist.",
        def_bonus=10,
        hp_bonus=15,
    ),
    Item(
        "Drachenschuppen",
        ItemType.ARMOR,
        Rarity.RARE,
        "Schuppen eines längst besiegten Drachen.",
        def_bonus=22,
    ),
]

POTIONS: list[Item] = [
    Item(
        "Kleiner Heiltrank",
        ItemType.POTION,
        Rarity.COMMON,
        "Stellt 20 HP wieder her.",
        heal_amount=20,
    ),
    Item(
        "Heiltrank",
        ItemType.POTION,
        Rarity.COMMON,
        "Stellt 40 HP wieder her.",
        heal_amount=40,
    ),
    Item(
        "Großer Heiltrank",
        ItemType.POTION,
        Rarity.UNCOMMON,
        "Stellt 80 HP wieder her.",
        heal_amount=80,
    ),
    Item(
        "Stärketrank",
        ItemType.POTION,
        Rarity.UNCOMMON,
        "Dauerhaft +8 ATK.",
        atk_bonus=8,
    ),
]

RELICS: list[Item] = [
    Item(
        "Amulett der Stärke",
        ItemType.RELIC,
        Rarity.RARE,
        "Dauerhaft +15% ATK.",
        atk_pct=0.15,
    ),
    Item(
        "Ring der Verteidigung",
        ItemType.RELIC,
        Rarity.RARE,
        "Dauerhaft +15% DEF.",
        def_pct=0.15,
    ),
    Item(
        "Talisman der Eile",
        ItemType.RELIC,
        Rarity.RARE,
        "Dauerhaft +15% SPD.",
        spd_pct=0.15,
    ),
    Item(
        "Herz des Drachen",
        ItemType.RELIC,
        Rarity.RARE,
        "Dauerhaft +20% max HP.",
        hp_pct=0.20,
    ),
    Item(
        "Zerbrochenes Modem",
        ItemType.RELIC,
        Rarity.RARE,
        "Trotzdem +10% auf alles. Irgendwie.",
        atk_pct=0.10,
        def_pct=0.10,
        spd_pct=0.10,
    ),
]

CURSED_ITEMS: list[Item] = [
    Item(
        "Verfluchter Ring",
        ItemType.CURSED,
        Rarity.CURSED,
        "Oh nein. -10% ATK.",
        atk_pct=-0.10,
    ),
    Item(
        "Bleifüße",
        ItemType.CURSED,
        Rarity.CURSED,
        "Du kannst dich kaum bewegen. -15% SPD.",
        spd_pct=-0.15,
    ),
    Item(
        "Kaputtes Modem",
        ItemType.CURSED,
        Rarity.CURSED,
        "Kein Internet. -5% auf alles.",
        atk_pct=-0.05,
        def_pct=-0.05,
        spd_pct=-0.05,
    ),
]


# ─── Loot-Funktion ───────────────────────────────────────────────────────────


def get_random_loot(
    include_relics: bool = False, cursed_chance: float = 0.05
) -> Optional[Item]:
    """
    Gibt einen zufälligen Gegenstand zurück oder None.

    Wahrscheinlichkeiten:
        cursed_chance → verfluchtes Item
        4%            → Relikt (nur wenn include_relics=True)
        26%           → Waffe
        25%           → Rüstung
        15%           → Trank
        Rest          → nichts
    """
    roll = random.random()

    if roll < cursed_chance:
        return random.choice(CURSED_ITEMS)

    roll -= cursed_chance

    if include_relics and roll < 0.04:
        return random.choice(RELICS)

    roll -= 0.04 if include_relics else 0.0

    if roll < 0.26:
        return random.choice(WEAPONS)
    if roll < 0.51:
        return random.choice(ARMORS)
    if roll < 0.66:
        return random.choice(POTIONS)

    return None
