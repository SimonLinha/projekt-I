# Správce úkolů - Finální verze po úpravách

from typing import List, Dict

ukoly: List[Dict[str, str]] = []  # Globální seznam úkolů


def pridat_ukol() -> None:
    """Přidá nový úkol do seznamu, požaduje název i popis."""
    while True:
        nazev = input("Zadejte název úkolu: ").strip()
        if not nazev:
            print("Název úkolu nesmí být prázdný. Zkuste to znovu.")
            continue

        popis = input("Zadejte popis úkolu: ").strip()
        if not popis:
            print("Popis úkolu nesmí být prázdný. Zkuste to znovu.")
            continue

        ukol = {"nazev": nazev, "popis": popis}
        ukoly.append(ukol)
        print("Úkol byl úspěšně přidán.")
        break


def zobraz_ukoly() -> None:
    """Zobrazí všechny uložené úkoly, nebo upozorní, že seznam je prázdný."""
    if not ukoly:
        print("Žádné úkoly nejsou zadány.")
    else:
        print("Seznam úkolů:")
        for i, ukol in enumerate(ukoly, start=1):
            print(f"{i}. {ukol['nazev']} – {ukol['popis']}")


def odstranit_ukol() -> None:
    """Umožní uživateli odstranit úkol podle čísla v seznamu."""
    if not ukoly:
        print("Seznam úkolů je prázdný.")
        return

    zobraz_ukoly()
    try:
        cislo = int(input("Zadejte číslo úkolu k odstranění: "))
        if 1 <= cislo <= len(ukoly):
            odstraneny = ukoly.pop(cislo - 1)
            print(f"Úkol '{odstraneny['nazev']}' byl odstraněn.")
        else:
            print("Neplatné číslo úkolu.")
    except ValueError:
        print("Zadejte platné číslo.")
    except KeyError:
        print("Chyba při odstraňování úkolu.")


def hlavni_menu() -> None:
    """Zobrazí hlavní menu a vyhodnocuje volbu uživatele."""
    while True:
        print("\nSprávce úkolů - Hlavní menu")
        print("1. Přidat nový úkol")
        print("2. Zobrazit všechny úkoly")
        print("3. Odstranit úkol")
        print("4. Konec programu")

        try:
            moznost = int(input("Vyberte možnost (1-4): "))
        except ValueError:
            print("Zadejte platné číslo.")
            continue

        if moznost == 1:
            pridat_ukol()
        elif moznost == 2:
            zobraz_ukoly()
        elif moznost == 3:
            odstranit_ukol()
        elif moznost == 4:
            print("Ukončuji program...")
            break
        else:
            print("Neplatná volba. Zkuste to znovu.")


# Spuštění programu
if __name__ == "__main__":
    hlavni_menu()