# pylint: skip-file

import argparse
import sys


def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Ein einfaches Kommandozeilen-Rechentool."
    )

    parser.add_argument(
        "--verbose",
        "-v",
        action="store_true",
        help="Zeige zusätzliche Informationen zur Berechnung an.",
    )

    subparsers = parser.add_subparsers(
        dest="command",
        required=True,
        help="Verfügbare Befehle",
    )

    def add_operation_subparser(name: str, help_text: str):
        p = subparsers.add_parser(name, help=help_text)
        p.add_argument("a", type=float, help="Erste Zahl")
        p.add_argument("b", type=float, help="Zweite Zahl")
        return p

    add_operation_subparser("add", "Addiert zwei Zahlen.")
    add_operation_subparser("sub", "Subtrahiert zwei Zahlen (a - b).")
    add_operation_subparser("mul", "Multipliziert zwei Zahlen.")
    add_operation_subparser("div", "Dividiert zwei Zahlen (a / b).")
    add_operation_subparser("mod", "Modulo zwei Zahlen (a % b).")

    return parser


def handle_command(args: argparse.Namespace) -> float:
    a = args.a
    b = args.b

    if args.command == "add":
        result = a + b
    elif args.command == "sub":
        result = a - b
    elif args.command == "mul":
        result = a * b
    elif args.command == "mod":
        result = a % b
    elif args.command == "div":
        if b == 0:
            raise ZeroDivisionError("Division durch 0 ist nicht erlaubt.")
        result = a / b
    else:
        raise ValueError(f"Unbekannter Befehl: {args.command}")

    if args.verbose:
        print(f"[INFO] Operation: {args.command}, a={a}, b={b}, Ergebnis={result}")

    return result


def main(argv: list[str] | None = None) -> int:
    if argv is None:
        argv = sys.argv[1:]

    parser = create_parser()

    try:
        args = parser.parse_args(argv)
        result = handle_command(args)
        print(f"Ergebnis: {result}")
        return 0
    except ZeroDivisionError as e:
        print(f"Fehler: {e}", file=sys.stderr)
        return 1
    except Exception as e:
        print(f"Unerwarteter Fehler: {e}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
