"""
Day 74 – Natural Language Processing (NLP)
- Einfache Sentimentanalyse
- Tokenisierung
- Wort- und Satzstatistiken
"""

from textblob import TextBlob


def analyze_text(text: str) -> None:
    """Führt verschiedene NLP-Auswertungen auf dem Text durch und druckt das Ergebnis."""
    blob = TextBlob(text)

    # Sentimentanalyse
    polarity = blob.sentiment.polarity  # -1 (negativ) bis 1 (positiv)
    subjectivity = blob.sentiment.subjectivity  # 0 (objektiv) bis 1 (subjektiv)

    if polarity > 0.1:
        sentiment_label = "positiv"
    elif polarity < -0.1:
        sentiment_label = "negativ"
    else:
        sentiment_label = "neutral"

    print("\n--- NLP Analyse ---")
    print(f"Originaltext: {text}")
    print(f"Sentiment: {sentiment_label}")
    print(f"  Polarity: {polarity:.3f}")
    print(f"  Subjectivity: {subjectivity:.3f}")

    # Tokenisierung
    words = blob.words
    sentences = blob.sentences

    print("\n--- Tokenisierung & Statistik ---")
    print(f"Anzahl Wörter: {len(words)}")
    print(f"Anzahl Sätze: {len(sentences)}")
    print(f"Einzigartige Wörter: {len(set(w.lower() for w in words))}")

    # Häufigste Wörter (ganz einfache, naive Zählung)
    lower_words = [w.lower() for w in words]
    freq = {}
    for w in lower_words:
        freq[w] = freq.get(w, 0) + 1

    # Top 5 Wörter
    top_words = sorted(freq.items(), key=lambda x: x[1], reverse=True)[:5]
    print("\nHäufigste Wörter (Top 5):")
    for w, count in top_words:
        print(f"  '{w}': {count}x")

    # Einfache Rechtschreibkorrektur-Demo (für den ersten Satz)
    if sentences:
        first_sentence = sentences[0]
        corrected = first_sentence.correct()
        if str(corrected) != str(first_sentence):
            print("\n--- Rechtschreibkorrektur (erster Satz) ---")
            print(f"Original:   {first_sentence}")
            print(f"Korrigiert: {corrected}")


def main() -> None:
    print("Day 74 – Natural Language Processing (NLP)")
    print("Gib einen Text ein, der analysiert werden soll.")
    print("(Leere Eingabe beendet das Programm.)\n")

    while True:
        text = input("Text eingeben: ").strip()
        if not text:
            print("Beendet.")
            break

        analyze_text(text)
        print("\n" + "-" * 40 + "\n")


if __name__ == "__main__":
    main()
