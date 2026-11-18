"""
JW Library Tools
================
Trzy komendy:
  python jwlibrary_tools.py unpack  plik.jwlibrary   -> rozpakuje do folderu plik_unpacked/
  python jwlibrary_tools.py repack  plik_unpacked/   -> spakuje z powrotem i zaktualizuje hash
  python jwlibrary_tools.py rehash  plik_unpacked/   -> tylko aktualizuje hash w manifest.json

Przykładowy workflow:
  1. python jwlibrary_tools.py unpack  2025-07-06_NORBOOK.jwlibrary
  2. Otwórz userData.db w VSC (rozszerzenie SQLite) i edytuj
  3. python jwlibrary_tools.py repack  2025-07-06_NORBOOK_unpacked
"""

import sys
import os
import json
import hashlib
import zipfile
import shutil
from pathlib import Path
from datetime import datetime


# ── helpers ──────────────────────────────────────────────────────────────────

def sha256_file(path: Path) -> str:
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def find_jwlibrary_files(folder: Path) -> list[Path]:
    """Zwraca listę plików .jwlibrary w folderze (nie rekurencyjnie)."""
    return sorted(folder.glob("*.jwlibrary"))


# ── unpack ────────────────────────────────────────────────────────────────────

def unpack(source: str):
    src = Path(source)
    if not src.exists():
        print(f"Błąd: plik '{src}' nie istnieje.")
        sys.exit(1)
    if not src.suffix == ".jwlibrary":
        print(f"Ostrzeżenie: plik nie ma rozszerzenia .jwlibrary, kontynuuję...")

    out_dir = src.parent / (src.stem + "_unpacked")
    if out_dir.exists():
        answer = input(f"Folder '{out_dir}' już istnieje. Nadpisać? [t/N] ").strip().lower()
        if answer != "t":
            print("Anulowano.")
            sys.exit(0)
        shutil.rmtree(out_dir)

    out_dir.mkdir()
    with zipfile.ZipFile(src, "r") as z:
        z.extractall(out_dir)

    db_path = out_dir / "userData.db"
    manifest_path = out_dir / "manifest.json"

    print(f"\n✓ Rozpakowano do: {out_dir}/")
    print(f"  userData.db     — otwórz w SQLite (VSC lub DB Browser) i edytuj")
    print(f"  manifest.json   — nie edytuj ręcznie, hash zostanie zaktualizowany automatycznie")

    if manifest_path.exists():
        with open(manifest_path, encoding="utf-8") as f:
            m = json.load(f)
        info = m.get("userDataBackup", {})
        device = info.get("deviceName", "—")
        last_mod = info.get("lastModifiedDate", "—")
        schema = info.get("schemaVersion", "—")
        print(f"\n  Urządzenie:      {device}")
        print(f"  Ostatnia zmiana: {last_mod}")
        print(f"  Schema version:  {schema}")

    print(f"\nGotowe. Po edycji uruchom:")
    print(f"  python jwlibrary_tools.py repack \"{out_dir}\"")


# ── rehash ────────────────────────────────────────────────────────────────────

def rehash(folder: str):
    folder_path = Path(folder)
    db_path = folder_path / "userData.db"
    manifest_path = folder_path / "manifest.json"

    if not db_path.exists():
        print(f"Błąd: brak pliku userData.db w '{folder_path}'")
        sys.exit(1)
    if not manifest_path.exists():
        print(f"Błąd: brak pliku manifest.json w '{folder_path}'")
        sys.exit(1)

    new_hash = sha256_file(db_path)

    with open(manifest_path, encoding="utf-8") as f:
        manifest = json.load(f)

    old_hash = manifest.get("userDataBackup", {}).get("hash", "—")
    manifest["userDataBackup"]["hash"] = new_hash

    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(manifest, f, separators=(",", ":"), ensure_ascii=False)

    print(f"✓ Hash zaktualizowany w manifest.json")
    print(f"  Stary: {old_hash[:16]}...")
    print(f"  Nowy:  {new_hash[:16]}...")


# ── repack ────────────────────────────────────────────────────────────────────

def repack(folder: str):
    folder_path = Path(folder)

    if not folder_path.exists() or not folder_path.is_dir():
        print(f"Błąd: folder '{folder_path}' nie istnieje.")
        sys.exit(1)

    db_path = folder_path / "userData.db"
    manifest_path = folder_path / "manifest.json"

    if not db_path.exists():
        print(f"Błąd: brak pliku userData.db w '{folder_path}'")
        sys.exit(1)
    if not manifest_path.exists():
        print(f"Błąd: brak pliku manifest.json w '{folder_path}'")
        sys.exit(1)

    # Najpierw zaktualizuj hash
    print("Aktualizuję hash...")
    rehash(folder)

    # Nazwa pliku wyjściowego
    date_str = datetime.now().strftime("%Y-%m-%d")
    # Spróbuj odczytać oryginalną nazwę z manifestu
    with open(manifest_path, encoding="utf-8") as f:
        manifest = json.load(f)
    device = manifest.get("userDataBackup", {}).get("deviceName", "BACKUP")
    out_name = f"{date_str}_{device}_edited.jwlibrary"
    out_path = folder_path.parent / out_name

    # Spakuj wszystkie pliki z folderu
    with zipfile.ZipFile(out_path, "w", zipfile.ZIP_DEFLATED) as z:
        for file in sorted(folder_path.iterdir()):
            if file.is_file():
                z.write(file, file.name)

    size_kb = out_path.stat().st_size // 1024
    print(f"\n✓ Spakowano do: {out_path}")
    print(f"  Rozmiar: {size_kb} KB")
    print(f"\nAby przywrócić: JW Library → Ustawienia → Kopia zapasowa → Przywróć")


# ── main ──────────────────────────────────────────────────────────────────────

def usage():
    print(__doc__)
    sys.exit(0)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        usage()

    command = sys.argv[1].lower()
    target = sys.argv[2]

    if command == "unpack":
        unpack(target)
    elif command == "repack":
        repack(target)
    elif command == "rehash":
        rehash(target)
    else:
        print(f"Nieznana komenda: '{command}'")
        usage()
