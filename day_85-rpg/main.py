"""
main.py — Einstiegspunkt des Internet-Rettungs-RPG

Spielablauf:
    1. Intro-Text
    2. Charakter erstellen (Name → Rasse → Klasse)
    3. Startskills anzeigen
    4. Karte generieren
    5. Schleife: Pfad wählen → Ereignis → nächste Ebene
    6. Sieg oder Game Over
"""

from character import CLASSES, RACES, Companion, Player
from display import (
    ASCII_GAME_OVER,
    ASCII_TITLE,
    ASCII_VICTORY,
    Color,
    ask_choice,
    print_header,
    print_separator,
)
from path import generate_map, print_map, run_event

# ─── Charaktererstellung ─────────────────────────────────────────────────────


def _show_race_info(race_name: str) -> None:
    """Zeigt die vollständige Info einer Rasse an."""
    r = RACES[race_name]
    print_header(f"RASSE: {r.name}")
    print(f"  {Color.BOLD}{r.description}{Color.RESET}\n")
    print(f"  {Color.DIM}{r.lore}{Color.RESET}\n")
    print_separator()
    bonuses = (
        f"HP {'+' if r.hp_bonus >= 0 else ''}{r.hp_bonus}  "
        f"ATK {'+' if r.atk_bonus >= 0 else ''}{r.atk_bonus}  "
        f"DEF {'+' if r.def_bonus >= 0 else ''}{r.def_bonus}  "
        f"SPD {'+' if r.spd_bonus >= 0 else ''}{r.spd_bonus}"
    )
    print(f"  {Color.CYAN}Stats:          {bonuses}{Color.RESET}")
    print(f"  {Color.CYAN}Klassen:        {', '.join(r.allowed_classes)}{Color.RESET}")
    print(f"  {Color.MAGENTA}Rassen-Fähigkeit: {r.racial_ability}{Color.RESET}")
    print(f"  {Color.DIM}  → {r.racial_desc}{Color.RESET}")
    print()


def _browse_races() -> str:
    """
    Lässt den Spieler Rassen einzeln durchblättern.
    Returns: Name der gewählten Rasse.
    """
    race_names = list(RACES.keys())
    idx = 0

    while True:
        _show_race_info(race_names[idx])
        nav = ask_choice(
            [
                f"Diese Rasse wählen: {race_names[idx]}",
                f"Nächste Rasse →  ({race_names[(idx + 1) % len(race_names)]})",
                f"← Vorherige Rasse ({race_names[(idx - 1) % len(race_names)]})",
            ],
            "",
        )

        if nav == 0:
            return race_names[idx]
        idx = (idx + 1) % len(race_names) if nav == 1 else (idx - 1) % len(race_names)


def create_character() -> Player:
    print_header("CHARAKTERERSTELLUNG")

    # Name
    raw = input(f"{Color.CYAN}Wie heißt du, Held:in? {Color.RESET}").strip()
    name = raw or "Held"

    # Rasse — Browse-Menü
    print(f"\n{Color.CYAN}Blättere durch die Rassen und wähle deine.{Color.RESET}\n")
    input(f"{Color.DIM}[ENTER zum Starten]{Color.RESET}")
    chosen_race = RACES[_browse_races()]

    # Klasse wählen (nur erlaubte Klassen dieser Rasse)
    print_header(f"KLASSE WÄHLEN — {chosen_race.name}")
    class_names = chosen_race.allowed_classes
    for i, cname in enumerate(class_names, 1):
        c = CLASSES[cname]
        stats = (
            f"HP:{c.base_hp + chosen_race.hp_bonus}  "
            f"ATK:{c.base_atk + chosen_race.atk_bonus}  "
            f"DEF:{c.base_def + chosen_race.def_bonus}  "
            f"SPD:{c.base_spd + chosen_race.spd_bonus}"
        )
        print(f"  {Color.BOLD}[{i}]{Color.RESET} {cname:14} — {c.description}")
        print(f"       {Color.CYAN}{stats}{Color.RESET}\n")

    class_idx = ask_choice(class_names, "Klasse wählen")
    chosen_class = CLASSES[class_names[class_idx]]

    player = Player(name, chosen_race, chosen_class)

    # Startübersicht
    print_header(f"Dein Charakter: {player.get_stats_summary()}")
    print(f"{Color.BOLD}Deine Startskills:{Color.RESET}\n")
    for s in player.skills:
        print(f"  • {s}")
    if player.racial_skill:
        print(
            f"\n  {Color.MAGENTA}⚡ Rassen-Fähigkeit: {player.racial_skill.name}"
            f" — {player.racial_skill.description}{Color.RESET}"
        )

    print_separator()
    input(f"\n{Color.CYAN}[ENTER — Abenteuer beginnen!]{Color.RESET}")

    return player


# ─── Statistiken am Ende ─────────────────────────────────────────────────────


def _print_run_summary(player: Player, reached_level: int) -> None:
    print_header("LAUF-ZUSAMMENFASSUNG")
    print(f"  Charakter:    {player.get_stats_summary()}")
    print(f"  Ebene:        {reached_level}/6")
    print(f"  Relikte:      {len(player.relics)}")
    if player.relics:
        for r in player.relics:
            print(f"              • {r.name}")
    print(f"  Inventar:     {len(player.inventory)} Tränke")
    print()


# ─── Hauptspiel-Schleife ─────────────────────────────────────────────────────


def run_game() -> None:
    print(ASCII_TITLE)
    print(f"""{Color.CYAN}
  In Deutschland ist das Internet ausgefallen.

  Ein mächtiger Drache hat die Hauptzentrale besetzt
  und hütet das Internet als seinen persönlichen Schatz.

  Keine E-Mails. Kein Netflix. Keine Katzenvideos.

  Du bist die letzte Hoffnung.
  Besiege den Drachen. Rette das Internet.

  Für die Memes. Für die Katzenvideos. Für uns alle.
{Color.RESET}""")

    input(f"{Color.CYAN}[ENTER zum Starten]{Color.RESET}")

    player = create_character()
    companion = Companion()
    game_map = generate_map()

    print_header("DEIN BEGLEITER")
    print(
        f"  {Color.BLUE}{companion.name}{Color.RESET} begleitet dich auf deiner Reise!"
    )
    print(f"  Skills: {', '.join(s.name for s in companion.skills)}")
    input(f"\n{Color.CYAN}[ENTER — Los geht's!]{Color.RESET}")

    current_level = 0

    while current_level < len(game_map):
        level_nodes = game_map[current_level]

        print_map(game_map, current_level)

        # Pfad wählen (Boss hat nur einen Pfad)
        if len(level_nodes) == 1:
            chosen_node = level_nodes[0]
        else:
            chosen_node = level_nodes[ask_choice(["Weg A", "Weg B"], "Welchen Weg")]

        # Inventar-Kurzinfo anzeigen
        inv_lines = player.show_inventory()
        print(f"\n{Color.DIM}Inventar: {' | '.join(inv_lines)}{Color.RESET}\n")

        survived = run_event(player, chosen_node, companion)
        chosen_node.visited = True

        if not survived:
            print(ASCII_GAME_OVER)
            _print_run_summary(player, current_level + 1)
            break

        current_level += 1

        if current_level == len(game_map):
            print(ASCII_VICTORY)
            print(f"\n{Color.GREEN}{Color.BOLD}Das Internet ist gerettet!{Color.RESET}")
            print(
                f"{Color.GREEN}Deutschland dankt dir. Besonders die Streamingdienste.{Color.RESET}\n"
            )
            _print_run_summary(player, 11)

    input(f"\n{Color.CYAN}[ENTER zum Beenden]{Color.RESET}")


# ─── Einstiegspunkt ──────────────────────────────────────────────────────────

if __name__ == "__main__":
    run_game()
