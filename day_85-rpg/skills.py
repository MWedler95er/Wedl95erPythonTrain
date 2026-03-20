"""
skills.py — Alle Fähigkeiten und Statuseffekte

Konzept:
  - EffectType: Art des Effekts (Gift, Feuer, Betäubung, ...)
  - Effect:     Ein aktiver Effekt mit Wert und verbleibender Dauer
  - SkillType:  Angriff / Verteidigung / Spezial
  - Skill:      Eine Fähigkeit mit Schaden, Verteidigung, Heilung, Effekten
"""

from __future__ import annotations

import copy
from dataclasses import dataclass
from enum import Enum
from typing import Optional

# ─── Effekttypen ─────────────────────────────────────────────────────────────


class EffectType(Enum):
    POISON = "vergiftet"  # Schaden pro Runde (ignoriert Verteidigung)
    BURN = "brennend"  # Schaden pro Runde (Feuer)
    STUN = "betäubt"  # Runde überspringen
    WEAKEN = "geschwächt"  # ATK des Ziels reduziert (in %)
    REGEN = "regeneriert"  # HP pro Runde heilen
    STRENGTHEN = "gestärkt"  # ATK erhöht (in %)
    SHIELD = "geschützt"  # Absorbiert Schaden (Wert = verbleibende HP des Schilds)


@dataclass
class Effect:
    """
    Repräsentiert einen aktiven Statuseffekt.

    Attribute:
        type:     Art des Effekts
        value:    Schadens-/Heilwert oder %-Bonus
        duration: Verbleibende Runden
    """

    type: EffectType
    value: int
    duration: int

    def tick(self) -> None:
        """Reduziert die Dauer um 1 (am Rundenende aufrufen)."""
        self.duration -= 1

    def is_active(self) -> bool:
        return self.duration > 0

    def __str__(self) -> str:
        return f"{self.type.value}({self.duration}R)"


# ─── Skill-Typen ─────────────────────────────────────────────────────────────


class SkillType(Enum):
    ATTACK = "Angriff"
    DEFENSE = "Verteidigung"
    SPECIAL = "Spezial"


# ─── Skill ───────────────────────────────────────────────────────────────────


@dataclass
class Skill:  # pylint: disable=too-many-instance-attributes
    """
    Eine Fähigkeit des Spielers oder Gegners.

    Attribute:
        id:                 Eindeutige ID (1–25)
        name:               Anzeigename
        skill_type:         Angriff / Verteidigung / Spezial
        description:        Kurze Beschreibung
        damage:             Basisschaden (0 = kein Schaden)
        defense:            Schildpunkte (0 = kein Schild)
        heal:               Heilung (0 = keine Heilung)
        effect:             Optionaler Statuseffekt
        hits:               Anzahl Treffer (für Mehrfachtreffer-Skills)
        ignore_defense_pct: Anteil der Verteidigung der ignoriert wird (0.0–1.0)
        lifesteal_pct:      Anteil des Schadens der als HP zurückkommt (0.0–1.0)
        level:              Aktuelles Skill-Level (steigt durch Level-Up)
    """

    id: int
    name: str
    skill_type: SkillType
    description: str
    damage: int = 0
    defense: int = 0
    heal: int = 0
    effect: Optional[Effect] = None
    hits: int = 1
    ignore_defense_pct: float = 0.0
    lifesteal_pct: float = 0.0
    level: int = 1
    # Für Rassen-Fähigkeiten: max_uses=1 → einmal pro Kampf nutzbar (0 = unbegrenzt)
    max_uses: int = 0
    special_tag: str = ""  # z. B. "elf_besinnung", "mensch_befreiung"

    def get_total_damage(self) -> int:
        """Basisschaden + 10% pro Level über 1."""
        bonus = 1.0 + (self.level - 1) * 0.10
        return int(self.damage * bonus)

    def get_total_defense(self) -> int:
        bonus = 1.0 + (self.level - 1) * 0.10
        return int(self.defense * bonus)

    def get_total_heal(self) -> int:
        bonus = 1.0 + (self.level - 1) * 0.10
        return int(self.heal * bonus)

    def upgrade(self) -> None:
        """Erhöht das Level um 1 (+10% auf alle Werte)."""
        self.level += 1

    def copy(self) -> "Skill":
        """Gibt eine tiefe Kopie zurück (wichtig da Effect ein mutable Objekt ist)."""
        return copy.deepcopy(self)

    def __str__(self) -> str:
        parts = [f"{self.name} (Lv.{self.level}) [{self.skill_type.value}]"]
        if self.damage:
            total = self.get_total_damage() * self.hits
            parts.append(f"DMG:{total}" + (f"×{self.hits}" if self.hits > 1 else ""))
        if self.defense:
            parts.append(f"Schild:{self.get_total_defense()}")
        if self.heal:
            parts.append(f"Heal:{self.get_total_heal()}")
        if self.ignore_defense_pct:
            parts.append(f"Durchdring:{int(self.ignore_defense_pct * 100)}%")
        if self.lifesteal_pct:
            parts.append(f"Lifesteal:{int(self.lifesteal_pct * 100)}%")
        if self.effect:
            parts.append(str(self.effect))
        return " | ".join(parts)


# ─── Hilfsfunktion ───────────────────────────────────────────────────────────


def _e(etype: EffectType, value: int, duration: int) -> Effect:
    """Kurzschreibweise um Effect-Objekte zu erstellen."""
    return Effect(etype, value, duration)


# ─── Alle 25 Skills ──────────────────────────────────────────────────────────

ALL_SKILLS: list[Skill] = [
    # ── Angriffsskills (1–14) ────────────────────────────────────────────────
    Skill(1, "Schwerthieb", SkillType.ATTACK, "Ein solider Schwerthieb.", damage=18),
    Skill(
        2,
        "Doppelschlag",
        SkillType.ATTACK,
        "Zwei schnelle Hiebe à 60% Schaden.",
        damage=11,
        hits=2,
    ),
    Skill(
        3,
        "Schildstoß",
        SkillType.ATTACK,
        "Treffer + 8 Schildpunkte für dich.",
        damage=12,
        defense=8,
    ),
    Skill(
        4,
        "Feuerkugel",
        SkillType.ATTACK,
        "Feuerschaden + Brennen (3 Runden).",
        damage=16,
        effect=_e(EffectType.BURN, 6, 3),
    ),
    Skill(
        5,
        "Blitzschlag",
        SkillType.ATTACK,
        "Blitzschaden + 30% Betäubungschance.",
        damage=20,
        effect=_e(EffectType.STUN, 0, 1),
    ),
    Skill(
        6,
        "Eissplitter",
        SkillType.ATTACK,
        "Eiskristalle + Schwächung des Gegners (2 Runden).",
        damage=14,
        effect=_e(EffectType.WEAKEN, 20, 2),
    ),
    Skill(7, "Dolchstoß", SkillType.ATTACK, "Hoher Einzelschaden.", damage=28),
    Skill(
        8,
        "Giftstich",
        SkillType.ATTACK,
        "Vergiftet den Gegner (4 Runden).",
        damage=8,
        effect=_e(EffectType.POISON, 7, 4),
    ),
    Skill(
        9,
        "Schattenschlag",
        SkillType.ATTACK,
        "Ignoriert 50% der Verteidigung.",
        damage=20,
        ignore_defense_pct=0.5,
    ),
    Skill(
        10,
        "Heilige Klinge",
        SkillType.ATTACK,
        "Schaden + Heilt 30% des verursachten Schadens.",
        damage=18,
        lifesteal_pct=0.3,
    ),
    Skill(
        11,
        "Fluch",
        SkillType.ATTACK,
        "Dunkle Magie brennt die Seele (3 Runden).",
        damage=10,
        effect=_e(EffectType.BURN, 8, 3),
    ),
    Skill(
        12,
        "Seelenentzug",
        SkillType.ATTACK,
        "Stiehlt Lebenskraft (60% Lifesteal).",
        damage=15,
        lifesteal_pct=0.6,
    ),
    Skill(13, "Faustsalve", SkillType.ATTACK, "3 schnelle Treffer.", damage=10, hits=3),
    Skill(
        14,
        "Donnertritt",
        SkillType.ATTACK,
        "Kraftvoller Tritt + Betäubung (1 Runde).",
        damage=22,
        effect=_e(EffectType.STUN, 0, 1),
    ),
    # ── Verteidigungsskills (15–20) ──────────────────────────────────────────
    Skill(
        15, "Schildwall", SkillType.DEFENSE, "Hoher Schild für diese Runde.", defense=28
    ),
    Skill(
        16,
        "Ausweichen",
        SkillType.DEFENSE,
        "Schild + Stärkung (+20% ATK, 2 Runden).",
        defense=10,
        effect=_e(EffectType.STRENGTHEN, 20, 2),
    ),
    Skill(
        17,
        "Magieschild",
        SkillType.DEFENSE,
        "Magischer Schild absorbiert Schaden für 2 Runden.",
        defense=22,
        effect=_e(EffectType.SHIELD, 15, 2),
    ),
    Skill(18, "Heilung", SkillType.DEFENSE, "Stellt 30 HP wieder her.", heal=30),
    Skill(
        19,
        "Göttl. Schutz",
        SkillType.DEFENSE,
        "Verteidigung + Heilung in einem.",
        defense=15,
        heal=15,
    ),
    Skill(
        20,
        "Meditation",
        SkillType.DEFENSE,
        "Tiefe Ruhe: Heilung + Regeneration (3 Runden).",
        heal=20,
        effect=_e(EffectType.REGEN, 8, 3),
    ),
    # ── Spezialskills (21–25) ────────────────────────────────────────────────
    Skill(
        21,
        "Kampfschrei",
        SkillType.SPECIAL,
        "Erhöht eigene ATK um 30% für 3 Runden.",
        effect=_e(EffectType.STRENGTHEN, 30, 3),
    ),
    Skill(
        22,
        "Verfluchung",
        SkillType.SPECIAL,
        "Schwächt Gegner: -30% ATK für 3 Runden.",
        effect=_e(EffectType.WEAKEN, 30, 3),
    ),
    Skill(
        23,
        "Rauchbombe",
        SkillType.SPECIAL,
        "Schaden + Schwächung des Gegners.",
        damage=10,
        effect=_e(EffectType.WEAKEN, 25, 2),
    ),
    Skill(
        24,
        "Blutdurst",
        SkillType.SPECIAL,
        "Rage-Modus: Massive Stärkung für 2 Runden.",
        effect=_e(EffectType.STRENGTHEN, 40, 2),
    ),
    Skill(
        25,
        "Volles Internet",
        SkillType.SPECIAL,
        "5G aktiviert! Zufälliger mächtiger Effekt.",
        damage=15,
        heal=15,
        effect=_e(EffectType.STRENGTHEN, 20, 2),
    ),
    # ══════════════════════════════════════════════════════════════════════════
    # KLASSEN-SPEZIFISCHE SKILLS (26–85)
    # ══════════════════════════════════════════════════════════════════════════
    # ── Krieger (26–35) ──────────────────────────────────────────────────────
    Skill(
        26,
        "Helmspalter",
        SkillType.ATTACK,
        "Gewaltiger Hieb — schwächt die Verteidigung des Gegners.",
        damage=38,
        effect=_e(EffectType.WEAKEN, 20, 2),
    ),
    Skill(
        27,
        "Wirbelwind",
        SkillType.ATTACK,
        "Dreht sich wie ein Kreisel — 3 Treffer.",
        damage=15,
        hits=3,
        ignore_defense_pct=0.3,
    ),
    Skill(
        28,
        "Blutopfer",
        SkillType.ATTACK,
        "Schmerz treibt dich an — massiver Schaden.",
        damage=48,
    ),
    Skill(
        29,
        "Eiserne Haut",
        SkillType.DEFENSE,
        "Haut wie Stahl — massiver Schild.",
        defense=42,
    ),
    Skill(
        30,
        "Waffenwurf",
        SkillType.ATTACK,
        "Geschossenes Eisen ignoriert Rüstung.",
        damage=30,
        ignore_defense_pct=0.70,
    ),
    Skill(
        31,
        "Kriegsgebrüll",
        SkillType.SPECIAL,
        "Das Brüllen eines Kriegers — ATK massiv erhöht.",
        effect=_e(EffectType.STRENGTHEN, 50, 3),
    ),
    Skill(
        32,
        "Sturmangriff",
        SkillType.ATTACK,
        "Voller Sprint — Schaden + Betäubungschance.",
        damage=32,
        effect=_e(EffectType.STUN, 0, 1),
    ),
    Skill(
        33,
        "Blutrausch",
        SkillType.ATTACK,
        "Rasender Angriff — 5 Treffer mit Lifesteal.",
        damage=8,
        hits=5,
        lifesteal_pct=0.20,
    ),
    Skill(
        34,
        "Schildschlag",
        SkillType.ATTACK,
        "Mit dem Schild angreifen — DMG + eigener Schild.",
        damage=20,
        defense=25,
    ),
    Skill(
        35,
        "Letzter Stand",
        SkillType.ATTACK,
        "Wenn alles verloren scheint — ein letzter Schlag.",
        damage=52,
    ),
    # ── Magier (36–45) ───────────────────────────────────────────────────────
    Skill(
        36,
        "Arkaner Blitz",
        SkillType.ATTACK,
        "Konzentrierte Arkankraft trifft mit voller Wucht.",
        damage=45,
        ignore_defense_pct=0.30,
    ),
    Skill(
        37,
        "Frostexplosion",
        SkillType.ATTACK,
        "Eisige Explosion — 2 Treffer + Schwächung.",
        damage=22,
        hits=2,
        effect=_e(EffectType.WEAKEN, 25, 2),
    ),
    Skill(
        38,
        "Zeitverzerrung",
        SkillType.SPECIAL,
        "Die Zeit verlangsamt sich — Gegner betäubt.",
        damage=10,
        effect=_e(EffectType.STUN, 0, 2),
    ),
    Skill(
        39,
        "Magische Barriere",
        SkillType.DEFENSE,
        "Eine Wand aus purer Magie — massiver Schild.",
        defense=48,
    ),
    Skill(
        40,
        "Arkane Überlastung",
        SkillType.ATTACK,
        "Zu viel Magie auf einmal — ignoriert Rüstung komplett.",
        damage=55,
        ignore_defense_pct=1.0,
    ),
    Skill(
        41,
        "Manaschild",
        SkillType.DEFENSE,
        "Schild + Magie-Regen für 3 Runden.",
        defense=35,
        effect=_e(EffectType.REGEN, 10, 3),
    ),
    Skill(
        42,
        "Kältewelle",
        SkillType.ATTACK,
        "Eiswind schwächt und schadet.",
        damage=20,
        effect=_e(EffectType.WEAKEN, 30, 3),
    ),
    Skill(
        43,
        "Arkanexplosion",
        SkillType.ATTACK,
        "Doppelte Arkanenergie — 2 Schläge.",
        damage=25,
        hits=2,
    ),
    Skill(
        44,
        "Dimensionsriss",
        SkillType.ATTACK,
        "Reißt ein Loch in die Realität — ignoriert Rüstung.",
        damage=42,
        ignore_defense_pct=0.85,
    ),
    Skill(
        45,
        "Magiemeisterschaft",
        SkillType.ATTACK,
        "Die ultimative Zauberkunst — massiver Schaden.",
        damage=62,
    ),
    # ── Priester (46–55) ─────────────────────────────────────────────────────
    Skill(
        46,
        "Heiliges Licht",
        SkillType.ATTACK,
        "Blendendes Licht — Schaden + kleine Heilung.",
        damage=25,
        heal=20,
    ),
    Skill(
        47,
        "Bannfluch",
        SkillType.SPECIAL,
        "Entfernt Debuffs + Stärkung für 2 Runden.",
        effect=_e(EffectType.STRENGTHEN, 20, 2),
        special_tag="remove_debuffs",
    ),
    Skill(
        48,
        "Göttliche Gnade",
        SkillType.DEFENSE,
        "Gottes Schutz — Schild + Heilung.",
        defense=30,
        heal=25,
    ),
    Skill(
        49,
        "Segen",
        SkillType.SPECIAL,
        "Göttlicher Segen — Stärkung + Regeneration.",
        effect=_e(EffectType.STRENGTHEN, 40, 3),
    ),
    Skill(
        50,
        "Heiliger Zorn",
        SkillType.ATTACK,
        "Göttlicher Zorn — Schaden + Lifesteal.",
        damage=32,
        lifesteal_pct=0.50,
    ),
    Skill(
        51,
        "Exorzismus",
        SkillType.ATTACK,
        "Treibt das Böse aus — schwächt stark.",
        damage=35,
        effect=_e(EffectType.WEAKEN, 40, 2),
    ),
    Skill(
        52,
        "Gebet",
        SkillType.DEFENSE,
        "Stilles Gebet — starke Regeneration für 5 Runden.",
        effect=_e(EffectType.REGEN, 15, 5),
    ),
    Skill(
        53,
        "Martyrium",
        SkillType.ATTACK,
        "Schmerz als Waffe — Schaden + Schild.",
        damage=38,
        defense=18,
    ),
    Skill(
        54,
        "Massenheilung",
        SkillType.DEFENSE,
        "Eine Welle göttlicher Heilung.",
        heal=62,
    ),
    Skill(
        55,
        "Göttl. Eingreifen",
        SkillType.DEFENSE,
        "Dreifach-Combo: Schaden, Heilung, Schild.",
        damage=18,
        heal=28,
        defense=20,
    ),
    # ── Schurke (56–65) ──────────────────────────────────────────────────────
    Skill(
        56,
        "Meuchelmord",
        SkillType.ATTACK,
        "Aus dem Schatten — hoher Schaden, ignoriert Rüstung.",
        damage=50,
        ignore_defense_pct=0.60,
    ),
    Skill(
        57,
        "Klingenregen",
        SkillType.ATTACK,
        "Messer überall — 4 Treffer + Gift.",
        damage=10,
        hits=4,
        effect=_e(EffectType.POISON, 8, 4),
    ),
    Skill(
        58,
        "Konterattacke",
        SkillType.ATTACK,
        "Schlag zurück — Schaden + eigene Stärkung.",
        damage=35,
        effect=_e(EffectType.STRENGTHEN, 30, 2),
    ),
    Skill(
        59,
        "Hinterhalt",
        SkillType.ATTACK,
        "Überraschungsangriff — ignoriert die Hälfte der Rüstung.",
        damage=45,
        ignore_defense_pct=0.50,
    ),
    Skill(
        60,
        "Diebstahl",
        SkillType.ATTACK,
        "Klaut und schwächt — Schaden + starke Schwächung.",
        damage=15,
        effect=_e(EffectType.WEAKEN, 40, 2),
    ),
    Skill(
        61,
        "Fallensteller",
        SkillType.ATTACK,
        "Eine Falle — Schaden + langes Gift.",
        damage=20,
        effect=_e(EffectType.POISON, 10, 4),
    ),
    Skill(
        62,
        "Tödlicher Tanz",
        SkillType.ATTACK,
        "5 rasende Treffer — unaufhaltbar.",
        damage=13,
        hits=5,
    ),
    Skill(
        63,
        "Schattenform",
        SkillType.DEFENSE,
        "Im Schatten — Schild + Stärkung.",
        defense=35,
        effect=_e(EffectType.STRENGTHEN, 25, 2),
    ),
    Skill(
        64,
        "Nervengift",
        SkillType.ATTACK,
        "Gift in den Adern — Schaden + Brennen.",
        damage=12,
        effect=_e(EffectType.BURN, 10, 3),
    ),
    Skill(
        65,
        "Klingenmeister",
        SkillType.ATTACK,
        "Meisterlicher Doppelschlag — 50% Rüstungsdurchdringung.",
        damage=25,
        hits=2,
        ignore_defense_pct=0.40,
    ),
    # ── Mönch (66–75) ────────────────────────────────────────────────────────
    Skill(
        66,
        "Innere Stille",
        SkillType.DEFENSE,
        "Tiefe Ruhe — Heilung + Regeneration.",
        heal=40,
        effect=_e(EffectType.REGEN, 10, 3),
    ),
    Skill(
        67,
        "Drachenklaue",
        SkillType.ATTACK,
        "Drei Klauen — 3 Treffer + eigene Stärkung.",
        damage=13,
        hits=3,
        effect=_e(EffectType.STRENGTHEN, 20, 2),
    ),
    Skill(
        68,
        "Windschritt",
        SkillType.ATTACK,
        "Blitzschnell — Schaden + Ausweich-Stärkung.",
        damage=28,
        effect=_e(EffectType.STRENGTHEN, 30, 2),
    ),
    Skill(
        69,
        "Chakra-Stoß",
        SkillType.ATTACK,
        "Spirituelle Energie — Schaden + Schild.",
        damage=35,
        defense=18,
    ),
    Skill(
        70,
        "Eiserner Körper",
        SkillType.DEFENSE,
        "Stahl-Haltung — massiver Schild + Stärkung.",
        defense=38,
        effect=_e(EffectType.STRENGTHEN, 20, 3),
    ),
    Skill(
        71,
        "Sieben-Schlag-Combo",
        SkillType.ATTACK,
        "Sieben Schläge in einem Atemzug.",
        damage=9,
        hits=7,
    ),
    Skill(
        72,
        "Erleuchtung",
        SkillType.SPECIAL,
        "Geistige Klarheit — massiv gestärkt für 2 Runden.",
        effect=_e(EffectType.STRENGTHEN, 60, 2),
    ),
    Skill(
        73,
        "Naturheilung",
        SkillType.DEFENSE,
        "Die Natur heilt — starke Heilung.",
        heal=52,
    ),
    Skill(
        74,
        "Schwerkraftschlag",
        SkillType.ATTACK,
        "Schwer wie ein Felsbrocken — Schaden + Betäubung.",
        damage=40,
        effect=_e(EffectType.STUN, 0, 1),
    ),
    Skill(
        75,
        "Geistesblitz",
        SkillType.ATTACK,
        "Schnell wie ein Gedanke — Schaden + Regen.",
        damage=35,
        effect=_e(EffectType.REGEN, 12, 3),
    ),
    # ── Hexenmeister (76–85) ─────────────────────────────────────────────────
    Skill(
        76,
        "Seelenpakt",
        SkillType.SPECIAL,
        "Verkauft die Seele — massiv gestärkt für 2 Runden.",
        effect=_e(EffectType.STRENGTHEN, 70, 2),
    ),
    Skill(
        77,
        "Blutmagie",
        SkillType.ATTACK,
        "Blut als Waffe — hoher Schaden + 40% Lifesteal.",
        damage=55,
        lifesteal_pct=0.40,
    ),
    Skill(
        78,
        "Verdammnis",
        SkillType.ATTACK,
        "Ewiges Feuer — Schaden + langer Brenneffekt.",
        damage=15,
        effect=_e(EffectType.BURN, 10, 4),
    ),
    Skill(
        79,
        "Dunkle Pforte",
        SkillType.ATTACK,
        "Ein Riss in die Dunkelheit — ignoriert alle Rüstung.",
        damage=45,
        ignore_defense_pct=1.0,
    ),
    Skill(
        80,
        "Schattenklon",
        SkillType.ATTACK,
        "Der Klon greift mit — 2 Treffer.",
        damage=30,
        hits=2,
    ),
    Skill(
        81,
        "Pakt des Todes",
        SkillType.ATTACK,
        "Tötet und stiehlt — 80% Lifesteal.",
        damage=40,
        lifesteal_pct=0.80,
    ),
    Skill(
        82,
        "Nekromantie",
        SkillType.ATTACK,
        "Dunkle Magie schwächt und schadet.",
        damage=30,
        effect=_e(EffectType.WEAKEN, 50, 2),
    ),
    Skill(
        83,
        "Eldritch-Explosion",
        SkillType.ATTACK,
        "Uralte Magie explodiert — 50% Rüstungsdurchdringung.",
        damage=50,
        ignore_defense_pct=0.50,
    ),
    Skill(
        84,
        "Teufelspakt",
        SkillType.SPECIAL,
        "Der Teufel zahlt — 80% Stärkung für 2 Runden.",
        effect=_e(EffectType.STRENGTHEN, 80, 2),
    ),
    Skill(
        85,
        "Chaosmagie",
        SkillType.ATTACK,
        "Unberechenbare Magie — Schaden + langer Brenneffekt.",
        damage=22,
        effect=_e(EffectType.BURN, 10, 3),
    ),
    # ══════════════════════════════════════════════════════════════════════════
    # RASSEN-FÄHIGKEITEN (91–95) — je einmal pro Kampf nutzbar
    # ══════════════════════════════════════════════════════════════════════════
    Skill(
        91,
        "Raserei",
        SkillType.SPECIAL,
        "ORK: Eingehender Schaden → 1 für diesen Zug + 80% Stärkung.",
        defense=999,
        effect=_e(EffectType.STRENGTHEN, 80, 1),
        max_uses=1,
    ),
    Skill(
        92,
        "Besinnung",
        SkillType.SPECIAL,
        "ELF: Erhöht ATK dauerhaft um 8 (innere Konzentration).",
        max_uses=1,
        special_tag="elf_besinnung",
    ),
    Skill(
        93,
        "Zwergentrunk",
        SkillType.DEFENSE,
        "ZWERG: Heilt 40% max HP + 28 Rüstung für diesen Zug.",
        defense=28,
        max_uses=1,
        special_tag="zwerg_trunk",
    ),
    Skill(
        94,
        "Weile",
        SkillType.DEFENSE,
        "GNOM: Wird 3 Runden unverwundbar (Schild: 500).",
        defense=500,
        effect=_e(EffectType.SHIELD, 500, 3),
        max_uses=1,
    ),
    Skill(
        95,
        "Befreiung",
        SkillType.SPECIAL,
        "MENSCH: Entfernt alle Debuffs + zufälliger Gegenangriff (20 DMG).",
        damage=20,
        max_uses=1,
        special_tag="mensch_befreiung",
    ),
]

# ─── Lookup-Tabellen ─────────────────────────────────────────────────────────

# Schneller Zugriff per ID
SKILL_BY_ID: dict[int, Skill] = {s.id: s for s in ALL_SKILLS}

# Klassen-spezifische Skill-IDs (10 pro Klasse)
CLASS_SKILL_POOL: dict[str, list[int]] = {
    "Krieger": list(range(26, 36)),
    "Magier": list(range(36, 46)),
    "Priester": list(range(46, 56)),
    "Schurke": list(range(56, 66)),
    "Mönch": list(range(66, 76)),
    "Hexenmeister": list(range(76, 86)),
}

# Rassen-Fähigkeiten
RACIAL_SKILL_ID: dict[str, int] = {
    "Ork": 91,
    "Elf": 92,
    "Zwerg": 93,
    "Gnom": 94,
    "Mensch": 95,
}
