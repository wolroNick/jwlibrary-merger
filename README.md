# JW Library Merger — README

Aplikacja webowa do **scalania dwóch lub więcej kopii zapasowych `.jwlibrary`** — np. backupu z telefonu i z tabletu — w jeden plik, bez utraty notatek, zaznaczeń, zakładek i tagów z żadnego z urządzeń. Pozwala też **edytować pojedynczy backup** (zakładka „Edit backup”). Działa na komputerze i na telefonie.

Cały proces działa **lokalnie w przeglądarce**. Żaden plik ani żadne dane nie są wysyłane na jakikolwiek serwer.

**Otwórz aplikację:** https://wolronick.github.io/jwlibrary-merger/

---

## Wymagania

- Nowoczesna przeglądarka (Chrome, Firefox, Edge lub Safari) z włączonym JavaScriptem — na komputerze albo na telefonie.
- Pliki `.jwlibrary`, które chcesz scalić (co najmniej dwa) albo edytować.

## Jak uruchomić

### Z internetu (zalecane)

Otwórz https://wolronick.github.io/jwlibrary-merger/ — zawsze najnowsza wersja. Po pierwszym otwarciu strona działa także **bez internetu**.

### Jako aplikacja na telefonie lub komputerze

- **Android (Chrome):** otwórz stronę → menu ⋮ → **„Zainstaluj aplikację”** (albo **„Dodaj do ekranu głównego”**). Możesz też kliknąć przycisk **Install** w nagłówku, jeśli się pojawi.
- **iPhone / iPad (Safari):** otwórz stronę → przycisk **Udostępnij** → **„Do ekranu początkowego”**.
- **Komputer (Chrome / Edge):** ikona instalacji na pasku adresu albo przycisk **Install** w nagłówku.

Ikona „JWL Merger” pojawi się obok innych aplikacji, a aplikacja otworzy się w osobnym oknie i zadziała offline.

### Z pliku na dysku

Pobierz repozytorium (**Code → Download ZIP**), rozpakuj i otwórz `index.html` dwuklikiem. Działa też sam plik `index.html` — wtedy przy otwarciu potrzebny jest internet, bo biblioteki `sql.js` i `JSZip` są wczytywane z CDN zamiast z folderu `vendor/`.

### Na telefonie — wybór i zapis plików

- Pliki `.jwlibrary` wybierasz z „Pobranych”, Dysku Google, iCloud itp. — aplikacja sama sprawdza, czy plik jest poprawnym backupem.
- Gotowy plik pobierasz przyciskiem **Download**. Jeśli przeglądarka pozwala, pojawi się też **Share…** — otwiera systemowe menu udostępniania (np. zapis na Dysku Google albo wysłanie do JW Library). Na Androidzie Chrome zwykle nie pozwala udostępniać plików `.jwlibrary`, więc tam użyj **Download**, a potem w JW Library wybierz plik z folderu „Pobrane”.

## Krok po kroku

### 1. Wgraj pliki

Wgraj swoje pliki `.jwlibrary` do pól **„Backup 1”**, **„Backup 2”** (przeciągnij plik na pole albo kliknij, żeby wybrać z dysku) albo zaznacz kilka naraz przyciskiem **„Choose several files…”**. Możesz scalić do 6 plików; kolejne pole dodasz przyciskiem **„+ Add another slot”**.

Nie musisz się martwić, do którego pola trafi który plik — aplikacja sama sortuje je chronologicznie na podstawie daty ostatniej modyfikacji.

Każdy wgrany plik pokazuje urządzenie, datę i krótkie podsumowanie (liczba notatek, zaznaczeń, zakładek, tagów), żebyś mógł zweryfikować, że to właściwy plik. Jeśli ten sam plik wgrasz dwa razy, zostanie użyty tylko raz.

**Jeśli plik jest uszkodzony** albo nie jest poprawnym backupem `.jwlibrary` (np. brakuje w nim `manifest.json` lub `userData.db`), pole pokaże czerwony komunikat błędu z opisem problemu — możesz wtedy wgrać inny plik w to samo miejsce.

### 2. Kliknij „Analyse files"

Przycisk aktywuje się po wgraniu co najmniej dwóch plików. Aplikacja:

- sortuje pliki od najstarszego do najnowszego (najnowszy jest bazą),
- wykonuje **próbne scalenie** — liczby w podsumowaniu są dokładnie tymi, które trafią do wyniku,
- wyświetla tabelę **konfliktów** — notatek edytowanych inaczej na dwóch urządzeniach,
- pokazuje **listę elementów, które zostaną dodane ze starszych backupów** (notatki, zaznaczenia, zakładki) z polami wyboru — patrz „Usunięte elementy” niżej.

### 3. Kliknij „Merge & download"

Aplikacja tworzy nowy, scalony plik, sprawdza spójność bazy i pokazuje przycisk do pobrania pliku `RRRR-MM-DD_MERGED.jwlibrary`.

### 4. Zaimportuj scalony plik w JW Library

**JW Library → Ustawienia → Kopia zapasowa → Przywróć** i wybierz nowo pobrany plik.

> **Zanim to zrobisz:** zachowaj gdzieś oryginalne pliki `.jwlibrary`, na wszelki wypadek. Import w JW Library zastępuje bieżące dane na urządzeniu.

---

## Co jest scalane

| Dane | Uwagi |
|---|---|
| Notatki (Note) | patrz sekcja „Jak działają konflikty notatek" poniżej |
| Zaznaczenia (UserMark + BlockRange) | dopasowywane po unikalnym identyfikatorze zaznaczenia |
| Zakładki (Bookmark) | jeśli slot w danej publikacji jest zajęty, zakładka trafia do wolnego slotu |
| Tagi (Tag) i przypisania tagów (TagMap) | tagi o tej samej nazwie nie są duplikowane |
| Miejsca w publikacjach (Location) | używane wewnętrznie do poprawnego dopasowania notatek/zaznaczeń/zakładek |
| Pola formularzy w zeszytach (InputField) | np. wypełnione pola w publikacjach typu „zeszyt"; przy różnicy zostaje wartość z najnowszego backupu |
| Playlisty (PlaylistItem, znaczniki, multimedia) | razem z plikami obrazów i nagrań ze wszystkich backupów |

## Usunięte elementy

JW Library nie zapisuje informacji o usunięciu. Jeśli usunąłeś notatkę na nowszym urządzeniu, a jest ona w starszym backupie, przy scalaniu by „wróciła”. Dlatego w kroku 2 widzisz listę wszystkiego, co zostanie dodane ze starszych backupów, i możesz odznaczyć to, czego nie chcesz.

Elementy oznaczone **„probably deleted”** są w starszym backupie urządzenia, ale brakuje ich w nowszym backupie **tego samego** urządzenia — prawie na pewno zostały tam usunięte, więc domyślnie są odznaczone.

## Jak działają konflikty notatek

Konflikt to sytuacja, w której **ta sama notatka** (ten sam wewnętrzny identyfikator) ma **inny tytuł lub inną treść** w dwóch backupach — czyli np. edytowałeś tę samą notatkę na telefonie i na tablecie, w różny sposób.

W takim przypadku aplikacja **nie usuwa żadnej wersji**:

1. Wersja **edytowana najpóźniej** (według daty zmiany samej notatki) zostaje jako właściwa notatka.
2. Druga wersja jest dodawana jako **osobna, nowa notatka**, z tytułem poprzedzonym `[Older version]`.
3. Możesz później otworzyć obie notatki w JW Library, porównać je i ręcznie scalić lub usunąć tę, która jest zbędna.

Konflikty są widoczne w tabeli już na etapie analizy (krok 2), zanim jeszcze pobierzesz scalony plik.

## Ostrzeżenia, na które warto zwrócić uwagę

Aplikacja pokazuje w logu ostrzeżenia (żółte/pomarańczowe wpisy), jeśli:

- **Data w manifeście jednego z plików jest brakująca lub niepoprawna** — aplikacja wtedy sama próbuje ustalić datę na podstawie zawartości bazy albo daty modyfikacji samego pliku, żeby nie pomylić kolejności „starszy → nowszy".
- **Backupy mają różne wersje schematu bazy** (`schemaVersion` w manifeście) — pliki pochodzą z różnych wersji JW Library. Najlepiej zaktualizować aplikację na wszystkich urządzeniach i zrobić świeże backupy.
- **Nie udało się skopiować części rekordów albo kontrola spójności wykryła problem** — plik i tak zostanie utworzony, ale ekran końcowy pokaże ostrzeżenie: zweryfikuj wynik przed zaimportowaniem go i usunięciem oryginałów.
- **Zakładka nie zmieściła się** — publikacja ma tylko 10 slotów; jeśli wszystkie są zajęte, zakładka ze starszego backupu jest pomijana.

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
