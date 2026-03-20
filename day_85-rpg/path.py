"""
path.py — Karten- und Ereignis-System (Slay the Spire Stil)

Kartenstruktur:
    5 Ebenen mit je 2 wählbaren Pfaden → dann Boss
    Gesamt: 6 Ereignisse pro Run

Ereignistypen:
    COMBAT   — Kampf gegen 1–3 Gegner
    LOOT     — Schatzkiste
    CAMP     — Lagerfeuer: rasten oder Skill upgraden
    SPECIAL  — Einzigartiges Ereignis (Fee, See, Internet-Mast)
    BOSS     — Internet-Drache (immer letztes Event)
"""

from __future__ import annotations

import random
from dataclasses import dataclass, field
from enum import Enum
from typing import TYPE_CHECKING

from character import ENEMY_BY_NAME, ENEMY_TEMPLATES, Enemy, Player
from combat import run_combat
from display import ASCII_DRAGON, Color, ask_choice, print_box, print_header
from items import Item, ItemType, get_random_loot
from skills import ALL_SKILLS

if TYPE_CHECKING:
    from character import Companion

# ─── Ereignistypen & Knoten ──────────────────────────────────────────────────


class EventType(Enum):
    COMBAT = "⚔  Kampf"
    LOOT = "💰 Schatzkiste"
    CAMP = "🔥 Lager"
    SPECIAL = "✨ Spezialereignis"
    BOSS = "🐉 Endboss"


@dataclass
class Node:
    event_type: EventType
    description: str
    event_data: dict = field(default_factory=dict)
    visited: bool = False


# ─── Hilfsfunktionen ─────────────────────────────────────────────────────────


def _get_enemies(round_num: int) -> list[Enemy]:
    """Erstellt Gegner passend zum Fortschritt. Stärker = spätere Runde."""
    scale = 1.0 + round_num * 0.10
    pool = [
        t for t in ENEMY_TEMPLATES if t.name not in ("Internet-Drache", "Trickster-Fee")
    ]
    count = 1 if round_num <= 2 else (2 if round_num <= 4 else random.randint(1, 3))
    chosen = random.choices(pool, k=count)
    return [Enemy(t, level_scale=scale) for t in chosen]


def _handle_loot(player: Player, items: list[Item]) -> None:
    """Zeigt gefundene Items an und lässt den Spieler entscheiden."""
    print_header("Loot!")
    if not items:
        print(f"{Color.DIM}Leider nichts Brauchbares dabei.{Color.RESET}")
        return

    for item in items:
        print(f"\n  {Color.YELLOW}Gefunden: {item}{Color.RESET}")
        print(f"  {Color.DIM}{item.description}{Color.RESET}\n")

        if item.item_type == ItemType.POTION:
            player.inventory.append(item)
            print("  → Trank ins Inventar gelegt.")

        elif item.item_type in (ItemType.WEAPON, ItemType.ARMOR):
            choice = ask_choice([f"Ausrüsten: {item}", "Ablehnen"], "Was tun")
            if choice == 0:
                old = player.equip(item)
                if old:
                    print(f"  {Color.DIM}{old.name} abgelegt.{Color.RESET}")
                print(f"  {Color.GREEN}{item.name} ausgerüstet!{Color.RESET}")

        elif item.item_type in (ItemType.RELIC, ItemType.CURSED):
            print(f"  {Color.MAGENTA}Wird automatisch angewendet...{Color.RESET}")
            player.apply_relic(item)
            if item.item_type == ItemType.CURSED:
                print(f"  {Color.RED}Uh oh. Das war ein Fluch!{Color.RESET}")
            else:
                print(f"  {Color.GREEN}Relikt-Boni dauerhaft aktiv!{Color.RESET}")


def _handle_level_up(player: Player) -> None:
    """Level-Up Menü: Skill upgraden + ggf. neuen Skill wählen."""
    print_header(f"Level Up! Du bist jetzt Level {player.level}!")

    # Skill upgraden
    print(f"{Color.BOLD}Wähle einen Skill zum Upgraden (+10% Werte):{Color.RESET}\n")
    labels = [f"{s}  (Lv.{s.level} → Lv.{s.level + 1})" for s in player.skills]
    idx = ask_choice(labels, "Skill upgraden")
    player.skills[idx].upgrade()
    print(
        f"\n  {Color.GREEN}{player.skills[idx].name} ist jetzt Lv.{player.skills[idx].level}!{Color.RESET}"
    )

    # Ab Level 3: neuen Skill würfeln / wählen
    if player.level >= 3:
        print(
            f"\n{Color.CYAN}Ab Level 3: Du kannst einen Skill austauschen!{Color.RESET}"
        )
        choice = ask_choice(["Neuen Skill würfeln (3 zur Wahl)", "Überspringen"])
        if choice == 0:
            current_ids = {s.id for s in player.skills}
            available = [s for s in ALL_SKILLS if s.id not in current_ids]
            if available:
                picks = random.sample(available, min(3, len(available)))
                print(f"\n{Color.BOLD}Wähle einen neuen Skill:{Color.RESET}\n")
                new_idx = ask_choice([str(s) for s in picks])
                print(
                    f"\n{Color.BOLD}Welchen bisherigen Skill ersetzen?{Color.RESET}\n"
                )
                replace_idx = ask_choice([str(s) for s in player.skills], "Ersetzen")
                player.skills[replace_idx] = picks[new_idx].copy()
                print(
                    f"  {Color.GREEN}Neuer Skill: {player.skills[replace_idx].name}!{Color.RESET}"
                )


# ─── Ereignis-Handler ────────────────────────────────────────────────────────


def _event_combat(
    player: Player, round_num: int, companion: "Companion | None" = None
) -> bool:
    enemies = _get_enemies(round_num)
    result = run_combat(player, enemies, companion)

    if not result.victory:
        return False

    # XP vergeben
    for msg in player.gain_xp(result.xp):
        print(f"  {Color.GREEN}{msg}{Color.RESET}")
        if "LEVEL UP" in msg:
            _handle_level_up(player)

    # Loot verteilen
    if result.loot:
        _handle_loot(player, result.loot)

    return True


def _event_loot(player: Player) -> bool:
    print_header("Schatzkiste!")
    print("Du findest eine alte Truhe...\n")

    items = []
    for _ in range(random.randint(1, 3)):
        item = get_random_loot(include_relics=True, cursed_chance=0.08)
        if item:
            items.append(item)

    _handle_loot(player, items)
    return True


def _event_camp(player: Player) -> bool:
    print_header("Lagerfeuer")
    print("Ein ruhiger Rastplatz. Du hörst das Knistern des Feuers.\n")

    choice = ask_choice(
        [
            f"Rasten — Heile 30% max HP (aktuell +{int(player.max_hp * 0.30)} HP)",
            "Trainieren — Upgrade einen Skill",
        ]
    )

    if choice == 0:
        healed = player.heal(int(player.max_hp * 0.30))
        print(f"\n  {Color.GREEN}Du erholst dich: +{healed} HP.{Color.RESET}")
    else:
        # Simulierter Level-Up nur für das Upgrade (kein echtes Level-Up)
        print(f"\n{Color.BOLD}Wähle einen Skill zum Trainieren (+10%):{Color.RESET}\n")
        labels = [str(s) for s in player.skills]
        idx = ask_choice(labels, "Skill trainieren")
        player.skills[idx].upgrade()
        print(
            f"\n  {Color.GREEN}{player.skills[idx].name} ist jetzt Lv.{player.skills[idx].level}!{Color.RESET}"
        )

    return True


def _special_fee(player: Player) -> None:
    """Ereignis 0: Die Trickster-Fee."""
    print_box(
        "✨ Eine schimmernde Fee!",
        [
            "Eine kleine Fee flattert auf dich zu.",
            "Sie wirkt freundlich... aber trickreich.",
            "Was tust du?",
        ],
    )
    choice = ask_choice(
        [
            "Um Heilung bitten (75% Chance — manchmal stiehlt sie HP)",
            "Sie angreifen (Kampf, aber guter Loot möglich)",
        ]
    )
    if choice == 0:
        if random.random() < 0.75:
            healed = player.heal(int(player.max_hp * 0.50))
            print(f"\n  {Color.GREEN}Die Fee heilt dich um {healed} HP!{Color.RESET}")
        else:
            dmg = int(player.max_hp * 0.10)
            player.take_damage(dmg, ignore_def_pct=1.0)
            print(f"\n  {Color.RED}Die Fee lacht und stiehlt {dmg} HP!{Color.RESET}")
    else:
        fee = Enemy(ENEMY_BY_NAME["Trickster-Fee"])
        result = run_combat(player, [fee])
        if result.victory:
            for msg in player.gain_xp(result.xp):
                print(f"  {Color.GREEN}{msg}{Color.RESET}")
            if result.loot:
                _handle_loot(player, result.loot)


def _special_see(player: Player) -> None:
    """Ereignis 1: Der verfluchte See."""
    print_box(
        "🌊 Verfluchter See",
        [
            "Ein glitzernder See liegt vor dir.",
            "Tief unten scheint etwas zu leuchten...",
            "Ein Schatz? Oder ein Fluch?",
        ],
    )
    choice = ask_choice(["In den See tauchen (50% Schatz / 50% Fluch)", "Weitergehen"])
    if choice == 0:
        if random.random() < 0.50:
            item = get_random_loot(include_relics=True, cursed_chance=0.0)
            if item:
                print(f"\n  {Color.YELLOW}Du findest: {item}!{Color.RESET}")
                _handle_loot(player, [item])
            else:
                print(f"\n  {Color.DIM}Nur Schlamm da unten.{Color.RESET}")
        else:
            dmg = int(player.max_hp * 0.20)
            player.take_damage(dmg, ignore_def_pct=1.0)
            print(
                f"\n  {Color.RED}Der See war verflucht! Du verlierst {dmg} HP.{Color.RESET}"
            )


def _special_mast(player: Player) -> None:
    """Ereignis 2: Flächendeckendes 5G-Internet."""
    print_box(
        "📶 FLÄCHENDECKENDES 5G-INTERNET!",
        [
            "Du entdeckst einen mysteriösen 5G-Mast mitten im Wald.",
            "Volle Signalstärke! Alle Bars!",
            "Deine Kräfte werden magisch gebufft: ATK dauerhaft +20%!",
        ],
        color=Color.CYAN,
    )
    player.base_atk = int(player.base_atk * 1.20)
    print(f"  {Color.GREEN}ATK dauerhaft +20%! (Danke, Telekom){Color.RESET}")


_SPECIAL_EVENTS = {0: _special_fee, 1: _special_see, 2: _special_mast}


def _event_special(player: Player, event_id: int) -> bool:
    """Verzweigt zu einem von drei Spezialereignissen."""
    handler = _SPECIAL_EVENTS.get(event_id)
    if handler:
        handler(player)
    return player.is_alive


def _event_boss(player: Player, companion: "Companion | None" = None) -> bool:
    """Der finale Kampf gegen den Internet-Drachen."""
    print(ASCII_DRAGON)
    print_header("DER INTERNET-DRACHE")
    print(
        f"{Color.RED}Der Drache wacht über sein kostbarstes Gut: Das Internet Deutschlands.{Color.RESET}"
    )
    print(
        f"{Color.RED}'Kein Mensch soll je wieder YouTube schauen!' — Drache{Color.RESET}\n"
    )
    input(f"{Color.CYAN}[ENTER um zu kämpfen]{Color.RESET}")

    boss = Enemy(ENEMY_BY_NAME["Internet-Drache"])
    result = run_combat(player, [boss], companion)
    return result.victory


# ─── Map-Generator ───────────────────────────────────────────────────────────


def generate_map() -> list[list[Node]]:
    """
    Erstellt eine zufällige Karte mit 10 Ebenen (je 2 Pfade) + Boss.

    Garantien:
        - Mindestens 2 Camps verteilt (Ebene 1 und 6)
        - Mindestens 2 Loot-Knoten (Ebene 2 und 7)
        - Alle 3 Spezialereignisse kommen mehrfach vor
        - Letzte Ebene ist immer der Boss
    """
    event_pool = [
        (EventType.COMBAT, "Gegner blockieren den Weg!"),
        (EventType.COMBAT, "Ein Hinterhalt!"),
        (EventType.COMBAT, "Bewaffnete Wachen patrouillieren hier."),
        (EventType.COMBAT, "Etwas lauert im Schatten."),
        (EventType.LOOT, "Eine vergessene Schatzkiste."),
        (EventType.CAMP, "Ein ruhiger Rastplatz."),
        (EventType.SPECIAL, "Etwas Merkwürdiges liegt in der Luft..."),
    ]
    special_ids = [0, 1, 2, 0, 1, 2, 0, 1, 2, 0]
    random.shuffle(special_ids)

    game_map: list[list[Node]] = []

    for lvl in range(10):
        nodes = []
        for _ in range(2):
            etype, desc = random.choice(event_pool)
            data: dict = {"round": lvl + 1}
            if etype == EventType.SPECIAL:
                data["special_id"] = special_ids[lvl % len(special_ids)]
            nodes.append(Node(etype, desc, data))
        game_map.append(nodes)

    # Garantieren: Camps und Loot gleichmäßig verteilt
    game_map[1][0] = Node(EventType.CAMP, "Ein ruhiger Rastplatz.", {"round": 2})
    game_map[2][1] = Node(EventType.LOOT, "Eine vergessene Schatzkiste.", {"round": 3})
    game_map[6][0] = Node(EventType.CAMP, "Ein ruhiger Rastplatz.", {"round": 7})
    game_map[7][1] = Node(EventType.LOOT, "Eine alte Schatztruhe.", {"round": 8})

    # Boss immer zuletzt
    game_map.append(
        [Node(EventType.BOSS, "Der Internet-Drache wartet.", {"round": 11})]
    )

    return game_map


# ─── Karte anzeigen ──────────────────────────────────────────────────────────


def print_map(game_map: list[list[Node]], current_level: int) -> None:
    """
    Zeigt nur die aktuelle Gabelung an — nicht die gesamte Karte.
    Fortschritt wird als 'Ebene X von Y' angezeigt.
    """
    total = len(game_map) - 1  # ohne Boss
    print_header(f"WEGWAHL  —  Ebene {current_level + 1} von {total + 1}")

    nodes = game_map[current_level]

    if len(nodes) == 1:
        # Boss oder einzelner Knoten — kein Weg zu wählen
        node = nodes[0]
        print(f"  {Color.RED}Vor euch liegt: {node.event_type.value}{Color.RESET}")
        print(f"  {Color.DIM}{node.description}{Color.RESET}")
    else:
        print(f"  {Color.YELLOW}Ihr steht an einer Gabelung.{Color.RESET}")
        print(f"  {Color.DIM}Welchen Weg geht ihr?{Color.RESET}\n")
        print(
            f"  {Color.BOLD}Weg A:{Color.RESET} {nodes[0].event_type.value}  —  {nodes[0].description}"
        )
        print(
            f"  {Color.BOLD}Weg B:{Color.RESET} {nodes[1].event_type.value}  —  {nodes[1].description}"
        )

    print()


# ─── Ereignis ausführen ──────────────────────────────────────────────────────


def run_event(player: Player, node: Node, companion: "Companion | None" = None) -> bool:
    """
    Führt das Ereignis des gewählten Knotens aus.
    Returns False wenn der Spieler gestorben ist.
    """
    print_header(node.event_type.value)
    print(f"{Color.CYAN}{node.description}{Color.RESET}\n")

    match node.event_type:
        case EventType.COMBAT:
            return _event_combat(player, node.event_data.get("round", 1), companion)
        case EventType.LOOT:
            return _event_loot(player)
        case EventType.CAMP:
            return _event_camp(player)
        case EventType.SPECIAL:
            return _event_special(player, node.event_data.get("special_id", 0))
        case EventType.BOSS:
            return _event_boss(player, companion)
        case _:
            return True
