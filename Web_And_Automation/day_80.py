import requests
from bs4 import BeautifulSoup


def scrape_products():
    """
    Beispiel: Wir holen Produktdaten (Titel und Preis)
    von der Testseite webscraper.io.
    """

    url = "https://webscraper.io/test-sites/e-commerce/allinone"

    # 1. Webseite laden
    response = requests.get(url, timeout=10)
    response.raise_for_status()  # Fehler werfen, falls die Seite nicht geladen werden kann

    # 2. HTML parsen
    soup = BeautifulSoup(response.text, "html.parser")

    # 3. Elemente finden
    product_items = soup.select("div.thumbnail")
    print("=" * 40)
    print(f"Anzahl gefundener Produkte: {len(product_items)}")

    print("Gefundene Produkte:")
    print("-" * 40)

    for item in product_items:
        title_tag = item.select_one("a.title")
        price_tag = item.select_one("h4.price")

        title = title_tag.get_text(strip=True) if title_tag else "Kein Titel gefunden"
        price = price_tag.get_text(strip=True) if price_tag else "Kein Preis gefunden"

        print(f"Produkt: {title}")
        print(f"Preis:   {price}")
        print("-" * 40)


if __name__ == "__main__":
    scrape_products()
