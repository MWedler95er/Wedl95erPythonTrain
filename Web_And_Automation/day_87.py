from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup

_DOPPEL_LINE = "=" * 40 + "\n"
_SIMPEL_LINE = "-" * 40 + "\n"
TXT_FILE = "s_c.md"


def write_c_s(txt_file, text_input):
    with open(txt_file, "a+", encoding="utf-8") as bare_txt:
        bare_txt.writelines(text_input)
    return "DONE"


def scrape_products(aktuell_url: str):
    """
    Holt Produktdaten (Titel und Preis) von einer gegebenen URL.
    Erwartet eine Seite im Stil von webscraper.io/e-commerce.
    """

    # 1. Webseite laden
    response = requests.get(aktuell_url, timeout=10)
    response.raise_for_status()  # Fehler werfen, falls die Seite nicht geladen werden kann

    # 2. HTML parsen
    soup = BeautifulSoup(response.text, "html.parser")

    # 3. Elemente finden
    product_items = soup.select("div.thumbnail")
    _found_produnkt = (
        f"Anzahl gefundener Produkte: {len(product_items)} auf {aktuell_url}"
    )
    _g_prudukte = "Gefundene Produkte:"
    print(_DOPPEL_LINE)
    print(_found_produnkt)
    print(_g_prudukte)
    print(_SIMPEL_LINE)
    write_c_s(TXT_FILE, _DOPPEL_LINE)
    write_c_s(TXT_FILE, _found_produnkt)
    write_c_s(TXT_FILE, _g_prudukte)
    write_c_s(TXT_FILE, _SIMPEL_LINE)

    for item in product_items:
        title_tag = item.select_one("a.title")
        price_tag = item.select_one("h4.price")

        title = title_tag.get_text(strip=True) if title_tag else "Kein Titel gefunden"
        price = price_tag.get_text(strip=True) if price_tag else "Kein Preis gefunden"

        _produkt = f"Produkt: {title}"
        _preis = f"Preis:   {price}"
        print(_produkt)
        print(_preis)
        print(_SIMPEL_LINE)
        write_c_s(TXT_FILE, _produkt)
        write_c_s(TXT_FILE, _preis)
        write_c_s(TXT_FILE, _SIMPEL_LINE)


def collect_links(start_url: str) -> list[str]:
    """
    Sammelt alle internen Links auf der gegebenen Startseite.
    Gibt eine Liste von absoluten URLs zurück.
    """

    response = requests.get(start_url, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    found_urls: list[str] = []

    # Domain der Start-URL merken, damit wir nur interne Links nehmen
    parsed_start = urlparse(start_url)
    base_netloc = parsed_start.netloc

    for a_tag in soup.find_all("a", href=True):
        href = a_tag["href"]

        # Absolute URL aus relative + Basis-URL bauen
        full_url = urljoin(start_url, href)

        parsed_full = urlparse(full_url)
        # Nur Links innerhalb derselben Domain behalten
        if parsed_full.netloc == base_netloc:
            if full_url not in found_urls:
                found_urls.append(full_url)

    print()
    _found_urls_c = f"Anzahl gefundener Links auf {start_url}: {len(found_urls)}"
    print(_found_urls_c)
    write_c_s(TXT_FILE, _found_urls_c)

    return found_urls


if __name__ == "__main__":
    START_URL = "https://webscraper.io/test-sites/e-commerce/allinone"

    # 1. Links einsammeln (Crawler-Teil)
    urls_to_visit = collect_links(START_URL)

    # Optional: Start-URL selbst auch scrapen
    if START_URL not in urls_to_visit:
        urls_to_visit.insert(0, START_URL)

    # 2. Alle gefundenen URLs nacheinander scrapen (Scraper-Teil)
    for url in urls_to_visit:
        _end_cr_and_scr = f"\nCrawle und scrape: {url}"
        print(_end_cr_and_scr)
        scrape_products(url)
        write_c_s(TXT_FILE, _end_cr_and_scr)
