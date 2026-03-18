"""
Day 75 – Einfaches Empfehlungssystem im Schul-Setting

Idee:
- Wir haben einige Schüler:innen und deren Lieblingsfächer.
- Für eine ausgewählte Person empfehlen wir weitere Fächer, die ähnliche Personen mögen.
"""


def similarity(subjects_a: set[str], subjects_b: set[str]) -> int:
    """
    Berechnet eine einfache Ähnlichkeit:
    Anzahl der gemeinsamen Fächer.
    """
    common = subjects_a.intersection(subjects_b)
    return len(common)


def recommend_subjects(
    target_name: str, students_subjects: dict[str, set[str]]
) -> list[tuple[str, int]]:
    """
    Gibt eine Liste von empfohlenen Fächern zurück.
    Jedes Fach bekommt eine Punktzahl basierend auf:
    - wie ähnlich andere Schüler:innen sind
    - welche zusätzlichen Fächer sie mögen
    """
    target_subjects = students_subjects[target_name]

    # 1. Ähnlichkeit zu allen anderen berechnen
    similarity_scores: dict[str, int] = {}
    for name, subjects in students_subjects.items():
        if name == target_name:
            continue  # sich selbst überspringen
        score = similarity(target_subjects, subjects)
        if score > 0:
            similarity_scores[name] = score

    # 2. Fächer sammeln, die andere mögen, target aber nicht
    subject_scores: dict[str, int] = {}
    for other_name, sim_score in similarity_scores.items():
        other_subjects = students_subjects[other_name]
        new_subjects = other_subjects - target_subjects  # nur neue Fächer

        for subj in new_subjects:
            subject_scores[subj] = subject_scores.get(subj, 0) + sim_score

    # 3. sortierte Liste (höchste Punktzahl zuerst)
    sorted_subjects = sorted(
        subject_scores.items(), key=lambda item: item[1], reverse=True
    )
    return sorted_subjects


def main() -> None:
    print("Willkommen zu Day 75 – Empfehlungssystem")
    print("Wir empfehlen Fächer basierend auf ähnlichen Schüler:innen.\n")

    # Beispiel-Daten: wer mag welche Fächer?
    students_subjects: dict[str, set[str]] = {
        "anna": {"mathe", "informatik"},
        "ben": {"informatik", "sport"},
        "carla": {"deutsch", "kunst", "informatik"},
        "david": {"mathe", "physik", "informatik"},
        "eva": {"kunst", "musik", "deutsch"},
    }

    print("Verfügbare Schüler:innen:")
    for name in students_subjects:
        print(f" - {name}")

    name = (
        input("\nFür wen sollen wir Fächer empfehlen? (Name eingeben): ")
        .strip()
        .lower()
    )

    if name not in students_subjects:
        print("Diesen Namen kenne ich nicht. Programm endet.")
        return

    print(f"\nDu hast '{name}' gewählt.")
    liked = students_subjects[name]
    print(f"{name} mag bereits: {liked}")

    recommendations = recommend_subjects(name, students_subjects)

    if not recommendations:
        print("\nKeine neuen Empfehlungen gefunden (alle Fächer schon abgedeckt?).")
    else:
        print("\nEmpfohlene Fächer für dich:")
        for subject, score in recommendations:
            print(f" - {subject} (Punktzahl: {score})")


if __name__ == "__main__":
    main()
