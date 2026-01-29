#!/usr/bin/env python3
from pathlib import Path
import urllib.parse
import urllib.request

FLAGS = [
    "eu",
    "at",
    "be",
    "bg",
    "hr",
    "cy",
    "cz",
    "dk",
    "ee",
    "fi",
    "fr",
    "de",
    "gr",
    "hu",
    "ie",
    "it",
    "lv",
    "lt",
    "lu",
    "mt",
    "nl",
    "pl",
    "pt",
    "ro",
    "sk",
    "si",
    "es",
    "se",
    "al",
    "ba",
    "ge",
    "md",
    "me",
    "mk",
    "rs",
    "tr",
    "ua",
    "gl",
]

OUT_DIR = Path("assets/flags")
OUT_DIR.mkdir(parents=True, exist_ok=True)

BASE_URL = "https://flagcdn.com"


def download_flag(code: str) -> None:
    dest = OUT_DIR / f"{code}.svg"
    url = f"{BASE_URL}/{code}.svg"
    print(f"Downloading {code} from {url}")
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": "buy-from-eu-badge-generator/1.0 (+https://flagcdn.com/)",
            "Accept": "image/svg+xml,q=0.9,*/*;q=0.8",
        },
    )
    with urllib.request.urlopen(req) as response:
        data = response.read()
    dest.write_bytes(data)


def main() -> None:
    for code in FLAGS:
        download_flag(code)


if __name__ == "__main__":
    main()
