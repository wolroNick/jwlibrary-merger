# JW Library Merger — README

Aplikacja webowa (jeden plik HTML) do **scalania dwóch lub więcej kopii zapasowych `.jwlibrary`** — np. backupu z telefonu i z tabletu — w jeden plik, bez utraty notatek, zaznaczeń, zakładek i tagów z żadnego z urządzeń.

Cały proces działa **lokalnie w przeglądarce**. Żaden plik ani żadne dane nie są wysyłane na jakikolwiek serwer.

---

## Wymagania

- Nowoczesna przeglądarka (Chrome, Firefox, Edge lub Safari) z włączonym JavaScriptem.
- Jednorazowe połączenie z internetem — przy pierwszym otwarciu strona wczytuje z CDN dwie biblioteki: `sql.js` (obsługa bazy SQLite w przeglądarce) i `JSZip` (rozpakowywanie/pakowanie plików `.jwlibrary`, które są zwykłymi archiwami ZIP).
- Pliki `.jwlibrary`, które chcesz scalić (co najmniej dwa).

## Jak uruchomić

Nie trzeba niczego instalować. Wystarczy otworzyć plik `jwlibrary-merger.html`:

- dwuklik na plik, albo
- przeciągnięcie pliku do okna otwartej przeglądarki, albo
- kliknięcie prawym przyciskiem → „Otwórz za pomocą" → wybrana przeglądarka.

## Krok po kroku

### 1. Wgraj pliki

Na ekranie startowym są dwa pola do wgrania plików — **„Older backup"** i **„Newer backup"**. Wgraj do nich swoje pliki `.jwlibrary` (przeciągnij albo kliknij, żeby wybrać z dysku). Jeśli masz więcej niż dwa backupy do scalenia (np. z trzech urządzeń), kliknij **„+ Add another file"**, żeby dodać kolejne pole.

Nie musisz się martwić, do którego pola trafi który plik — aplikacja sama sortuje je chronologicznie na podstawie daty ostatniej modyfikacji.

Każdy wgrany plik pokazuje krótkie podsumowanie (liczba notatek, zaznaczeń, zakładek, tagów), żebyś mógł zweryfikować, że to właściwy plik.

**Jeśli plik jest uszkodzony** albo nie jest poprawnym backupem `.jwlibrary` (np. brakuje w nim `manifest.json` lub `userData.db`), pole pokaże czerwony komunikat błędu z opisem problemu — możesz wtedy wgrać inny plik w to samo miejsce.

### 2. Kliknij „Analyse files"

Przycisk aktywuje się po wgraniu co najmniej dwóch plików. Aplikacja:

- sortuje pliki od najstarszego do najnowszego,
- porównuje zawartość każdego starszego backupu z najnowszym,
- pokazuje w logu, ile nowych notatek, zaznaczeń, zakładek i tagów zostanie dodanych z każdego starszego pliku,
- wyświetla tabelę **konfliktów** — czyli notatek, które istnieją w obu backupach pod tym samym identyfikatorem, ale mają inną treść lub tytuł (np. edytowałeś tę samą notatkę na dwóch urządzeniach).

### 3. Kliknij „Merge & download"

Aplikacja tworzy nowy, scalony plik i automatycznie zaczyna jego pobieranie: `RRRR-MM-DD_MERGED.jwlibrary`.

### 4. Zaimportuj scalony plik w JW Library

**JW Library → Ustawienia → Kopia zapasowa → Przywórz** i wybierz nowo pobrany plik.

> **Zanim to zrobisz:** zachowaj gdzieś oryginalne pliki `.jwlibrary`, na wszelki wypadek. Import w JW Library zastępuje bieżące dane na urządzeniu.

---

## Co jest scalane

| Dane | Uwagi |
|---|---|
| Notatki (Note) | patrz sekcja „Jak działają konflikty notatek" poniżej |
| Zaznaczenia (UserMark + BlockRange) | dopasowywane po unikalnym identyfikatorze zaznaczenia |
| Zakładki (Bookmark) | z uwzględnieniem unikalności slotu zakładki |
| Tagi (Tag) i przypisania tagów (TagMap) | tagi o tej samej nazwie nie są duplikowane |
| Miejsca w publikacjach (Location) | używane wewnętrznie do poprawnego dopasowania notatek/zaznaczeń/zakładek |
| Pola formularzy w zeszytach (InputField) | np. wypełnione pola w publikacjach typu „zeszyt" |

## Czego aplikacja **nie** scala

- **Playlisty** (`PlaylistItem` i powiązane tabele) — nie są obecnie obsługiwane. Jeśli korzystasz z playlist w JW Library, ta funkcja nie przeniesie ich z starszego backupu.

## Jak działają konflikty notatek

Konflikt to sytuacja, w której **ta sama notatka** (ten sam wewnętrzny identyfikator) ma **inny tytuł lub inną treść** w dwóch backupach — czyli np. edytowałeś tę samą notatkę na telefonie i na tablecie, w różny sposób.

W takim przypadku aplikacja **nie usuwa żadnej wersji**:

1. Nowsza wersja notatki zostaje w scalonym pliku bez zmian.
2. Starsza wersja jest dodawana jako **osobna, nowa notatka**, z tytułem poprzedzonym `[Older version]`.
3. Możesz później otworzyć obie notatki w JW Library, porównać je i ręcznie scalić lub usunąć tę, która jest zbędna.

Konflikty są widoczne w tabeli już na etapie analizy (krok 2), zanim jeszcze pobierzesz scalony plik.

## Ostrzeżenia, na które warto zwrócić uwagę

Aplikacja pokazuje w logu ostrzeżenia (żółte/pomarańczowe wpisy), jeśli:

- **Data w manifeście jednego z plików jest brakująca lub niepoprawna** — aplikacja wtedy sama próbuje ustalić datę na podstawie zawartości bazy albo daty modyfikacji samego pliku, żeby nie pomylić kolejności „starszy → nowszy".
- **Backupy mają różne wersje schematu bazy** (`schemaVersion` w manifeście) — może to oznaczać, że pliki pochodzą z bardzo różnych wersji JW Library i scalenie może się nie powiedzie lub dać niekompletny wynik.
- **Podczas scalania wystąpiły błędy SQL** — w takim wypadku pobrany plik i tak zostanie utworzony, ale ostrzeżenie (widoczne również na ekranie końcowym) sygnalizuje, że warto dokładnie zweryfikować wynik przed zaimportowaniem go i usunięciem oryginałów.

## Bezpieczeństwo i prywatność

- Całe przetwarzanie (rozpakowywanie, odczyt bazy SQLite, scalanie, pakowanie) odbywa się **lokalnie w przeglądarce** — pliki nie są przesyłane na żaden serwer.
- Oryginalne pliki `.jwlibrary` **nie są modyfikowane** — powstaje zupełnie nowy plik wynikowy.
- Jedyny ruch sieciowy to jednorazowe wczytanie bibliotek `sql.js` i `JSZip` z CDN przy pierwszym otwarciu strony.

## Dobre praktyki

- Zachowaj oryginalne pliki `.jwlibrary` do momentu, aż sprawdzisz, że scalony plik działa poprawnie po imporcie.
- Po imporcie porównaj w JW Library liczbę notatek/zaznaczeń z podsumowaniem, które aplikacja wyświetliła po scaleniu.
- Jeśli scalasz więcej niż dwa backupy naraz, zrób to w jednej sesji (bez odświeżania strony) — kliknięcie **„Merge more files"** czyści dane z pamięci i pozwala zacząć od nowa z nowym zestawem plików.
- Przy dużych bibliotekach (tysiące zaznaczeń/notatek) analiza i scalanie mogą potrwać dłużej — nie zamykaj karty w trakcie.

## Edycja pojedynczego backupu (zakładka „Edit backup”)

Zakładka **Edit backup** w nagłówku aplikacji zastępuje dawny skrypt `jwlibrary_tools.py`. Otwierasz w niej jeden plik `.jwlibrary` i możesz:

- przeglądać, wyszukiwać, edytować i usuwać **notatki** (także ich tagi), **zaznaczenia** (zmiana koloru), **zakładki** i **tagi**,
- w trybie **Tables** edytować dowolną tabelę bazy albo uruchomić własne zapytanie SQL,
- pobrać `userData.db`, zmienić go w zewnętrznym edytorze SQLite i wgrać z powrotem,
- zapisać wynik jako nowy plik `.jwlibrary` — hash w `manifest.json` jest przeliczany automatycznie.

Usuwanie dba o spójność bazy: razem z notatką znikają jej przypisania tagów, a razem z zaznaczeniem jego zakresy (notatka zostaje). Rekordu, którego używają inne dane, nie da się usunąć. Wszystkie zmiany można cofnąć przyciskiem **Discard all changes**, dopóki nie zapiszesz pliku.
