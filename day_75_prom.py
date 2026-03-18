import pandas as pd


def load_games(csv_path: str) -> pd.DataFrame:
    df = pd.read_csv(csv_path)
    # Sicherstellen, dass Strings und Kleinbuchstaben für Vergleich
    df["name"] = df["name"].astype(str).str.lower()
    df["genre"] = df["genre"].astype(str).str.lower()
    df["tags"] = df["tags"].astype(str).str.lower()
    return df


def preprocess_tags(tags_str: str) -> set:
    return {t.strip() for t in tags_str.split(",") if t.strip()}


def similarity_score(
    user_genres: set, user_tags: set, game_genre: str, game_tags: str
) -> float:
    game_genre_set = {game_genre} if game_genre else set()
    game_tags_set = preprocess_tags(game_tags)

    # Genre-Score: 1 Punkt wenn Genre passt
    genre_score = 1.0 if (user_genres & game_genre_set) else 0.0

    # Tag-Score: Anteil gemeinsamer Tags
    if user_tags:
        common_tags = user_tags & game_tags_set
        tag_score = len(common_tags) / len(user_tags)
    else:
        tag_score = 0.0

    # Gesamt: Genre doppelt gewichten, Tags einfach
    return 2 * genre_score + tag_score


def build_user_profile_from_game(df: pd.DataFrame, fav_game_name: str):
    # passendes Spiel suchen
    row = df[df["name"].str.lower() == fav_game_name.lower()]
    if row.empty:
        return None, None

    genre = row.iloc[0]["genre"]
    tags_str = row.iloc[0]["tags"]
    user_genres = {genre} if isinstance(genre, str) else set()
    user_tags = preprocess_tags(tags_str) if isinstance(tags_str, str) else set()
    return user_genres, user_tags


def build_user_profile_from_input(genres_input: str, tags_input: str):
    user_genres = {g.strip().lower() for g in genres_input.split(",") if g.strip()}
    user_tags = {t.strip().lower() for t in tags_input.split(",") if t.strip()}
    return user_genres, user_tags


def recommend_games(df: pd.DataFrame, user_genres: set, user_tags: set, top_n: int = 5):
    df = df.copy()
    scores = []
    for _, row in df.iterrows():
        score = similarity_score(user_genres, user_tags, row["genre"], row["tags"])
        scores.append(score)

    df["similarity"] = scores

    # Spiele mit Score 0 rausfiltern
    df = df[df["similarity"] > 0]

    # Optional: Bewertung mit einbeziehen, falls es eine Spalte "rating" gibt
    if "rating" in df.columns:
        # einfache Kombination: similarity * (rating / max_rating)
        max_rating = df["rating"].max() if df["rating"].max() > 0 else 1
        df["final_score"] = df["similarity"] * (df["rating"] / max_rating)
        df = df.sort_values(by="final_score", ascending=False)
    else:
        df = df.sort_values(by="similarity", ascending=False)

    return df.head(top_n)


def show_stats(recommended_df: pd.DataFrame):
    if recommended_df.empty:
        print("Keine Empfehlungen gefunden.")
        return

    print("\nStatistiken zu den Empfehlungen:")
    # Anzahl pro Genre
    genre_counts = recommended_df["genre"].value_counts()
    print("\nEmpfohlene Spiele pro Genre:")
    print(genre_counts)

    if "rating" in recommended_df.columns:
        print("\nDurchschnittliche Bewertung der empfohlenen Spiele:")
        print(recommended_df["rating"].mean())


def main():
    csv_path = "games_march2025_cleaned_201.csv"  # hier ggf. anpassen
    df = load_games(csv_path)

    print("Willkommen zum Spiele-Empfehlungstool!")
    mode = input(
        "Möchtest du nach Lieblingsspiel (1) oder nach Genres/Tags (2) empfehlen? [1/2]: "
    ).strip()

    if mode == "1":
        fav_game = input("Gib den Namen deines Lieblingsspiels ein: ").strip()
        user_genres, user_tags = build_user_profile_from_game(df, fav_game)
        if user_genres is None:
            print(
                "Spiel nicht in der Datenbank gefunden. Versuche Modus 2 (Genres/Tags)."
            )
            return
    else:
        genres_input = input(
            "Gib deine Lieblingsgenre (kommagetrennt) ein (z.B. RPG, Action): "
        )
        tags_input = input(
            "Gib Tags ein, die dir gefallen (kommagetrennt, z.B. open world, co-op): "
        )
        user_genres, user_tags = build_user_profile_from_input(genres_input, tags_input)

    recommendations = recommend_games(df, user_genres, user_tags, top_n=5)

    print("\nEmpfohlene Spiele:")
    if recommendations.empty:
        print("Leider keine passenden Spiele gefunden.")
    else:
        for _, row in recommendations.iterrows():
            line = f"- {row['name']} (Genre: {row['genre']}"
            if "rating" in recommendations.columns:
                line += f", Bewertung: {row['rating']}"
            line += ")"
            print(line)

    show_stats(recommendations)


if __name__ == "__main__":
    main()
