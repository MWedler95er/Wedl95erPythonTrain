from nltk.tokenize import word_tokenize

# Einfache Wissensbasis (Frage-Stichwort -> Antwort)
FAQS = {
    "hallo": "Hallo! Wie kann ich dir helfen?",
    "hi": "Hi! Schön, dass du da bist. Was möchtest du wissen?",
    "hilfe": "Ich bin ein einfacher Chatbot. Frag mich etwas über Schule, Lernen oder Programmierung.",
    "schule": "Schule ist wichtig, um Grundlagen zu lernen. Hast du eine konkrete Frage dazu?",
    "python": "Python ist eine Programmiersprache, die sich gut zum Lernen eignet.",
    "tschüss": "Tschüss! Bis zum nächsten Mal.",
    "danke": "Gern geschehen! :)",
}


def preprocess(text: str) -> list[str]:
    """Text in Kleinbuchstaben umwandeln und in Wörter zerlegen."""
    text = text.lower()
    tokens = word_tokenize(text, language="german")
    return tokens


def find_best_answer(user_input: str) -> str:
    """Suche eine passende Antwort anhand einfacher Stichworte."""
    tokens = preprocess(user_input)

    # Falls Nutzer sich verabschiedet:
    if any(t in ["tschüss", "tschuess", "bye"] for t in tokens):
        return FAQS["tschüss"]

    # Falls Nutzer sich bedankt:
    if any(t in ["danke", "thx"] for t in tokens):
        return FAQS["danke"]

    # Prüfe bekannte Schlüsselwörter
    for keyword, answer in FAQS.items():
        if keyword in tokens:
            return answer

    # Falls nichts passt:
    return "Das habe ich leider nicht verstanden. Kannst du deine Frage anders formulieren?"


def chat():
    print("Einfacher Schul-Chatbot (Tag 76)")
    print("Schreibe 'quit' oder 'exit', um zu beenden.\n")

    while True:
        user_input = input("Du: ")

        if user_input.lower() in ["quit", "exit"]:
            print("Bot: Auf Wiedersehen! 👋")
            break

        response = find_best_answer(user_input)
        print("Bot:", response)


chat()
