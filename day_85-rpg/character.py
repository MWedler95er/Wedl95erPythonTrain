"""
character.py — Spieler, Gegner, Rassen und Klassen

Vererbungshierarchie:
    Character          ← Basisklasse (HP, ATK, DEF, SPD, Effekte, Skills)
    ├── Player         ← Spielercharakter (Level, XP, Inventar, Ausrüstung)
    └── Enemy          ← Gegner (Template-basiert, skalierbar)
"""

from __future__ import annotations

import random
from dataclasses import dataclass, field
from typing import Optional

from items import Item, ItemType
from skills import (
    ALL_SKILLS,
    CLASS_SKILL_POOL,
    RACIAL_SKILL_ID,
    SKILL_BY_ID,
    Effect,
    EffectType,
    Skill,
)

# ─── Rassen ──────────────────────────────────────────────────────────────────


@dataclass
class Race:  # pylint: disable=too-many-instance-attributes
    name: str
    description: str  # Kurzbeschreibung
    lore: str  # Meme-Hintergrundgeschichte
    racial_ability: str  # Name der Rassen-Fähigkeit
    racial_desc: str  # Beschreibung der Rassen-Fähigkeit
    hp_bonus: int = 0
    atk_bonus: int = 0
    def_bonus: int = 0
    spd_bonus: int = 0
    allowed_classes: list[str] = field(default_factory=list)


RACES: dict[str, Race] = {
    "Mensch": Race(
        name="Mensch",
        description="Ausgewogen in allem — ein guter Allrounder.",
        lore=(
            "Der klassische Normi-German-NPC. Geht jeden Morgen zur Arbeit, "
            "zahlt brav Rundfunkgebühren und beschwert sich übers Wetter. "
            "Ohne Internet weiß er nicht mehr was er mit sich anfangen soll."
        ),
        racial_ability="Befreiung",
        racial_desc="Entfernt alle Debuffs und kontert sofort mit einem zufälligen Angriff.",
        hp_bonus=10,
        atk_bonus=2,
        def_bonus=2,
        spd_bonus=2,
        allowed_classes=["Mönch", "Priester", "Schurke"],
    ),
    "Elf": Race(
        name="Elf",
        description="Schnell und magisch begabt, aber zerbrechlich.",
        lore=(
            "Die Oberschicht in Elfenform. Braucht das Internet um Aktien zu "
            "handeln, NFTs zu kaufen und auf LinkedIn Motivationssprüche zu "
            "posten. Ohne DAX-Kurs ist der Elf praktisch funktionsunfähig. "
            "Hat natürlich einen Zweitwohnsitz in der Schweiz."
        ),
        racial_ability="Besinnung",
        racial_desc="Innere Konzentration: Erhöht ATK dauerhaft um 8.",
        hp_bonus=0,
        atk_bonus=5,
        def_bonus=0,
        spd_bonus=5,
        allowed_classes=["Priester", "Magier", "Hexenmeister"],
    ),
    "Zwerg": Race(
        name="Zwerg",
        description="Zäh und ausdauernd, etwas langsamer.",
        lore=(
            "Der Nationaltrinker — Ballermann-Veteran und Bierzelt-Legende. "
            "Braucht das Internet um Schunkelsongs auf YouTube zu hören und "
            "Fotos vom Ballermann 6 hochzuladen. Sein Schnauzer ist sein "
            "Markenzeichen, sein Maßkrug sein bester Freund."
        ),
        racial_ability="Zwergentrunk",
        racial_desc="Ein kräftiger Schluck: Heilt 40% max HP + 28 Rüstung für diesen Zug.",
        hp_bonus=20,
        atk_bonus=3,
        def_bonus=5,
        spd_bonus=-2,
        allowed_classes=["Krieger", "Priester", "Mönch"],
    ),
    "Ork": Race(
        name="Ork",
        description="Brutal und stark, wenig Finesse.",
        lore=(
            "Der wütende Fußballfan der sein Spiel nicht sehen kann. "
            "Hat extra einen 85-Zoll-Fernseher gekauft, aber dank des Drachen "
            "kein IPTV mehr. Sein Blutdruck ist auf Rekordniveau. "
            "Trikot von 2006 ist seine Rüstung."
        ),
        racial_ability="Raserei",
        racial_desc="WUUUT! Schaden auf 1 reduziert diesen Zug + 80% ATK-Boost.",
        hp_bonus=15,
        atk_bonus=8,
        def_bonus=0,
        spd_bonus=-1,
        allowed_classes=["Krieger", "Mönch", "Hexenmeister"],
    ),
    "Gnom": Race(
        name="Gnom",
        description="Klein, flink und trickreich.",
        lore=(
            "Der klassische Geek-Nerd. Hat den Drachen wahrscheinlich schon "
            "in einem Reddit-Thread predicted. Braucht das Internet für "
            "GitHub, Steam-Downloads und 47 offene Browser-Tabs. "
            "Trägt ein Linux-T-Shirt. Jeden Tag."
        ),
        racial_ability="Weile",
        racial_desc="AFK für 3 Runden — absolut unverwundbar (Schild: 500).",
        hp_bonus=-5,
        atk_bonus=0,
        def_bonus=0,
        spd_bonus=8,
        allowed_classes=["Schurke", "Hexenmeister", "Krieger"],
    ),
}


# ─── Klassen ─────────────────────────────────────────────────────────────────


@dataclass
class CharClass:
    name: str
    description: str
    base_hp: int
    base_atk: int
    base_def: int
    base_spd: int
    skill_pool: list[int]  # Skill-IDs aus ALL_SKILLS


CLASSES: dict[str, CharClass] = {
    "Krieger": CharClass(
        "Krieger",
        "Stark, zäh, direkt — lebt auf der Frontlinie.",
        base_hp=100,
        base_atk=12,
        base_def=10,
        base_spd=6,
        skill_pool=[1, 2, 3, 15, 16, 21, 24],
    ),
    "Magier": CharClass(
        "Magier",
        "Magische Kraft — hoher Schaden, wenig HP.",
        base_hp=70,
        base_atk=8,
        base_def=5,
        base_spd=8,
        skill_pool=[4, 5, 6, 17, 25],
    ),
    "Priester": CharClass(
        "Priester",
        "Heiler mit heiliger Kraft — überleben durch Support.",
        base_hp=85,
        base_atk=8,
        base_def=8,
        base_spd=7,
        skill_pool=[10, 18, 19, 20, 21],
    ),
    "Schurke": CharClass(
        "Schurke",
        "Schnell, giftig, hinterlistig — trifft bevor man ihn sieht.",
        base_hp=75,
        base_atk=10,
        base_def=5,
        base_spd=12,
        skill_pool=[7, 8, 9, 16, 23],
    ),
    "Mönch": CharClass(
        "Mönch",
        "Balance zwischen Angriff und Verteidigung.",
        base_hp=90,
        base_atk=10,
        base_def=8,
        base_spd=10,
        skill_pool=[13, 14, 16, 20, 21],
    ),
    "Hexenmeister": CharClass(
        "Hexenmeister",
        "Dunkle Magie, Flüche und Seelenentzug.",
        base_hp=75,
        base_atk=9,
        base_def=5,
        base_spd=8,
        skill_pool=[11, 12, 22, 23, 24, 25],
    ),
}


# ─── Basischarakter ───────────────────────────────────────────────────────────


class Character:  # pylint: disable=too-many-instance-attributes
    """
    Basisklasse für alle Charaktere (Spieler und Gegner).

    Enthält: HP, Basis-Stats, Statuseffekte, Skills.
    Leitet ATK dynamisch aus base_atk + aktiven Effekten ab.
    """

    def __init__(  # pylint: disable=too-many-arguments,too-many-positional-arguments
        self, name: str, max_hp: int, atk: int, def_: int, spd: int
    ) -> None:
        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp
        self.base_atk = atk
        self.base_def = def_
        self.base_spd = spd
        self.effects: list[Effect] = []
        self.skills: list[Skill] = []

    # ── Properties ───────────────────────────────────────────────────────────

    @property
    def atk(self) -> int:
        """ATK berechnet: base_atk × (1 + Stärkungs-% - Schwächungs-%)."""
        strengthen = sum(
            e.value for e in self.effects if e.type == EffectType.STRENGTHEN
        )
        weaken = sum(e.value for e in self.effects if e.type == EffectType.WEAKEN)
        total = self.base_atk * (1 + strengthen / 100 - weaken / 100)
        return max(1, int(total))

    @property
    def def_(self) -> int:
        return self.base_def

    @property
    def spd(self) -> int:
        return self.base_spd

    @property
    def is_alive(self) -> bool:
        return self.hp > 0

    @property
    def is_stunned(self) -> bool:
        return any(e.type == EffectType.STUN and e.is_active() for e in self.effects)

    # ── Kampf-Methoden ───────────────────────────────────────────────────────

    def take_damage(self, amount: int, ignore_def_pct: float = 0.0) -> int:
        """
        Berechnet und wendet Schaden an.

        Formel: Schaden = max(1, eingehender_Schaden - effektive_Verteidigung)
        Schild-Effekte werden zuerst verbraucht.

        Returns: Tatsächlich erlittener Schaden
        """
        effective_def = int(self.base_def * (1 - ignore_def_pct))

        # Schild verbrauchen
        shield_effects = [e for e in self.effects if e.type == EffectType.SHIELD]
        shield_total = sum(e.value for e in shield_effects)
        absorbed = min(shield_total, max(0, amount - effective_def))

        for e in shield_effects:
            reduction = min(e.value, absorbed)
            e.value -= reduction
            absorbed -= reduction
            if absorbed <= 0:
                break

        actual = max(1, amount - effective_def - absorbed)
        self.hp = max(0, self.hp - actual)
        # Erschöpfte Schilde entfernen
        self.effects = [
            e
            for e in self.effects
            if not (e.type == EffectType.SHIELD and e.value <= 0)
        ]
        return actual

    def heal(self, amount: int) -> int:
        """Heilt HP (nicht über max_hp). Returns: tatsächlich geheilte Menge."""
        before = self.hp
        self.hp = min(self.max_hp, self.hp + amount)
        return self.hp - before

    def add_effect(self, effect: Effect) -> None:
        """Fügt Effekt hinzu. Ersetzt bestehenden Effekt desselben Typs."""
        self.effects = [e for e in self.effects if e.type != effect.type]
        self.effects.append(Effect(effect.type, effect.value, effect.duration))

    def process_effects(self) -> list[str]:
        """
        Verarbeitet alle aktiven Effekte am Rundenanfang.
        Gibt Liste von Beschreibungs-Strings zurück.
        """
        messages = []
        for effect in list(self.effects):
            if effect.type == EffectType.POISON:
                dmg = self.take_damage(effect.value, ignore_def_pct=1.0)
                messages.append(f"{self.name} erleidet {dmg} Giftschaden.")
            elif effect.type == EffectType.BURN:
                dmg = self.take_damage(effect.value, ignore_def_pct=1.0)
                messages.append(f"{self.name} erleidet {dmg} Brandschaden.")
            elif effect.type == EffectType.REGEN:
                healed = self.heal(effect.value)
                messages.append(f"{self.name} regeneriert {healed} HP.")
            effect.tick()

        # Abgelaufene Effekte entfernen
        self.effects = [e for e in self.effects if e.is_active()]
        return messages

    def get_effect_summary(self) -> str:
        """Kurzübersicht aller aktiven Effekte."""
        return "  ".join(str(e) for e in self.effects)


# ─── Spieler ─────────────────────────────────────────────────────────────────


class Player(Character):  # pylint: disable=too-many-instance-attributes
    """
    Spielercharakter — erbt von Character.

    Zusätzlich: Level/XP, Inventar, Ausrüstung, Relikte.
    """

    def __init__(self, name: str, race: Race, char_class: CharClass) -> None:
        hp = char_class.base_hp + race.hp_bonus
        atk = char_class.base_atk + race.atk_bonus
        def_ = char_class.base_def + race.def_bonus
        spd = char_class.base_spd + race.spd_bonus
        super().__init__(name, hp, atk, def_, spd)

        self.race = race
        self.char_class = char_class
        self.level = 1
        self.xp = 0
        self.xp_to_next = 100

        self.inventory: list[Item] = []
        self.relics: list[Item] = []
        self.weapon: Optional[Item] = None
        self.armor: Optional[Item] = None

        # Rassen-Fähigkeit (einmal pro Kampf)
        racial_id = RACIAL_SKILL_ID.get(race.name)
        self.racial_skill: Optional[Skill] = (
            SKILL_BY_ID[racial_id].copy()
            if racial_id and racial_id in SKILL_BY_ID
            else None
        )
        self.racial_skill_used: bool = False

        self._assign_starting_skills()

    def _assign_starting_skills(self) -> None:
        """
        Wählt 6 Startskills:
          - 1–3 klassen-spezifische Skills (aus CLASS_SKILL_POOL)
          - Rest aus dem allgemeinen Klassen-Pool (IDs 1–25)
          - Garantiert: min. 1 Angriff + 1 Verteidigung
        """
        class_name = self.char_class.name
        specific_ids = CLASS_SKILL_POOL.get(class_name, [])
        general_ids = self.char_class.skill_pool  # allgemeiner Pool (IDs 1–25)

        # 1–3 klassen-spezifische Skills
        num_specific = random.randint(1, 3)
        specific_pick = random.sample(
            specific_ids, min(num_specific, len(specific_ids))
        )
        specific_skills = [
            SKILL_BY_ID[sid].copy() for sid in specific_pick if sid in SKILL_BY_ID
        ]

        # Rest aus allgemeinem Pool
        general_pool = [
            SKILL_BY_ID[sid].copy() for sid in general_ids if sid in SKILL_BY_ID
        ]
        random.shuffle(general_pool)

        # Garantien: 1 Angriff + 1 Verteidigung
        all_candidates = specific_skills + general_pool
        attacks = [s for s in all_candidates if s.skill_type.value == "Angriff"]
        defenses = [s for s in all_candidates if s.skill_type.value == "Verteidigung"]

        selected: list[Skill] = []
        if attacks:
            selected.append(attacks[0])
        if defenses:
            selected.append(defenses[0])

        # Klassen-spezifische zuerst auffüllen
        for s in specific_skills:
            if s not in selected and len(selected) < 6:
                selected.append(s)

        # Rest aus allgemeinem Pool
        for s in general_pool:
            if s not in selected and len(selected) < 6:
                selected.append(s)

        # Notfall-Auffüllung aus allen Skills
        extras = [
            s.copy()
            for s in ALL_SKILLS
            if s.id not in {sk.id for sk in selected} and s.max_uses == 0
        ]
        random.shuffle(extras)
        while len(selected) < 6 and extras:
            selected.append(extras.pop())

        self.skills = selected[:6]

    # ── XP & Level ───────────────────────────────────────────────────────────

    def gain_xp(self, amount: int) -> list[str]:
        """Gibt XP. Gibt Meldungen zurück (inkl. Level-Up-Hinweis)."""
        messages = [f"+{amount} XP"]
        self.xp += amount
        while self.xp >= self.xp_to_next:
            self.xp -= self.xp_to_next
            self.xp_to_next = int(self.xp_to_next * 1.4)
            self._level_up()
            messages.append(f"LEVEL UP! Du bist jetzt Level {self.level}!")
        return messages

    def _level_up(self) -> None:
        self.level += 1
        self.max_hp += 10
        self.hp = min(self.hp + 10, self.max_hp)
        self.base_atk += 1
        self.base_def += 1

    # ── Ausrüstung ───────────────────────────────────────────────────────────

    def equip(self, item: Item) -> Optional[Item]:
        """Rüstet Item aus. Gibt altes Item zurück (oder None)."""
        old = None
        if item.item_type == ItemType.WEAPON:
            if self.weapon:
                old = self.weapon
                self.base_atk -= self.weapon.atk_bonus
                self.base_spd -= self.weapon.spd_bonus
            self.weapon = item
            self.base_atk += item.atk_bonus
            self.base_spd += item.spd_bonus
        elif item.item_type == ItemType.ARMOR:
            if self.armor:
                old = self.armor
                self.base_def -= self.armor.def_bonus
                self.base_spd -= self.armor.spd_bonus
            self.armor = item
            self.base_def += item.def_bonus
            self.base_spd += item.spd_bonus
        return old

    def use_potion(self, item: Item) -> str:
        """Benutzt einen Trank aus dem Inventar."""
        if item.item_type == ItemType.POTION:
            if item.heal_amount:
                healed = self.heal(item.heal_amount)
                self.inventory.remove(item)
                return f"Du trinkst {item.name} und heilist {healed} HP."
            if item.atk_bonus:
                self.base_atk += item.atk_bonus
                self.inventory.remove(item)
                return f"Du trinkst {item.name}. ATK +{item.atk_bonus}!"
        return "Das kannst du hier nicht benutzen."

    def apply_relic(self, relic: Item) -> None:
        """Wendet Relikt-Boni dauerhaft auf Stats an."""
        self.base_atk = int(self.base_atk * (1 + relic.atk_pct))
        self.base_def = int(self.base_def * (1 + relic.def_pct))
        self.base_spd = int(self.base_spd * (1 + relic.spd_pct))
        old_max = self.max_hp
        self.max_hp = int(self.max_hp * (1 + relic.hp_pct))
        self.hp += self.max_hp - old_max
        self.relics.append(relic)

    # ── Inventar ─────────────────────────────────────────────────────────────

    def show_inventory(self) -> list[str]:
        lines = []
        if self.weapon:
            lines.append(f"Waffe:   {self.weapon}")
        if self.armor:
            lines.append(f"Rüstung: {self.armor}")
        potions = [i for i in self.inventory if i.item_type == ItemType.POTION]
        if potions:
            lines.append("Tränke:  " + ", ".join(i.name for i in potions))
        if self.relics:
            lines.append("Relikte: " + ", ".join(i.name for i in self.relics))
        return lines if lines else ["Inventar ist leer."]

    # ── Zusammenfassung ──────────────────────────────────────────────────────

    def get_stats_summary(self) -> str:
        return (
            f"{self.name} | Lv.{self.level} {self.race.name} {self.char_class.name} | "
            f"HP:{self.hp}/{self.max_hp}  ATK:{self.atk}  DEF:{self.def_}  SPD:{self.spd}"
        )


# ─── Gegner-Template ──────────────────────────────────────────────────────────


@dataclass
class EnemyTemplate:  # pylint: disable=too-many-instance-attributes
    """Blaupause für einen Gegnertyp. Wird bei Enemy-Erstellung genutzt."""

    name: str
    max_hp: int
    atk: int
    def_: int
    spd: int
    xp_reward: int
    loot_chance: float  # 0.0 – 1.0
    skill_ids: list[int]
    description: str = ""


ENEMY_TEMPLATES: list[EnemyTemplate] = [
    EnemyTemplate(
        "Wireguard-Goblin",
        40,
        8,
        3,
        6,
        30,
        0.40,
        [1, 15],
        "Ein kleiner, nerviger Goblin.",
    ),
    EnemyTemplate(
        "Router-Troll",
        65,
        12,
        6,
        4,
        50,
        0.50,
        [1, 3, 15],
        "Bewacht die Brücke zum Netzwerk.",
    ),
    EnemyTemplate(
        "Firewall-Ritter", 80, 14, 10, 5, 70, 0.60, [1, 3, 21], "Kaum zu durchdringen."
    ),
    EnemyTemplate(
        "Malware-Magier",
        55,
        16,
        4,
        9,
        60,
        0.50,
        [4, 5, 22],
        "Wirft Schadcode nach dir.",
    ),
    EnemyTemplate(
        "DDoS-Dämon", 90, 18, 7, 7, 90, 0.70, [2, 14, 8], "Greift mit Schwärmen an."
    ),
    EnemyTemplate(
        "Phishing-Specter",
        50,
        12,
        3,
        11,
        55,
        0.50,
        [9, 8, 23],
        "Unsichtbar und hinterlistig.",
    ),
    EnemyTemplate(
        "Trickster-Fee", 35, 18, 2, 15, 40, 0.80, [7, 8, 23], "Klein aber gefährlich."
    ),
    EnemyTemplate(
        "Internet-Drache",
        250,
        20,
        5,
        8,
        200,
        1.00,
        [1, 4, 14, 21, 22],
        "Der Endboss. Hüter des Internets.",
    ),
]

ENEMY_BY_NAME: dict[str, EnemyTemplate] = {e.name: e for e in ENEMY_TEMPLATES}


class Enemy(Character):
    """
    Gegner — erbt von Character.
    Wird aus einem EnemyTemplate erstellt und kann level-skaliert werden.
    """

    def __init__(self, template: EnemyTemplate, level_scale: float = 1.0) -> None:
        hp = int(template.max_hp * level_scale)
        atk = int(template.atk * level_scale)
        def_ = int(template.def_ * level_scale)
        super().__init__(template.name, hp, atk, def_, template.spd)

        self.template = template
        self.xp_reward = template.xp_reward
        self.loot_chance = template.loot_chance
        self.skills = [
            SKILL_BY_ID[sid].copy() for sid in template.skill_ids if sid in SKILL_BY_ID
        ]

    def choose_skill(self) -> Skill:
        """Wählt einen zufälligen Skill aus dem Repertoire."""
        return random.choice(self.skills)


# ─── NPC-Begleiter ────────────────────────────────────────────────────────────


class Companion(Character):
    """
    Ein zufälliger NPC-Begleiter der den Spieler unterstützt.

    - Hat 4 zufällige Skills
    - Agiert jede Runde automatisch
    - Angriff → trifft zufälligen Gegner
    - Verteidigung/Buff → wirkt auf den Spieler
    """

    def __init__(self) -> None:
        race = random.choice(list(RACES.values()))
        char_class = random.choice(
            [CLASSES[c] for c in race.allowed_classes if c in CLASSES]
        )
        hp = char_class.base_hp + race.hp_bonus
        atk = char_class.base_atk + race.atk_bonus
        def_ = char_class.base_def + race.def_bonus
        spd = char_class.base_spd + race.spd_bonus

        name = f"{race.name}-{char_class.name}"
        super().__init__(name, hp, atk, def_, spd)

        self.race = race
        self.char_class = char_class

        # 4 zufällige Skills: mind. 1 Angriff + 1 Verteidigung
        specific = [
            SKILL_BY_ID[sid].copy()
            for sid in CLASS_SKILL_POOL.get(char_class.name, [])
            if sid in SKILL_BY_ID
        ]
        general = [
            SKILL_BY_ID[sid].copy()
            for sid in char_class.skill_pool
            if sid in SKILL_BY_ID
        ]
        candidates = specific + general
        random.shuffle(candidates)

        attacks = [s for s in candidates if s.skill_type.value == "Angriff"]
        defenses = [s for s in candidates if s.skill_type.value != "Angriff"]
        selected: list[Skill] = []
        if attacks:
            selected.append(attacks[0])
        if defenses:
            selected.append(defenses[0])
        for s in candidates:
            if s not in selected and len(selected) < 4:
                selected.append(s)
        while len(selected) < 4:
            selected.append(random.choice(candidates))

        self.skills = selected[:4]

    def act(
        self, enemies: list["Enemy"], player: "Player"
    ) -> tuple[Skill, "Character"]:
        """
        Wählt Skill + Ziel.
        Returns: (gewählter Skill, Ziel)
        """
        skill = random.choice(self.skills)
        alive = [e for e in enemies if e.is_alive]

        # Angriff → zufälliger Gegner; Buff/Heal → Spieler
        if skill.damage > 0 and alive:
            target: Character = random.choice(alive)
        else:
            target = player

        return skill, target
