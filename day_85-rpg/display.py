"""display.py — Terminal-Ausgabe: Farben, Healthbars, ASCII-Art"""


# ANSI Escape Codes — so funktionieren Farben im Terminal:
# \033[ leitet einen Steuercode ein, die Zahl bestimmt die Farbe, \033[0m setzt zurück
class Color:  # pylint: disable=too-few-public-methods
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"
    WHITE = "\033[97m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    RESET = "\033[0m"


def health_bar(current: int, maximum: int, length: int = 20) -> str:
    """Erstellt eine farbige Healthbar mit Unicode-Blöcken."""
    ratio = max(0.0, current / maximum) if maximum > 0 else 0.0
    filled = int(ratio * length)
    empty = length - filled

    # Farbe abhängig von der verbleibenden HP
    if ratio > 0.6:
        color = Color.GREEN
    elif ratio > 0.3:
        color = Color.YELLOW
    else:
        color = Color.RED

    hp_bar = f"{color}{'█' * filled}{'░' * empty}{Color.RESET}"
    return f"[{hp_bar}] {current}/{maximum}"


def print_header(text: str) -> None:
    """Druckt einen formatierten Header."""
    w = 52
    print(f"\n{Color.CYAN}{'═' * w}{Color.RESET}")
    print(f"{Color.BOLD}{Color.CYAN}{text.center(w)}{Color.RESET}")
    print(f"{Color.CYAN}{'═' * w}{Color.RESET}\n")


def print_separator() -> None:
    print(f"{Color.BLUE}{'─' * 52}{Color.RESET}")


def print_box(title: str, lines: list[str], color: str = Color.YELLOW) -> None:
    """Druckt eine formatierte Box mit Titel und Inhalt."""
    w = 50
    print(f"\n{color}┌{'─' * w}┐{Color.RESET}")
    print(f"{color}│{Color.BOLD} {title:<{w - 1}}{Color.RESET}{color}│{Color.RESET}")
    print(f"{color}├{'─' * w}┤{Color.RESET}")
    for line in lines:
        # Lange Zeilen abschneiden damit die Box nicht bricht
        truncated = line[: w - 2]
        print(f"{color}│{Color.RESET} {truncated:<{w - 1}}{color}│{Color.RESET}")
    print(f"{color}└{'─' * w}┘{Color.RESET}\n")


def ask_choice(options: list[str], prompt: str = "Wähle") -> int:
    """
    Zeigt nummerierte Optionen an und gibt den gewählten Index zurück (0-basiert).
    Wiederholt die Frage bei ungültiger Eingabe.
    """
    for i, opt in enumerate(options, 1):
        print(f"  {Color.BOLD}[{i}]{Color.RESET} {opt}")
    while True:
        try:
            raw = input(f"\n{Color.CYAN}{prompt} (1-{len(options)}): {Color.RESET}")
            choice = int(raw) - 1
            if 0 <= choice < len(options):
                return choice
            print(
                f"{Color.RED}Bitte eine Zahl zwischen 1 und {len(options)} eingeben.{Color.RESET}"
            )
        except ValueError:
            print(f"{Color.RED}Bitte eine Zahl eingeben.{Color.RESET}")


# ─── ASCII-Art ───────────────────────────────────────────────────────────────

ASCII_DRAGON = f"""{Color.RED}
        __   __
       /  \\_/  \\
      ( o   o   )    INTERNET-DRACHE
       \\   ∆   /   "Das Internet gehört MIR!"
   ~~~~~\\_____/~~~~~
{Color.RESET}"""

ASCII_VICTORY = f"""{Color.GREEN}
    ╔══════════════════════════════╗
    ║   🌐  INTERNET  GERETTET!  🌐 ║
    ║          \\( ^ _ ^ )/         ║
    ║    Die Katzenvideos sind      ║
    ║         wieder online!        ║
    ╚══════════════════════════════╝
{Color.RESET}"""

ASCII_GAME_OVER = f"""{Color.RED}
    ╔══════════════════════════════╗
    ║         GAME  OVER           ║
    ║      404: Hero not found     ║
    ║   Das Internet bleibt dunkel ║
    ╚══════════════════════════════╝
{Color.RESET}"""

ASCII_TITLE = f"""{Color.CYAN}
 ██████╗ ██████╗  █████╗  ██████╗██╗  ██╗███████╗███╗  ██╗
 ██   ██╗██   ██╗██   ██╗██      ██║  ██║██      ████╗ ██║
 ██   ██╗██████╔╝███████║██║     ███████║█████╗  ██╔██╗██║
 ██   ██╗██   ██╗██   ██║██║     ██╔══██║██      ██║╚████║
 ██████╔╝██   ██║██   ██║╚██████╗██║  ██║███████╗██║ ╚███║
 ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚══╝
         R E T T U N G S - R P G    v1.0
{Color.RESET}"""
