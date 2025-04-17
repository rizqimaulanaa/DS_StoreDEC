
import argparse
import requests
import os
from ds_store import DSStore

def download_dsstore(url, temp_path="temp_dsstore"):
    try:
        r = requests.get(url, timeout=10)
        if r.status_code == 200:
            with open(temp_path, "wb") as f:
                f.write(r.content)
            return temp_path
        else:
            print(f"[!] Gagal unduh: HTTP {r.status_code}")
    except Exception as e:
        print(f"[!] Error saat mengunduh: {e}")
    return None

def parse_dsstore(path):
    try:
        with DSStore.open(path, 'r') as d:
            found = set()
            for entry in d:
                found.add(entry.filename)
        print("\n[+] File ditemukan di .DS_Store:")
        for name in sorted(found):
            print(f" - {name}")
    except Exception as e:
        print(f"[!] Gagal parse .DS_Store: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="DS_Store Decryptor - Mendukung URL dan file lokal")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--url", help="URL ke file .DS_Store (contoh: https://example.com/.DS_Store)")
    group.add_argument("--file", help="Path ke file .DS_Store lokal")
    args = parser.parse_args()

    if args.url:
        temp_file = download_dsstore(args.url)
        if temp_file:
            parse_dsstore(temp_file)
            os.remove(temp_file)
    elif args.file:
        parse_dsstore(args.file)
