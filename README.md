# JW Library Merger

Aplikacja w przeglądarce do **scalania** i **edycji** kopii zapasowych JW Library (pliki `.jwlibrary`).

- **Merge**: łączy kopie z kilku urządzeń (np. telefonu i tabletu) w jeden plik, bez utraty notatek, zaznaczeń, zakładek, tagów i playlist.
- **Edit backup**: pozwala przejrzeć i poprawić jedną kopię: edytować lub usuwać notatki, zmieniać kolory zaznaczeń, porządkować tagi.

Działa na komputerze i na telefonie, także bez internetu. **Twoje pliki nigdy nie opuszczają urządzenia.** Całe przetwarzanie odbywa się w przeglądarce.

### ▶ Otwórz aplikację: https://wolronick.github.io/jwlibrary-merger/

> To nieoficjalne narzędzie, niezwiązane z twórcami JW Library. Zanim przywrócisz w JW Library plik przygotowany przez tę aplikację, **zachowaj oryginalne kopie**.

---

## Spis treści

1. [Uruchomienie](#uruchomienie)
2. [Scalanie kopii — krok po kroku](#scalanie-kopii--krok-po-kroku)
3. [Edycja kopii — krok po kroku](#edycja-kopii--krok-po-kroku)
4. [Jak działa scalanie](#jak-działa-scalanie)
5. [Co zrobić, gdy…](#co-zrobić-gdy)
6. [Prywatność i bezpieczeństwo](#prywatność-i-bezpieczeństwo)
7. [Dobre praktyki](#dobre-praktyki)
8. [Dla programistów](#dla-programistów)

---

## Uruchomienie

### W przeglądarce (zalecane)

Otwórz https://wolronick.github.io/jwlibrary-merger/. Zawsze dostajesz najnowszą wersję. Po pierwszym otwarciu strona działa także **offline**.

### Jako aplikacja (ikona na ekranie)

| Urządzenie | Jak zainstalować |
|---|---|
| **Android** (Chrome) | menu **⋮** → **Zainstaluj aplikację** (lub **Dodaj do ekranu głównego**) |
| **iPhone / iPad** (Safari) | przycisk **Udostępnij** → **Do ekranu początkowego** |
| **Komputer** (Chrome / Edge) | ikona instalacji na pasku adresu albo przycisk **Install** w nagłówku aplikacji |

Pojawi się ikona **JWL Merger**, a aplikacja otworzy się w osobnym oknie. Aktualizacje pobiera sama przy otwarciu z internetem. Czasem trzeba ją otworzyć dwa razy, żeby zobaczyć nową wersję.

### Z pliku na dysku

Na stronie repozytorium wybierz **Code → Download ZIP**, rozpakuj archiwum i otwórz `index.html` dwuklikiem. Sam plik `index.html` bez folderu `vendor/` też zadziała, ale wtedy przy otwarciu potrzebny jest internet, bo biblioteki zostaną pobrane z CDN.

---

## Scalanie kopii — krok po kroku

Zakładka **Merge** (otwiera się domyślnie).

### 1. Wczytaj pliki

- Przeciągnij plik na pole **Backup 1**, **Backup 2**… albo kliknij pole i wybierz plik.
- Możesz też zaznaczyć kilka plików naraz przyciskiem **Choose several files…**.
- Naraz można scalić do **6 plików**. Kolejne pola dodasz przyciskiem **+ Add another slot**.

Kolejność nie ma znaczenia: aplikacja sama sortuje kopie od najstarszej do najnowszej, a **najnowsza staje się bazą**. Przy każdym pliku widać urządzenie, datę i liczbę notatek, zaznaczeń, zakładek i tagów.

Jeśli plik jest uszkodzony albo nie jest kopią JW Library, pole zaświeci się na czerwono z opisem problemu. Ten sam plik wczytany dwa razy zostanie użyty tylko raz.

### 2. Analiza: „Analyse files”

Aplikacja wykonuje **próbne scalenie**, więc liczby w podsumowaniu to dokładnie to, co trafi do wyniku. Zobaczysz:

- **podsumowanie**: ile notatek, zaznaczeń, zakładek i tagów dojdzie ze starszych kopii;
- **ostrzeżenia**, jeśli coś wymaga uwagi (patrz [Ostrzeżenia](#ostrzeżenia));
- **notatki edytowane inaczej na dwóch urządzeniach**: przy każdej obie wersje obok siebie i wybór, co zachować (patrz [Konflikty notatek](#konflikty-notatek));
- **listę elementów dodawanych ze starszych kopii**, z polami wyboru i wyszukiwarką. **Odznacz to, czego nie chcesz**, np. notatki usunięte celowo (patrz [Usunięte elementy](#usunięte-elementy)).

### 3. Scalenie: „Merge & download”

Aplikacja tworzy plik `RRRR-MM-DD_MERGED_URZĄDZENIA.jwlibrary` (np. `2026-11-18_MERGED_PHONE+TABLET.jwlibrary`), sprawdza spójność bazy i **od razu go pobiera**. Przycisk **Download merged file** zostaje na wypadek, gdyby pobieranie się nie rozpoczęło. Jeśli kontrola coś wykryje, na ekranie końcowym pojawi się żółte ostrzeżenie.

Przycisk **Review in Edit backup** otwiera wynik w zakładce edycji. Możesz go tam przejrzeć i uporządkować (np. usunąć niepotrzebne notatki „[Older version]”), a potem zapisać poprawioną wersję.

Szczegółowy przebieg scalania jest pod **Details** w kroku 2; nad nim zawsze widać bieżący etap. Na telefonie przycisk **Merge & download** jest przyklejony do dołu ekranu.

### 4. Przywrócenie w JW Library

1. Przenieś plik na urządzenie, na którym chcesz mieć scalone dane.
2. W JW Library otwórz **Ustawienia → Kopia zapasowa → Przywróć** i wybierz plik. Nazwy w menu mogą się nieco różnić w zależności od wersji aplikacji.

> ⚠️ Przywrócenie **zastępuje** wszystkie dane JW Library na tym urządzeniu. Zachowaj oryginalne kopie, dopóki nie sprawdzisz wyniku.

**Na telefonie:**
- **Android**: plik trafia do folderu **Pobrane**. Wybierz go w JW Library albo otwórz w aplikacji **Pliki** i stuknij **Udostępnij → JW Library**. Chrome na Androidzie nie pozwala stronom udostępniać plików `.jwlibrary`, dlatego nie ma tam przycisku „Share…”.
- **iPhone / iPad**: przycisk **Share…** otwiera systemowe menu udostępniania. Wybierz JW Library albo zapisz plik w aplikacji Pliki lub na Dysku Google.

---

## Edycja kopii — krok po kroku

Zakładka **Edit backup** w nagłówku. Zastępuje dawny skrypt `jwlibrary_tools.py`.

### 1. Otwórz kopię

Wybierz jeden plik `.jwlibrary`. Zobaczysz urządzenie, datę, wersję schematu, liczbę elementów oraz to, czy **hash** w `manifest.json` zgadza się z bazą. Niezgodny hash zostanie poprawiony przy zapisie.

### 2. Przeglądaj i edytuj

Stuknij element na liście, żeby go edytować. Zmiany są trzymane w pamięci do czasu zapisu.

| Tryb | Co możesz zrobić |
|---|---|
| **Notes** | szukać, filtrować po tagu, zmieniać tytuł i treść, dodawać i usuwać tagi (także nowe), usuwać notatki |
| **Highlights** | filtrować po kolorze, zmieniać kolor, usuwać zaznaczenia (przypięta notatka zostaje) |
| **Bookmarks** | zmieniać tytuł i fragment, usuwać zakładki |
| **Tags** | zmieniać nazwy, usuwać tagi (notatki zostają). Wbudowany tag Ulubione jest chroniony |
| **Clean up** | porządki w kopii (patrz niżej) |
| **Tables** | dla zaawansowanych: dowolna tabela bazy i konsola SQL |

Usuwanie dba o spójność bazy. Razem z notatką znikają jej przypisania tagów, a razem z zaznaczeniem jego zakresy. Rekordu, którego używają inne dane (np. miejsca w publikacji z notatkami), nie da się usunąć.

#### Zaznaczanie wielu elementów

Przycisk **Select** nad listą włącza zaznaczanie: stukasz elementy, a u góry pojawia się pasek z działaniami dla zaznaczonych.

- **Select all N** zaznacza wszystko, co pasuje do bieżącego wyszukiwania i filtra, także elementy jeszcze niewyświetlone.
- **Notatki**: **Add tag** i **Remove tag** (także nowy tag), **Delete**.
- **Zaznaczenia**: **Set colour**, **Delete**.
- **Zakładki i tagi**: **Delete**.

Przykład: wpisz w wyszukiwarce „Older version”, kliknij **Select**, potem **Select all**, a na koniec **Delete**.

#### Eksport notatek

W trybie **Notes** przycisk **Export…** zapisuje notatki w czytelnej postaci: wszystkie albo tylko te pasujące do wyszukiwania i filtra. Notatki są pogrupowane według ksiąg biblijnych (w kolejności kanonicznej) i publikacji, razem z miejscem, tagami, kolorem zaznaczenia i datą.

- **Print / PDF**: otwiera notatki jako stronę. Przyciskiem na górze strony albo poleceniem drukowania w przeglądarce możesz je wydrukować lub zapisać jako PDF.
- **HTML file**: ta sama strona jako plik, który otworzysz w dowolnej przeglądarce.
- **CSV (Excel)**: tabela do arkusza kalkulacyjnego. Pola są rozdzielone średnikami, więc plik otwiera się poprawnie w Excelu z polskimi ustawieniami.

#### Porządki (Clean up)

Tryb **Clean up** sprawdza kopię i pokazuje, ile znalazł każdego rodzaju problemu. Nic się nie zmienia, dopóki nie naciśniesz przycisku.

| Sprawdzenie | Co robi naprawa |
|---|---|
| **„[Older version]” notes** | usuwa wszystkie; przycisk **Review** pokazuje je najpierw na liście, gotowe do zaznaczenia |
| **Empty notes** | usuwa notatki bez tytułu i treści (zaznaczenia zostają) |
| **Duplicate highlights** | zostawia jedno z kilku identycznych zaznaczeń; notatki z pozostałych są przepinane na nie |
| **Unused tags** | usuwa Twoje tagi, które nie są przypisane do niczego |
| **Broken links** | czyści odwołania do nieistniejących danych albo usuwa rekordy, które bez nich nie mogą istnieć |

Wszystkie zmiany (także działania zbiorcze i porządki) można cofnąć przyciskiem **Discard all changes**, dopóki nie zapiszesz pliku.

### 3. Zapisz

- **Save .jwlibrary** tworzy nowy plik `RRRR-MM-DD_URZĄDZENIE_edited.jwlibrary` z przeliczonym hashem. Opcja „Set backup modification date to now” ustawia datę kopii na bieżącą.
- **Discard all changes** cofa wszystko do stanu z otwartego pliku.
- **Edycja w zewnętrznym programie** (np. DB Browser for SQLite): pobierz bazę przyciskiem **Download userData.db**, edytuj ją, **zamknij edytor**, wgraj bazę przyciskiem **Upload edited userData.db** i zapisz.

---

## Jak działa scalanie

| Dane | Jak są łączone |
|---|---|
| **Notatki** | po wewnętrznym identyfikatorze; przy różnej treści patrz [Konflikty notatek](#konflikty-notatek) |
| **Zaznaczenia** (wraz z zakresami) | po wewnętrznym identyfikatorze; ten sam fragment zaznaczony osobno na dwóch urządzeniach (to samo miejsce i ten sam zakres słów) trafia do wyniku **raz** |
| **Zakładki** | publikacja ma 10 slotów; gdy slot jest zajęty, zakładka trafia do wolnego slotu tej publikacji |
| **Tagi** i ich przypisania | tag o tej samej nazwie nie jest duplikowany; przypisania do notatek, miejsc (Ulubione) i playlist są przenoszone |
| **Pola w zeszytach** | przy różnicy zostaje wartość z najnowszej kopii |
| **Playlisty** | razem ze znacznikami oraz plikami obrazów i nagrań ze wszystkich kopii |
| **Miejsca w publikacjach** | dopasowywane po publikacji, rozdziale, języku itd., bo każde urządzenie numeruje je inaczej |

### Usunięte elementy

JW Library nie zapisuje informacji o usunięciu. Notatka usunięta na nowszym urządzeniu, która została w starszej kopii, przy scalaniu by „wróciła”. Dlatego w kroku 2 możesz odznaczyć każdy element dodawany ze starszych kopii.

Elementy oznaczone na pomarańczowo jako **probably deleted** są w starszej kopii urządzenia, ale brakuje ich w nowszej kopii **tego samego urządzenia**. Prawie na pewno zostały tam usunięte, więc są **domyślnie odznaczone**. Elementy z innych urządzeń są domyślnie zaznaczone.

### Konflikty notatek

Konflikt to ta sama notatka z **innym tytułem lub treścią** w kopiach z różnych urządzeń. W kroku 2 każda taka notatka ma kartę z obiema wersjami (z urządzeniem i datą edycji) i wyborem:

| Wybór | Wynik |
|---|---|
| **Both** (domyślnie) | wersja **edytowana najpóźniej** zostaje jako notatka, a druga jest dodawana jako osobna notatka z tytułem `[Older version] …`, więc nic nie ginie |
| **Latest only** | zostaje tylko wersja edytowana najpóźniej |
| **Other only** | zostaje tylko druga wersja |

Przyciski **Both for all** i **Latest for all** ustawiają wybór dla wszystkich kart naraz. Notatki „[Older version]” możesz później porównać i usunąć, w JW Library albo w zakładce **Edit backup**: wpisz w wyszukiwarce „Older version”.

Wcześniejsza wersja notatki z **tego samego** urządzenia nie jest konfliktem, tylko starszym stanem, i jest pomijana.

### Ostrzeżenia

| Ostrzeżenie | Co oznacza |
|---|---|
| *…loaded twice and will be used only once* | ten sam plik wczytano dwa razy, więc zostanie użyty raz |
| *date in manifest.json is missing or invalid* | datę kopii ustalono z bazy albo z daty pliku; sprawdź w logu, czy kolejność kopii jest właściwa |
| *different JW Library versions (schema …)* | kopie pochodzą z różnych wersji aplikacji; najlepiej zaktualizować JW Library na wszystkich urządzeniach i zrobić świeże kopie |
| *…could not be copied* / *integrity check* | część danych nie dała się przenieść albo baza ma problem; sprawdź wynik przed przywróceniem |
| *all 10 slots … were taken* | zakładka ze starszej kopii nie zmieściła się w publikacji i została pominięta |

---

## Co zrobić, gdy…

**…na telefonie pliku `.jwlibrary` nie da się wybrać (jest wyszarzony).**
Upewnij się, że używasz aktualnej wersji aplikacji: otwórz ją z internetem i, jeśli trzeba, zamknij i otwórz ponownie. Obecna wersja przyjmuje każdy plik i sama sprawdza, czy to kopia JW Library.

**…pole pokazuje „Could not open…”.**
Plik jest uszkodzony albo to nie kopia JW Library, np. niepełne pobieranie. Utwórz kopię w JW Library jeszcze raz i wczytaj nowy plik.

**…na Androidzie nie ma przycisku „Share…”.**
Tak ma być, bo Chrome na Androidzie nie pozwala stronom udostępniać plików `.jwlibrary`. Użyj **Download**, a potem wybierz plik z folderu **Pobrane** (szczegóły w [kroku 4](#4-przywrócenie-w-jw-library)).

**…po scaleniu wróciły notatki, które usunąłem.**
Scal jeszcze raz z oryginalnych kopii i w kroku 2 odznacz te elementy. Możesz też usunąć je w zakładce **Edit backup** w gotowym pliku.

**…chcę wydrukować notatki albo mieć je w Excelu.**
W zakładce **Edit backup**, w trybie **Notes**, użyj przycisku **Export…** (szczegóły w sekcji [Eksport notatek](#eksport-notatek)).

**…pojawiły się notatki „[Older version] …”.**
To drugie wersje notatek edytowanych na dwóch urządzeniach. Porównaj je z właściwymi notatkami i usuń zbędne.

**…JW Library nie chce przywrócić pliku.**
Najczęściej kopia pochodzi z nowszej wersji JW Library niż ta, w której ją przywracasz. Zaktualizuj JW Library. Jeśli przy scalaniu pojawiło się ostrzeżenie o wersjach schematu, zrób świeże kopie na zaktualizowanych urządzeniach i scal ponownie.

**…kopie są w złej kolejności.**
Kolejność wynika z dat w kopiach. Sprawdź log w kroku 2. Jeśli któraś kopia ma błędną datę, aplikacja to zgłosi, a najlepiej utworzyć tę kopię ponownie.

**…aplikacja pokazuje starą wersję.**
Odśwież stronę z pominięciem pamięci podręcznej (komputer: **Ctrl+F5**, Mac: **Cmd+Shift+R**). Zainstalowaną aplikację zamknij i otwórz ponownie, mając włączony internet.

---

## Prywatność i bezpieczeństwo

- Rozpakowywanie, odczyt bazy, scalanie, edycja i pakowanie odbywają się **wyłącznie w przeglądarce**. Pliki nie są nigdzie wysyłane.
- Oryginalne pliki **nie są modyfikowane**: zawsze powstaje nowy plik wynikowy.
- Aplikacja nie używa ciasteczek, kont ani analityki. Biblioteki są częścią aplikacji. Z internetu, z CDN, pobierane są tylko wtedy, gdy otwierasz sam plik `index.html` bez folderu `vendor/`.
- W repozytorium nigdy nie zapisuj swoich kopii; plik `.gitignore` blokuje pliki `.jwlibrary` i `.db`.

---

## Dobre praktyki

- **Rób kopie regularnie** i przechowuj je poza telefonem, np. na Dysku Google i na komputerze. Nazwy plików z datą i urządzeniem (np. `2026-11-18_telefon.jwlibrary`) ułatwiają porządek.
- **Przed scaleniem** zapisz oryginały wszystkich kopii. Usuń je dopiero, gdy sprawdzisz wynik.
- **Po przywróceniu** porównaj w JW Library liczbę notatek i zaznaczeń z podsumowaniem z aplikacji.
- **Scalaj świeże kopie** zrobione tuż przed scaleniem na wszystkich urządzeniach.
- **Przy dużych bibliotekach** (tysiące notatek) analiza może potrwać dłużej, więc nie zamykaj karty w trakcie.

---

## Dla programistów

### Struktura plików

| Plik | Rola |
|---|---|
| `index.html` | cała aplikacja (HTML, CSS, JavaScript) |
| `sw.js` | service worker: działanie offline; **zwiększ `VERSION`** po zmianie plików w `vendor/` lub `icons/` |
| `manifest.webmanifest`, `icons/` | instalacja jako aplikacja (PWA) |
| `vendor/` | [sql.js](https://github.com/sql-js/sql.js) 1.10.2 (licencja MIT) i [JSZip](https://github.com/Stuk/jszip) 3.10.1 (licencja MIT lub GPLv3), z plikami licencji |

### Uruchomienie lokalne

Service worker i lokalne biblioteki wymagają serwera HTTP:

```bash
python3 -m http.server 8000
```

Następnie otwórz http://localhost:8000/.

### Publikacja

Strona jest publikowana przez **GitHub Pages** z gałęzi `main` (folder główny). Każda zmiana scalona do `main` trafia na stronę w ciągu 1–2 minut.

### Format pliku `.jwlibrary`

To archiwum ZIP z plikami:
- `manifest.json`, w którym `userDataBackup.hash` to SHA-256 bazy;
- `userData.db`, czyli baza SQLite;
- opcjonalnie pliki multimediów z playlist.
